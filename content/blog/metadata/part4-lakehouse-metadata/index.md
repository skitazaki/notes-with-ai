---
title: "Metadata at Lakehouse Scale"
date: "2026-05-21T12:00:00+09:00"
tags: ["Metadata", "Data", "Architecture", "Lakehouse"]
categories: ["Technology", "Data"]
draft: false
---

Part 3 ended at the point where metadata outgrew a single file.

A Parquet footer can tell a reader how one object is laid out, what statistics exist for its row groups, and which column chunks are worth reading. That is powerful, but only within the boundary of that file. Modern analytical datasets are rarely one file. They are usually thousands of Parquet objects in object storage, written over time by independent jobs, queried by multiple engines, and updated under real concurrency.

That is where metadata becomes a dataset-wide coordination layer.

This article extends [Parquet and the Rise of Physical Metadata](/blog/metadata/part3-parquet-physical-metadata/) and the series overview in [Metadata Systems - From Column Comments to Distributed Control Planes](/blog/metadata/). The practical question is not how one file can be scanned efficiently. It is how a table spread across many files can change safely while still giving engines a stable, efficient view of the data.

## File Metadata Is Not Table Metadata

Part 3 focused on file metadata.

File metadata answers questions such as these:

- What schema is embedded in this file?
- What row groups and column chunks exist?
- What min and max statistics are available?
- Which byte ranges need to be fetched to decode selected columns?

Those are local questions. They help with scan planning inside one object.

Lakehouse systems need a second layer that answers table questions instead:

- Which files currently belong to the table?
- Which snapshot of the table should a query read?
- Which schema and partition spec are current?
- What changed between two commits?
- How do two writers avoid publishing conflicting table state?

That distinction matters because object storage does not natively provide table semantics. An object store can keep blobs durably and serve ranged reads well, but it does not tell an engine which 14,000 Parquet files are the consistent current version of `orders`, nor does it provide an atomic table update primitive in the way a traditional database catalog does.

Without a higher metadata layer, engines often fall back to expensive and fragile patterns:

- recursively listing directories to discover files
- inferring partitions from path names alone
- assuming that all visible files are part of the latest table state
- relying on ad hoc conventions to detect in-progress or obsolete writes

Those patterns break down under scale. Listing large prefixes is expensive. Concurrent writers can race. Partial rewrites can expose mixed table state. Schema changes become hard to reason about because there is no authoritative versioned table definition.

Open table formats such as [Apache Iceberg](https://iceberg.apache.org/) and [Delta Lake](https://delta.io/) exist to solve that coordination problem. They treat the table as a versioned metadata structure whose state points to data files, rather than treating a directory full of files as the table itself.

## Object Storage Changes The Coordination Problem

It is useful to separate why Parquet became popular from why lakehouse metadata became necessary.

Parquet solved efficient file layout for analytical scans. Object storage solved cheap, durable, scalable storage. Neither by itself solved table coordination.

Suppose a daily append pipeline writes these objects:

```text
s3://warehouse/orders/dt=2026-05-19/part-0001.parquet
s3://warehouse/orders/dt=2026-05-19/part-0002.parquet
s3://warehouse/orders/dt=2026-05-20/part-0001.parquet
...
```

If the table is append-only and a single engine reads it casually, directory discovery may appear acceptable for a while.

Pressure arrives from four directions.

First, file counts grow. A query should not have to list and inspect every object under a large prefix just to discover which files are live.

Second, updates and deletes appear. Analytical tables are no longer only append logs. Teams rewrite partitions, compact files, apply GDPR deletes, merge CDC streams, and backfill historical slices.

Third, many engines read the same table. Spark, Trino, Flink, DuckDB, and custom services need a shared definition of current table state even though they do not share runtime memory.

Fourth, multiple writers show up. A batch compaction job, a streaming ingest job, and a backfill process may all try to publish changes around the same time.

At that point, the real problem is not file encoding. It is distributed coordination over table state.

The lakehouse answer is to make metadata authoritative. Queries resolve a table version first, then derive the relevant file set from that version. Compute follows metadata, not the other way around.

## Iceberg

[Apache Iceberg](https://iceberg.apache.org/) models a table as a hierarchy of metadata files, snapshots, manifest lists, and manifests.

The important idea is not the exact serialization format. It is the separation of concerns.

- Table metadata files describe table-level state such as the current snapshot, schema versions, partition specs, sort orders, and table properties.
- A snapshot represents one committed version of the table.
- A manifest list records which manifests belong to that snapshot.
- Each manifest records a set of data files and metadata about those files, such as partition values, statistics, sequence numbers, and status.

That structure gives Iceberg a scalable answer to a simple question: which files are in the table right now?

The answer is not "whatever files are present under this directory." It is "the files reachable from the current snapshot through its manifest list and manifests."

### Flow

A simplified Iceberg read flow looks like this in prose.

1. The engine asks a catalog for the current table metadata location.
2. It reads the current table metadata file and learns the active snapshot ID.
3. It loads the manifest list for that snapshot.
4. It reads only the manifests that may satisfy the query predicate.
5. From those manifests, it derives the exact data files that must be scanned.
6. Only then does it begin planning Parquet or ORC reads against the selected files.

That is already a major improvement over directory listing. The engine does not need to recursively crawl object storage to reconstruct table membership. It reads a compact metadata path that already describes the table version.

Manifests also reduce coordination cost at query time. Instead of opening every file footer in a large dataset just to decide relevance, the engine can often use manifest-level partition information and file statistics first. If a query filters on `event_date = '2026-05-20'`, a large fraction of manifests and data files can be eliminated before any Parquet footer reads occur.

This is the key distinction:

- Parquet metadata helps prune within a file.
- Iceberg metadata helps prune across the table before many files are touched at all.

### Snapshots

Snapshots are the unit of consistent table state.

When a writer appends new data, rewrites a set of files, or applies a delete, it does not mutate the visible table in place one file at a time. It prepares new metadata that describes the next snapshot, then commits that snapshot atomically through the catalog mechanism.

That gives readers a stable view. A query starting on snapshot `N` keeps reading that snapshot even if snapshot `N+1` is committed a moment later. This is one reason lakehouse tables can offer repeatable analytical reads without relying on database page latches or storage-engine internals.

Snapshots also make table history explicit. Engines and operators can ask questions such as these:

- What files were added by the last commit?
- Which snapshot introduced a schema change?
- Can a table be rolled back to an earlier consistent state?

Those are metadata questions, not file-format questions.

## Delta Lake

[Delta Lake](https://delta.io/) reaches a similar goal through a different metadata model centered on a transaction log.

Instead of representing table state primarily through manifest trees, Delta records table changes as an ordered log under `_delta_log`. JSON commit files and periodic checkpoints capture actions such as adding files, removing files, updating table metadata, and changing protocol versions.

Conceptually, the current table state is derived by replaying the log up to a version, then consulting checkpoints so engines do not need to reprocess the entire history every time.

The central idea is straightforward: the table is defined by an ordered history of metadata actions, not by the raw directory contents.

### Commit Example

A simplified append in Delta can be pictured like this.

The writer produces new Parquet data files first. It does not make them visible as table state merely by uploading them.

Then it attempts to commit a new log version containing actions similar to these:

```json
{
  "add": {
    "path": "part-00017-...snappy.parquet",
    "partitionValues": { "dt": "2026-05-20" },
    "size": 13428192,
    "stats": "{\"numRecords\":500000,\"minValues\":{...},\"maxValues\":{...}}"
  }
}
```

If that commit succeeds, the file becomes part of the next table version. If it fails due to a conflicting concurrent update, the writer must reevaluate against the new latest version.

That is why the log matters. Visibility is controlled by the metadata commit, not by the existence of a Parquet file in storage.

### Concurrency

Delta Lake is commonly described as using optimistic concurrency control. The useful operational meaning is this: writers assume conflicts are relatively infrequent, proceed without holding long exclusive locks over the entire write path, and validate at commit time whether the table changed in a way that invalidates their assumptions.

Consider two jobs:

- Job A compacts yesterday's small files into larger files.
- Job B appends late-arriving records into the same table.

Both may start from table version 120. If Job A tries to commit version 121 after Job B has already committed a change that overlaps the same logical scope, Job A may need to retry or fail, depending on the conflict semantics.

That pattern is familiar from distributed systems more broadly. The important point is that metadata is where the concurrency check lives. The storage layer is holding immutable data files; the log is coordinating which file set constitutes the table.

Checkpointing exists because log growth would otherwise become its own scaling problem. A mature table may have thousands of commits. Periodic checkpoints materialize table state so new readers can bootstrap from a recent compact representation plus a smaller suffix of log entries.

## Hive Metastore

[Apache Hive](https://hive.apache.org/) and the Hive Metastore remain important reference points because they illustrate what older metadata patterns did well and where they start to strain.

Hive Metastore provided a central catalog for tables, schemas, partitions, and storage locations. That was a major step forward compared with each engine inventing its own unmanaged path conventions.

The limitation is not that Hive Metastore was useless. The limitation is that it was designed around a different pressure profile.

In classic external-table usage, partition directories might be registered in the metastore while the actual file inventory still lives implicitly in storage. Under modern workload pressure, that leaves several gaps:

- the table catalog may know partition paths but not the full authoritative file set for a snapshot
- updates and deletes often rely on rewriting paths in ways that are not naturally transactional at table scale
- partition counts can become extremely large and expensive to manage
- engines may still need heavy listing behavior below each partition
- schema and partition evolution are more awkward than in newer open table formats

This is why Hive Metastore is best seen here as a contrast case. It centralizes some metadata, but it does not by itself provide the richer snapshot-oriented coordination model that Iceberg and Delta need for modern concurrent lakehouse workloads.

Many production deployments still use a metastore-like service or a modern catalog API as an entry point. The difference is what the catalog points to. In a lakehouse design, the catalog resolves a versioned table metadata structure rather than standing in for the complete coordination logic by itself.

## Evolution

Once metadata becomes the table control plane, evolution rules become explicit operational concerns.

Schema evolution is the most obvious case. Adding a column is not just a parser change. The table metadata must record the new schema version, preserve field identity or evolution semantics correctly, and let readers reconcile old files with new ones.

This is one reason Iceberg's field IDs matter operationally. A rename should not be interpreted as dropping one field and adding a different field when the intent is only to relabel the same logical column. Stable field identity helps engines and maintenance jobs reason about evolution more safely than name matching alone.

Partition evolution is just as important. Real tables outgrow their initial partition design. A dataset that began partitioned by day may later need month-level partitioning, bucket transforms, or hidden partition transforms on timestamp columns.

Older layouts often treat the partition path as the definition. That makes change painful because the storage directory shape becomes part of the contract. Modern table formats decouple the logical partition spec from the raw directory naming enough to let the table evolve while remaining queryable.

Atomic table state changes are the other half of the story.

If a maintenance job rewrites 800 small files into 20 larger files, readers should not observe a half-finished mix where some old files are removed and only some replacements are visible. The whole change needs to appear as one metadata transition from one snapshot or log version to the next.

That is the fundamental distributed-systems move in lakehouse metadata: immutable data files plus atomic publication of table state.

## Operations

The clean metadata models are necessary, but they do not remove operational pressure. They mostly make that pressure legible.

Small files are the most familiar example. A table with hundreds of thousands of tiny objects creates extra request overhead, bloats manifests or logs, and reduces scan efficiency. Compaction is therefore not just a storage cleanup task. It is metadata maintenance as well. The file set becomes more manageable for both readers and the table metadata layer.

Commit contention is another common issue. If many independent jobs target the same hot table, optimistic concurrency can degrade into frequent retries. The system remains correct, but throughput and latency suffer. This is often a workload-design problem as much as a format problem: too many writers are attempting to publish overlapping table state too often.

Metadata bloat is a quieter but important risk. Snapshots accumulate. Manifests multiply. Transaction logs grow. Checkpoints help, and snapshot expiration or manifest compaction helps, but the table metadata path needs routine maintenance just like the data path does.

Catalog dependencies matter too. A table format may be open, but queries still depend on a functioning catalog resolution path, correct permissions, and consistent metadata locations. If the catalog is unavailable, misconfigured, or stale, data files sitting safely in storage do not automatically become a usable table.

This is one reason practitioners should stop talking about metadata as though it were only descriptive overhead. At lakehouse scale, metadata services are part of the serving path.

## Planning

The most important systems consequence is what happens before compute starts.

Query engines do not begin by downloading every file under a prefix and hoping to optimize later. In a healthy lakehouse design, they reason over metadata in layers.

An engine may follow a sequence like this:

1. Resolve the table in a catalog.
2. Load the current snapshot or log-derived table version.
3. Use manifest, log, partition, or checkpoint metadata to eliminate irrelevant files.
4. Read file-level metadata such as Parquet statistics for the remaining candidates.
5. Only then schedule scan and compute tasks.

That sequence explains why snapshots and manifests reduce expensive listing and coordination work. They give the engine a compact authoritative summary of table membership and change history, so the planning phase can stay metadata-driven instead of storage-crawl-driven.

It also clarifies the boundary between file metadata and table metadata.

File metadata says, "inside this file, these row groups and column chunks exist, and these statistics describe them."

Table metadata says, "for this consistent version of the table, these files are live, this schema applies, this partition spec is active, and this change history produced the current state."

Without the first layer, scans are wasteful. Without the second layer, the table itself is unstable.

That is why open table formats turned metadata into a distributed systems concern. Once a table spans many immutable files on object storage, correctness and efficiency both depend on authoritative metadata transitions that multiple engines can trust.

Part 5 picks up from there.

Once the catalog, snapshot, and file set are resolved, query engines still have to decide what computation should run at all. That next step depends on metadata again: statistics, pruning rules, and planning inputs that shape execution before the first full scan begins.
