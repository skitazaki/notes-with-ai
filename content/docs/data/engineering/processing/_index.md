---
date: "2026-08-17T09:00:00+09:00"
title: "Data Processing"
weight: 2
prev: "/docs/data/engineering/ingestion"
next: "/docs/data/engineering/orchestration"
---

Data Processing transforms source or intermediate data into datasets that applications, analytics, and AI systems can use. Processing may filter records, join related entities, aggregate measures, enrich values from reference data, reshape schemas, or validate assumptions.

```mermaid
flowchart LR
  Ingestion --> Processing --> Delivery
```

This simple relationship describes responsibility, not a mandatory physical layout. Processing may occur before or after durable storage, in a database, in a distributed compute system, or continuously as events arrive.

## Transformation Operations

Common processing work includes:

- **Filtering** records that are outside the intended scope
- **Projection and reshaping** to select, rename, nest, or normalize fields
- **Joins** to combine records using shared keys or time relationships
- **Aggregation** to calculate measures at a chosen grain
- **Enrichment** to attach classifications, reference values, or derived attributes
- **Validation** to test structural and domain expectations before publishing output

Each operation should make its input assumptions and output grain explicit. A technically correct join can still produce misleading results when keys are non-unique or effective dates are ignored.

## ETL and ELT

**Extract, Transform, Load (ETL)** performs substantial transformation before data reaches the target serving system. It can protect the target from unsuitable inputs and centralize processing outside it.

**Extract, Load, Transform (ELT)** lands source data before transforming it in the target platform. It can preserve replayable inputs and use the target system's compute and governance capabilities.

The labels describe where transformation occurs, not the quality of the design. Many systems use both: light validation and protection before loading, followed by richer transformations after durable landing.

## Batch Processing

Batch processing operates on bounded input, such as a file, table snapshot, or time interval. It fits periodic reporting, large recomputations, reconciliation, and backfills.

Important concerns include:

- defining complete and repeatable input boundaries
- partitioning work so independent units can run in parallel
- making output replacement or merging idempotent
- isolating backfills from current production runs
- controlling resource use and cost for large recomputations

Batch output should identify which input interval and code version produced it. Without that context, recovery becomes guesswork.

## Stream Processing

Stream processing operates on continuous or near-continuous events. Results may update per event or over windows of event time.

Stream processors must manage:

- **Event time and processing time**, which answer different temporal questions
- **Windows**, which bound aggregation over an otherwise unbounded stream
- **State**, such as running counts, joins, or deduplication records
- **Checkpoints**, which make state recoverable after failure
- **Late events**, which may require corrections to previously emitted results
- **Replay**, which reconstructs state or results from retained events

Continuous processing does not guarantee immediate or final truth. Watermarks and lateness policies express when a result is considered sufficiently complete and how later corrections are handled.

## Distributed Processing Fundamentals

Large workloads are divided across workers, which introduces coordination costs as well as capacity.

**Partitioning** assigns records to units of parallel work. A balanced partitioning key improves throughput; skew can leave one worker overloaded while others are idle.

**Parallelism** increases concurrent work but is bounded by input layout, shared services, coordination overhead, and available resources.

**Shuffle** redistributes records between workers for operations such as joins or groupings. It is often one of the most expensive parts of a distributed job because it uses network, disk, serialization, and synchronization.

**State** must be partitioned, persisted, and recovered consistently. Checkpoints reduce recovery time, while replay reconstructs state from retained inputs when necessary.

**Fault tolerance** defines what happens when a task, worker, or dependency fails. Retrying a partition is safe only if its reads and writes have well-defined semantics.

Spark, Flink, SQL engines, and transformation frameworks such as dbt illustrate different processing environments. They should be selected according to workload semantics and operational constraints, not treated as definitions of processing itself.

## Processing Semantics and Architecture

Processing semantics describe the behavior a computation requires: bounded or unbounded input, ordering scope, state, latency, correction, consistency, and replay. Architectural choices determine where and how those requirements are implemented.

For example, a rolling total based on event time needs keyed state and a late-event policy regardless of whether it runs on a managed stream service or an open-source engine. A daily recomputation needs stable input boundaries and idempotent publication regardless of whether storage is called a warehouse or lakehouse.

Architecture describes the system structure and major design choices. Engineering makes the processing behavior reliable within that structure.

## Producing Trustworthy Outputs

Validation inside a processing job implements defined expectations, but it does not by itself define whether data is fit for every intended use. See [Data Management](/docs/data/management/) and [Data Quality Dimensions](/docs/data/management/data-quality-dimensions/) for the broader quality discipline.

Processing also depends on [Metadata](/docs/data/metadata/) for schemas, lineage, ownership, definitions, and impact analysis. [Data Orchestration](../orchestration/) coordinates when processing runs and how dependencies and failures are handled; [Data Observability](../observability/) reveals how processing behaves in production.
