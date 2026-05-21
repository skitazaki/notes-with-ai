---
title: "Parquet and the Rise of Physical Metadata"
date: "2026-05-21T10:00:00+09:00"
tags: ["Metadata", "Data", "Schema", "Architecture"]
categories: ["Technology", "Data"]
draft: false
---

Part 2 ended at the boundary where schema becomes operational. Once producers and consumers depend on the same structure, metadata is no longer just descriptive. It constrains change.

Large-scale analytical storage adds a different requirement. Correctness is not enough. Engines also need metadata that helps them avoid unnecessary work.

That is where physical metadata enters the picture.

This article extends [Types Become Contracts](/blog/metadata/part2-schema-contracts/) and the series overview in [Metadata Systems - From Column Comments to Distributed Control Planes](/blog/metadata/). The focus here is not Parquet as a brand name or a generic introduction to columnar formats. The practical question is how metadata embedded in a file influences scan cost, pruning, interoperability, and execution shape before most data bytes are even decoded.

## Storage Needs More Than Correctness Metadata

A schema contract can tell a consumer that `created_at` is a timestamp and `country_code` is a two-letter string. That matters for interpretation and compatibility. It does not tell a query engine whether 98 percent of a file can be skipped for a date filter.

That difference is the step from logical metadata to physical metadata.

Logical metadata answers questions such as these:

- What fields exist?
- What type does each field have?
- Which fields are required or optional?
- What meaning or compatibility guarantees do downstream systems rely on?

Physical metadata answers different questions:

- Where in the file is each column stored?
- How many row groups exist?
- What encoding and compression were used?
- What are the min and max values for a column segment?
- Can a filter eliminate a row group before any data pages are read?

CSV and JSON sharpen the contrast. They can describe records, but they give the engine very little structural help once bytes hit storage. A CSV reader typically has to scan linearly, tokenize rows, and interpret values after the fact. JSON adds nested structure but still offers no compact footer that says where a column lives, what its page boundaries are, or whether a whole segment can be skipped for `event_date >= '2026-05-01'`.

[Parquet](https://parquet.apache.org/) was built for that missing layer. It stores data in a columnar layout and pairs the encoded column data with metadata that query engines can inspect quickly. The file does not only hold values. It also carries a plan for how those values can be found, skipped, and decoded.

## File Layout

Parquet file structure is easiest to understand from the end of the file backward.

The important metadata lives in the footer. A reader usually performs a small ranged read near the end of the object, discovers the footer length, and then reads the serialized metadata block. That block contains the schema, row-group inventory, per-column chunk metadata, encodings, compression information, offsets, and statistics.

A compact mental model looks like this:

```text
PAR1
  column data pages
  column data pages
  ...
  row group N column chunks
  serialized footer metadata
footer_length
PAR1
```

The exact wire format is more detailed, but operationally the footer gives the engine an index into the file.

The main structural units are these:

- Row group: a horizontal partition of rows inside one file
- Column chunk: the bytes for one column within one row group
- Page: a smaller unit inside a column chunk, used for data and dictionary storage
- Footer metadata: the file-level directory that describes how all of those pieces fit together

In practice, the footer usually contains at least four categories of information that matter to readers:

- schema metadata for the file
- per-row-group row counts and byte sizes
- per-column-chunk offsets, encodings, codecs, and statistics
- enough structural detail to let the engine plan ranged reads instead of blind full-file scans

That last point is easy to underestimate. In object storage environments, a reader often does not want to download the entire file just to discover whether the query needs 3 percent of it or 90 percent of it. The footer makes a cheap planning phase possible. The engine can issue a small read near the file tail, decode metadata, and then request only the byte ranges that correspond to the selected column chunks. That design fits modern analytical storage well because file metadata can be inspected with far less network and CPU cost than full decoding.

Suppose a file contains columns `order_id`, `customer_id`, `created_at`, `country_code`, and `amount_jpy` for 10 million rows. A writer may divide those rows into five row groups of 2 million rows each. Inside each row group, every column is written separately as its own column chunk. The footer records where each chunk starts, how large it is, what codec was used, and what statistics were collected.

That structure is why Parquet readers do not behave like line-oriented readers. They can decide to read only the `created_at` and `amount_jpy` chunks for a query that never touches `customer_id`. They can also inspect statistics first and conclude that some row groups cannot possibly match the predicate.

Pages make the structure more granular still. A column chunk is not a single undifferentiated blob. It is a sequence of pages, often including an optional dictionary page followed by data pages. That gives writers and readers a useful tradeoff boundary. The footer gets the engine to the right chunk. Page structure governs how values are actually decoded inside that chunk. The distinction matters because Parquet metadata works at several layers at once: file planning, row-group pruning, column projection, and page-level decoding.

## Pruning

The most immediately valuable Parquet metadata is statistics.

At row-group or page scope, writers may record values such as:

- minimum value
- maximum value
- null count
- distinct count in some implementations or adjacent systems

Consider a file with three row groups for `event_date`:

```text
row group 1: min=2026-05-01, max=2026-05-07
row group 2: min=2026-05-08, max=2026-05-14
row group 3: min=2026-05-15, max=2026-05-21
```

Now run this filter:

```sql
SELECT count(*)
FROM events
WHERE event_date >= DATE '2026-05-15';
```

An engine can inspect footer metadata before reading most column data. Row groups 1 and 2 cannot satisfy the predicate, so they are eliminated. Only row group 3 needs to be scanned.

The same pattern applies to numeric ranges:

```text
column: amount_jpy
row group 1: min=100, max=1200
row group 2: min=1300, max=4500
row group 3: min=5000, max=25000
```

For `WHERE amount_jpy > 10000`, the first two groups can be skipped immediately.

This is often described as predicate pushdown, but the useful detail is where the decision happens. The engine is not pushing a predicate into a remote database server. It is using file metadata to decide which physical segments are worth reading.

Null counts matter too. If a query asks for `WHERE coupon_code IS NOT NULL` and a row group has a null count equal to the row-group row count, that segment contributes nothing and can be skipped.

Partition directories often work alongside Parquet metadata, not instead of it. A dataset might be physically laid out under object storage paths such as:

```text
s3://warehouse/events/dt=2026-05-21/part-0001.parquet
```

Directory partitioning can prune whole files from a path filter. Footer statistics then prune further within the surviving files. One is dataset-adjacent metadata. The other is file-embedded metadata. Real engines commonly use both.

The quality of pruning depends on how files were written. If rows are appended in arbitrary order, min and max ranges may overlap heavily and every row group looks potentially relevant. If data is clustered by a frequently filtered column such as date, tenant, or region, the statistics become far more selective. Parquet does not create that value automatically. Writers and table-maintenance workflows have to preserve some amount of locality for the metadata to stay informative.

## Types

Parquet's type system is another place where metadata stops being decorative.

The format distinguishes between physical types and logical types. Physical types describe how values are actually stored. Logical types describe the higher-level meaning a reader should reconstruct.

For example:

- `INT32` may physically store a date as days since the Unix epoch
- `BYTE_ARRAY` may physically store UTF-8 strings
- `INT64` may physically store timestamps with a particular unit
- `FIXED_LEN_BYTE_ARRAY` may physically store decimal values

One concrete mapping is a decimal amount:

```text
logical type: DECIMAL(12,2)
physical type: FIXED_LEN_BYTE_ARRAY(8)
```

Another is a date:

```text
logical type: DATE
physical type: INT32
```

Why does this distinction matter? Because storage efficiency and interoperability pull in different directions.

On the storage side, a small set of physical primitives keeps encoding and vectorized processing practical. On the interoperability side, readers need enough metadata to reconstruct the intended semantics. If a system sees only `INT32`, it cannot know whether the value means a count, a date, or an enum-like code. The logical annotation closes that gap.

This is one reason Parquet metadata matters beyond one engine. A file may be written by Spark, scanned later by DuckDB, read through Arrow libraries, or queried by Trino. Those systems do not share runtime memory structures, but they can converge on the same interpretation if the physical and logical metadata are both preserved clearly enough.

When metadata is ambiguous, portability suffers. Timestamp semantics are a common example. Physical storage alone does not fully answer whether the value should be interpreted as UTC-normalized time, local wall time, or a specific precision boundary. Engines that make slightly different assumptions can all read the file and still disagree subtly about meaning.

## Encodings

Parquet metadata also tells the reader how values were encoded and compressed.

Writers may choose encodings such as dictionary encoding, run-length encoding, or plain encoding depending on data characteristics. Compression codecs such as Snappy, Zstandard, or Gzip may then be applied to column pages.

Those choices directly affect runtime behavior.

Dictionary encoding is a good example. If `country_code` contains a small repeating set of values, storing a compact dictionary plus integer references can shrink storage and improve scan locality. The footer and page metadata tell the reader what encoding is in use so it can decode values correctly and, in some cases, apply filters efficiently against dictionary contents before fully materializing rows.

Compression metadata matters for the same reason. A reader deciding whether to project three columns or thirty is also deciding how many compressed chunks need to be fetched and decompressed. Because Parquet is columnar, compression cost is tied to the selected columns and row groups, not to the entire record structure.

This is one of the reasons CSV and JSON comparisons remain useful. With row-oriented text formats, projection savings are limited because parsing still touches most of the file. With Parquet, column metadata makes selective access a normal execution path rather than a best effort.

## Arrow

Parquet becomes more important when viewed together with [Arrow](https://arrow.apache.org/).

Parquet is a storage format optimized for durable, compact, columnar files. Arrow is an in-memory columnar format optimized for efficient analytical processing and interchange between runtimes. They solve different problems, but they align well because both are built around columnar access and typed arrays.

In a common read path, an engine inspects Parquet metadata, selects the needed row groups and columns, decodes the relevant pages, and materializes them into Arrow-like column vectors or equivalent internal buffers. That handoff is not accidental. Parquet metadata helps the engine avoid decoding data that will never be needed, while Arrow-compatible vector layouts let the engine process the surviving data in batches.

This is where physical metadata becomes execution infrastructure.

If a query touches only `created_at`, `country_code`, and `amount_jpy`, the engine can skip unrelated columns at the file level. If statistics show that only two row groups match the predicate, it can skip the others. The remaining pages are decoded into contiguous vectors that fit vectorized operators such as filter, aggregate, and hash probe more naturally than row-by-row interpretation.

The result is not just lower I/O. It is a different execution shape. Metadata determines what enters the vectorized path at all.

Consider a concrete analytical query:

```sql
SELECT country_code, sum(amount_jpy)
FROM orders
WHERE created_at >= TIMESTAMP '2026-05-01 00:00:00'
  AND created_at < TIMESTAMP '2026-06-01 00:00:00'
GROUP BY country_code;
```

In a reasonably organized Parquet dataset, the engine can often follow a staged decision process:

1. Use partition metadata, if present, to eliminate files outside the month.
2. Read Parquet footers for the surviving files.
3. Use row-group statistics on `created_at` to skip groups that fall entirely outside the range.
4. Project only `created_at`, `country_code`, and `amount_jpy` instead of the full table schema.
5. Decode the selected pages into column vectors and run filter plus aggregation operators over those vectors.

Most of the important work happens before full value materialization. That is the central systems point. Metadata is not merely helping documentation or interoperability here. It is deciding which bytes become computation at all.

This also clarifies why Parquet metadata is not the same thing as a secondary index in an OLTP system. The engine is still scanning selected file segments, not performing point lookups against a mutable index tree. But for analytical workloads, that combination of projection, pruning, and batched decoding is often exactly the right compromise between write simplicity and read efficiency.

## Tradeoffs

Parquet metadata is powerful, but it is not magical.

The tradeoffs fall into two broad categories. Some are about semantic boundaries: what the file format can describe reliably, and what has to live in higher-level metadata systems. Others are about execution quality: how well the metadata supports pruning, planning, and portable performance.

### Semantic Boundaries

This is also the point where Parquet's limits become visible.

Teams often want a column to carry more than type information. They want a human-readable description such as "gross order amount in yen after discounts" or "customer signup timestamp recorded in Tokyo local time." Those are real metadata needs because they affect interpretation, not just documentation quality.

Parquet can carry some schema meaning, but it is not a general-purpose field documentation format. In the portable core format, a column has a name, physical type information, repetition rules, and optional logical type annotations. What it does not provide as a strong, standard cross-engine feature is a first-class per-column description field equivalent to a database column comment.

That distinction matters operationally. Some engines and libraries can attach custom metadata when writing files, and file-level key-value metadata exists. Certain ecosystems can also preserve richer field annotations through adjacent schema layers, such as an embedded Arrow schema or external table metadata in a catalog or lakehouse format. But those paths are not the same as saying that raw Parquet itself is a reliable, universal home for portable column descriptions.

So if the question is "can Parquet carry the description of a column?" the practical answer is: not in a standard way that every engine will interpret as an official column comment. If a description must survive across tools, review processes, and data products, it is usually safer to keep it in the table schema, catalog, registry, or another metadata layer designed for semantic documentation.

Timezone handling has a similar boundary.

Parquet can represent timestamp intent better than a bare string or integer, but it still does not solve every timezone problem. In modern Parquet logical types, timestamp metadata can express the time unit and whether the value is adjusted to UTC. That helps readers distinguish between an instant-like timestamp and a local timestamp interpretation.

What Parquet does not generally give you is a named timezone such as `Asia/Tokyo` stored as a standard logical-type parameter for the column. In other words, Parquet can help say "this timestamp is normalized to UTC" versus "this timestamp is not adjusted to UTC," but it is not the universal place to encode the business rule that a source system uses Japan Standard Time or America/Los_Angeles for interpretation.

That leaves teams with a practical pattern:

- use Parquet logical timestamp annotations for unit and UTC-adjustment semantics
- store named timezone rules in adjacent metadata or in the data contract
- if the source timezone is analytically important per row, store it explicitly as data rather than assuming readers will recover it from file metadata

This is consistent with the broader pattern in the series. Physical metadata is excellent at helping engines find, prune, and decode data. It is weaker as a complete carrier of business semantics. Once teams need rich descriptions, ownership context, units, or explicit timezone conventions, they usually have to combine Parquet with higher-level metadata systems rather than relying on the file format alone.

### Execution Quality

The first operational tradeoff is statistics quality. Pruning works only if the collected metadata is present and useful. If writers omit statistics, truncate them, or generate row groups that mix values too broadly, filters become less selective. A file can still be valid Parquet while being a poor pruning target.

The second tradeoff is file and row-group sizing. Very small files increase planning overhead and object-store request cost. Very large row groups can weaken selectivity and force heavier reads for targeted predicates. There is no single perfect size because the right choice depends on workload shape, object storage behavior, and downstream engine expectations.

The third tradeoff is portability versus engine-specific optimization. Parquet is intentionally interoperable, but not every optimization is equally portable. Some engines rely heavily on certain statistics, page indexes, or writer behaviors. Others are more conservative. A dataset tuned for one engine can remain readable everywhere while delivering uneven performance elsewhere.

There is also a semantic risk hidden inside physically valid storage. A column can be well-encoded and richly annotated yet still change meaning in ways that confuse downstream readers. Logical metadata helps, but it does not eliminate governance or migration discipline. Physical efficiency does not replace semantic correctness.

There is also a subtle failure mode around stale assumptions. Engineers often treat Parquet as inherently fast, then stop inspecting how files are actually written. But scan behavior is a property of the concrete metadata in the produced files, not the file extension alone. Bad sorting, broad row-group ranges, inconsistent logical annotations, or unnecessary column duplication can all erode the benefits people assume they are getting.

## Beyond One File

At this point, metadata is doing more than describing fields.

The footer tells readers how a file is organized. Row-group and column-chunk statistics decide whether segments can be skipped. Type annotations preserve meaning across engines. Encoding and compression metadata shape the cost of decoding. Arrow-aligned read paths turn those decisions into vectorized execution.

That is a major shift from Part 2. There, metadata coordinated producers and consumers around correctness. Here, metadata also controls how much compute is required to answer a query.

But Parquet still keeps the metadata scope bounded to a file and to nearby storage layout such as partition directories. Once a dataset spans thousands of files, the next problem appears. Engines need metadata that can reason across file sets, snapshots, partition evolution, and concurrent change.

That is the handoff to Part 4.

Once metadata lives across many files, manifests, and snapshots, it stops being only a file index. It becomes a distributed coordination layer for the dataset itself.
