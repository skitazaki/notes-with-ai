---
title: "Metadata as Query Planning"
date: "2026-05-22T10:00:00+09:00"
tags: ["Metadata", "Data", "SQL", "Architecture"]
categories: ["Technology", "Data"]
draft: false
---

Part 4 ended at the point where lakehouse tables became authoritative metadata structures.

An engine no longer treats a dataset as a loose directory of files. It resolves a table version, learns which files are live, and only then decides what work to schedule. That shift is important because query execution quality is shaped long before any scan operator starts decoding bytes.

That is where metadata becomes query planning.

This article extends [Metadata at Lakehouse Scale](/blog/metadata/part4-lakehouse-metadata/) and the series overview in [Metadata Systems - From Column Comments to Distributed Control Planes](/blog/metadata/). The practical question is not whether optimizers are clever in the abstract. It is what information they need before execution begins, how that information changes the plan, and what happens when the metadata is weak, stale, or misleading.

## Before a Query Reads Data, It Reads Metadata

Consider a straightforward analytical query:

```sql
SELECT customer_id, sum(amount_jpy) AS revenue
FROM sales
WHERE order_date >= DATE '2026-05-01'
  AND order_date < DATE '2026-05-08'
  AND region = 'JP'
GROUP BY customer_id;
```

The engine does not begin by opening every Parquet file under `sales/`.

It starts with planning questions instead:

- What table does `sales` refer to in the current catalog?
- Which snapshot or version of the table is visible to this query?
- Which files belong to that version?
- How is the table partitioned?
- What statistics exist at table, partition, file, or row-group scope?
- Which columns are required by projection and filtering?
- Is the expected result small enough for a broadcast join in a larger query?
- Are constraints or key relationships available that simplify the plan?

Those are all metadata questions.

This is why query planning should be seen as a metadata interpretation phase. SQL text expresses intent, but metadata tells the planner what that intent costs, which objects it applies to, and which parts of the dataset can be ignored safely. The optimizer is not reasoning over raw bytes yet. It is reasoning over descriptions of bytes, files, partitions, schemas, and relationships.

That description layer exists in several places at once: catalog entries, table-format metadata, partition maps, file statistics, and in some systems column-level summaries or constraints. Different engines expose those layers differently, but the pattern is consistent across [DuckDB](https://duckdb.org/), [Apache Spark](https://spark.apache.org/), and [Trino](https://trino.io/): compute quality depends heavily on metadata quality.

## Planner Inputs

It helps to separate the planner's metadata inputs by the decisions they support.

Schemas are the most obvious input. Without schema metadata, the engine does not know the types of expressions, the legality of predicates, or the physical readers required for each file format. Schema also controls coercion, nullability reasoning, and whether a filter can be pushed into a scan without semantic risk.

Statistics are the second major input. Row counts, distinct counts, null fractions, min and max values, histogram-like summaries, and file sizes all help estimate cardinality and cost. A planner does not need exact truth to be useful, but it does need signals strong enough to compare alternatives.

Partition maps and file inventories answer a different question: where could matching data physically live? In a lakehouse table that answer may come from Iceberg manifests, Delta transaction-log state, or a catalog-backed file listing abstraction. In a warehouse it may come from internal storage metadata. Either way, the planner needs a bounded candidate set before it can reason about scan work.

Constraints and lineage-adjacent metadata add further signal. Primary-key and uniqueness constraints may help deduce join cardinality even when they are not fully enforced. Freshness metadata, snapshot timestamps, or provenance fields can also influence which version of a table is eligible for planning in governed environments. These are not always traditional optimizer inputs, but they increasingly shape how platforms choose safe and relevant data before execution starts.

This is a useful systems boundary:

- schema metadata explains what the data means structurally
- location metadata explains where candidate data lives
- statistical metadata estimates how much matching data exists
- constraint and provenance metadata bounds what interpretations are safe

Generic optimizer diagrams often hide this distinction. They show a parser, a logical plan, and a physical plan box. The missing detail is that each transformation depends on metadata that turns a textual query into a bounded execution problem.

## Pruning

Pruning is the clearest example of metadata affecting runtime before any meaningful data scan occurs.

Suppose `sales` is partitioned by `order_date`, and each partition contains multiple Parquet files with min and max statistics on `region` and `order_date`. The query above references one week and one region. A healthy planner should eliminate most of the table in layers.

First comes partition pruning. If the partition map shows daily partitions for April, May, and June, the planner can keep only the partitions for `2026-05-01` through `2026-05-07`. That decision can often be made from table metadata alone without touching any file footer.

Second comes file pruning. Inside those selected partitions, file-level metadata may show that some files only contain `region = 'US'` or date ranges outside the requested window due to late compaction layouts or mixed partition transforms. Those files can be removed from the scan set before task scheduling.

Third comes row-group pruning inside the remaining files. Once the engine reads Parquet footer metadata for the surviving files, row groups whose min and max values cannot satisfy the predicate are skipped.

The key point is that the planner keeps narrowing the candidate set using metadata at progressively finer scopes:

1. catalog and table metadata define the current table version
2. partition metadata limits the candidate partitions
3. file metadata limits the candidate files
4. file-format statistics limit the candidate row groups

This is why file or partition elimination is not the same thing as "scanning less later." It changes the amount of work that is scheduled at all. Fewer files mean fewer object-store requests, fewer tasks, less decompression, lower memory pressure, and smaller intermediate state.

[Apache Spark SQL](https://spark.apache.org/sql/) makes this layering visible in explain plans where partition filters and pushed filters appear separately. [Trino](https://trino.io/) exposes similar behavior through connector-specific predicate pushdown and split generation. [DuckDB](https://duckdb.org/docs/stable/data/parquet/overview.html) often demonstrates the same idea more compactly when querying Parquet directly: it can use file and row-group statistics to avoid reading irrelevant segments even without a large distributed control plane around it.

The behavior differs by engine boundary. DuckDB often plans close to the file format because it is frequently embedded and scans files directly. Spark and Trino more often plan through catalogs, table formats, and distributed split schedulers. But the shared principle is the same: pruning depends on metadata that exists before scan execution.

## Statistics

Pruning reduces the scan set. Statistics shape the rest of the plan.

Consider a join query:

```sql
SELECT o.order_id, c.segment
FROM orders o
JOIN customers c
  ON o.customer_id = c.customer_id
WHERE o.order_date >= DATE '2026-05-01'
  AND c.country_code = 'JP';
```

Even after pruning, the planner still needs to decide join order, join algorithm, and data movement strategy. That requires cardinality estimates.

If metadata suggests that `customers` filtered to `country_code = 'JP'` produces only 50,000 rows while the filtered `orders` relation produces 200 million rows, broadcasting the smaller side may be cheaper than repartitioning both sides. If the statistics instead show that the filtered customer table remains large and highly skewed, the planner may prefer a partitioned hash join or a different join order entirely.

This is where cost-based optimization becomes practical rather than mythical. The optimizer is not reading minds. It is comparing candidate plans against estimated row counts, widths, file sizes, and operator costs derived from metadata.

Three estimates matter especially often:

- cardinality after filters
- selectivity of join predicates
- data size after projection

Bad estimates distort all three. If a planner assumes a predicate is highly selective when it is not, it may choose an overly aggressive broadcast plan. If it underestimates distinct values on a join key, it may place joins in an order that explodes intermediate results. If it lacks reliable null statistics, it may fail to simplify predicates or misjudge aggregation cost.

This is one limit of cost-based optimization that is easy to understate: the "cost-based" part is only as good as the metadata feeding the model. When statistics are absent, stale, or too coarse, the optimizer falls back to heuristics. Heuristics are sometimes reasonable, but they are not evidence.

Engine behavior diverges here.

Spark commonly depends on table and column statistics collected through catalog and table-format integrations, then refines some decisions with adaptive execution once runtime sizes become visible. Trino often relies on connector-provided table statistics, which means planning quality depends partly on how much metadata a connector can surface. DuckDB can often infer useful information from local file metadata quickly, but it still benefits when the surrounding table metadata is explicit rather than reconstructed ad hoc.

Across all three, the pattern is consistent: statistics do not merely tune a finished plan. They decide which plan is considered plausible in the first place.

## Catalogs

Planning starts earlier than statistics. It starts at name resolution.

When a query references `catalog.sales.orders`, the engine must resolve more than a storage path. A catalog or metadata service tells the planner which object exists, what schema version is current, which table format applies, which snapshot is visible, and where deeper planning metadata can be found.

That resolution step is easy to overlook because SQL makes it look cheap. In real systems it is part of the planning path.

[Apache Iceberg](https://iceberg.apache.org/) tables are a good example. A planner typically resolves the table through a catalog, reads the table metadata file, identifies the current snapshot, and only then begins manifest pruning and file selection. [Delta Lake](https://delta.io/) performs the same broad function through transaction-log state and checkpoints. A metastore-like system may provide the entry point even if the authoritative file set lives in the table format metadata rather than the catalog record itself.

This means catalogs participate in planning in at least four ways:

- name resolution and permissions
- schema and table-property lookup
- snapshot or version discovery
- access to deeper metadata structures used for pruning and cost estimation

In distributed engines, catalogs also shape latency and failure domains. If metadata resolution is slow, every query pays that planning overhead. If catalog state is inconsistent across regions or connectors, different engines may produce different candidate file sets for what users think is the same table. If permissions are resolved incorrectly, the planner may not even see partitions or columns that should be eligible.

That operational role is why modern metadata services are not optional decoration. They are planning infrastructure.

## Failure Modes

Metadata-driven planning works well when metadata is current and trustworthy. It degrades quickly when those assumptions break.

Stale statistics are the most familiar problem. A table may have been compacted, repartitioned, or heavily skewed by a recent ingest pattern, while the planner is still using estimates from last week. The query may remain logically correct, but the chosen plan can become much more expensive than necessary.

Incomplete metadata is different from stale metadata. Some tables simply do not expose enough detail. Maybe a connector returns row counts but no column statistics. Maybe file-level statistics exist but partition maps are weak. Maybe the catalog knows partition paths but not the exact live file set for a consistent snapshot. In those cases the optimizer cannot compare plans well because too many inputs are unknown.

Misleading metadata is worse than missing metadata. Corrupt min and max values, overly optimistic null fractions, or invalid uniqueness assumptions can lead the planner to eliminate relevant data or choose a pathological join strategy. Query engines usually guard correctness more carefully than performance, so they prefer not to prune unless metadata is trusted. Even so, degraded metadata quality often forces a defensive fallback to broader scans and simpler heuristics.

Lineage-adjacent metadata matters here too. If a planner cannot tell whether statistics correspond to the current snapshot, or whether a derived table is lagging behind its upstream source, it cannot reason confidently about freshness-sensitive workloads. In a classic dashboard this may only hurt latency. In a production data product or automated decision system it can affect whether the query result should have been used at all.

The practical lesson is direct: metadata quality is part of query-performance engineering. Teams often monitor CPU, memory, and scan volume while treating statistics maintenance or catalog health as background administration. That separation is artificial. If the planning metadata is weak, execution quality follows.

## Adaptive Boundary

Metadata-driven planning is powerful, but it is not the whole story. Many engines also adapt during execution.

Spark's adaptive query execution is a useful reference point. The initial plan is still built from metadata and estimates, but runtime information such as actual shuffle partition sizes can trigger plan revisions. A broadcast join may become viable only after a filter runs. A skewed partition may be split after real sizes are observed rather than inferred.

That does not make metadata less important. It clarifies the boundary.

Metadata-driven planning answers, "What should we schedule given what we know before execution starts?" Runtime adaptation answers, "Now that operators have produced real measurements, which parts of that plan should be revised?"

These phases are complementary.

- metadata reduces the search space before work begins
- runtime adaptation repairs or refines decisions after evidence arrives

Without metadata, the engine schedules too much work and starts from poor assumptions. Without adaptive behavior, the engine may stay trapped in bad early estimates even when runtime signals contradict them. Mature systems need both, but they operate at different times and with different evidence.

This distinction also prevents overclaiming planner intelligence. A query engine is not omniscient because it has a cost model. Before execution, it only knows what the metadata says. If the metadata is weak, the initial plan is necessarily approximate.

## AI Workloads

Classic query planning mostly cares about typed structure, file layout, and statistical summaries. AI workloads need all of that, then push metadata further.

A feature store query still benefits from partition pruning and cost estimation. A retrieval pipeline, however, also needs semantic metadata: embedding model version, chunk provenance, document timestamps, language, access policy, source reliability, and task-specific relevance signals. Those fields are not just descriptive labels for later display. They decide what can be retrieved, filtered, joined, reranked, and trusted.

That is why the boundary of metadata is widening. In relational planning, metadata helps answer questions such as which files to scan and whether a join should broadcast. In AI-native systems, metadata must also answer which chunk belongs to which source document version, whether two vectors were produced by compatible encoders, whether lineage permits this context to be used in a downstream answer, and whether freshness rules make a retrieved record ineligible.

The planning pattern is familiar even though the operators are changing.

- schemas and statistics describe structured tables
- semantic attributes and provenance describe retrieval objects
- catalogs and registries resolve the current logical object set
- planners use those signals to bound work before expensive execution starts

The next step for metadata is therefore not abandoning query planning. It is extending planning inputs beyond classic tables and file statistics into semantic, provenance, and retrieval context that machine-facing systems require.

## Planning Depends on Metadata

Metadata matters to query engines because planning is an information problem before it is a compute problem.

Schemas tell the engine what operations are legal. Partition maps and file inventories bound where matching data can live. Statistics estimate how much data remains after filters and joins. Catalogs resolve the versioned objects those decisions apply to. When those metadata layers are healthy, planners can prune aggressively, choose better join strategies, and schedule less work. When they are weak, stale, or misleading, cost-based optimization becomes guesswork and runtime adaptation has to recover from poor starting assumptions.

That is why metadata should be treated as an execution-planning layer, not only as documentation. The planner consumes metadata first and turns it into a physical strategy before most data bytes are touched.

Part 6 extends that idea into AI systems. Once the workload depends on retrieval, embeddings, provenance, and semantic filtering, typed tables and file statistics are no longer enough. AI-native systems need metadata that captures semantics, lineage, and retrieval context as first-class planning inputs.
