---
date: "2026-08-17T00:00:00+09:00"
title: "Data Integration and Flow"
weight: 3
prev: "/docs/data/architecture/patterns"
next: "/docs/data/architecture/modern-data-architecture"
---

Data integration connects systems so information produced in one boundary becomes useful in another. The movement mechanism determines latency, coupling, consistency, failure behavior, replayability, and who must operate the connection. It is therefore an architectural decision, not merely pipeline implementation.

## Begin with the Boundary

Identify the producer and consumer, the authoritative source, the meaning of the transferred data, and the service each side can promise. Then ask:

- Is the consumer requesting current state, receiving changes, or reconstructing history?
- What latency is valuable rather than merely possible?
- Can the consumer depend on producer availability?
- Are duplicates, reordering, and temporary inconsistency acceptable?
- Must processing be replayable or auditable?
- May data be copied across this security, privacy, residency, or ownership boundary?

## Movement Patterns

### Batch and File Transfer

Batch extracts bounded snapshots or increments on a schedule. Files provide portable, inspectable delivery artifacts and can cross disconnected boundaries.

Batch is useful when minutes or hours of latency are acceptable, volume is high, and reconciliation matters. Its visible completion points simplify reruns and audit. Large windows create freshness gaps and load spikes; poorly defined increments create duplicates or missed records.

### ETL and ELT

**ETL** transforms before loading into the target. It can minimize exposure and enforce a target contract before persistence. **ELT** loads source-shaped data and transforms within a scalable analytical system, preserving flexible reprocessing.

These are placement choices, not opposing eras. A flow may validate and minimize sensitive fields before loading, then perform analytical modeling in the warehouse. Compare where compute scales, where raw data may reside, how logic is tested, and which team owns it.

### APIs

APIs expose bounded domain queries or operations on demand. They preserve a producer-managed interface and avoid unrestricted database access.

They fit interactive lookups and operational integration, but couple the consumer to runtime availability, quotas, and version behavior. Bulk extraction through record-by-record APIs is often inefficient. Design pagination, caching, idempotency, rate limits, and error semantics explicitly.

### Replication and Change Data Capture

Replication maintains a copy for locality, availability, or workload isolation. **CDC** reads committed changes—commonly from a database log—and emits inserts, updates, and deletes downstream.

CDC can lower latency and source load compared with repeated full extracts. It also exposes physical database details, transaction ordering, schema changes, initial snapshots, and delete handling. A CDC record reports a storage change; it is not automatically a stable domain event.

### Messaging

Queues and message brokers decouple producer execution from consumer processing. They support asynchronous work, buffering, retries, and independent scaling.

The design must define acknowledgement, retry, dead-letter handling, idempotency, ordering scope, retention, and backpressure. “Exactly once” claims should be evaluated across the whole side effect, not only the broker transaction.

### Event Streaming

An event stream retains an ordered sequence that multiple consumers can process continuously and, within retention limits, replay. It supports real-time projections, monitoring, integration, and incremental analytics.

Streams add durable history and consumer independence, but require schema compatibility, partitioning, event-time handling, state management, and operational observability. Choose what an event means and whether the log is authoritative, derived, or only a transport.

### Federation and Virtualization

Federation queries data in its owning system rather than persisting a managed copy in the consumer's platform. It can support residency, autonomy, and fast access to current data.

Query-time integration inherits remote latency, availability, concurrency limits, and semantic differences. Pushdown and caching can improve performance but complicate policy and freshness. Federation is most effective when remote systems expose stable schemas, predictable service, and compatible identity and policy.

## Comparing the Choices

| Pattern           | Typical latency         | Coupling                                 | Consistency                   | Replayability                                    | Operational pressure                   |
| ----------------- | ----------------------- | ---------------------------------------- | ----------------------------- | ------------------------------------------------ | -------------------------------------- |
| Batch / files     | Minutes to days         | Low at runtime; contract coupling        | Snapshot or interval-based    | Strong when deliveries are retained              | Scheduling, increments, reconciliation |
| API               | Request-time            | High runtime dependency                  | Current according to producer | Usually low unless calls are logged              | Availability, quotas, versioning       |
| Replication / CDC | Seconds to minutes      | Coupled to source change model           | Eventually consistent copy    | Good if logs and snapshots are retained          | Schema change, ordering, resync        |
| Messaging         | Seconds or less         | Loosely coupled execution                | Usually eventual              | Depends on retention and dead-letter design      | Retries, duplicates, backpressure      |
| Event streaming   | Milliseconds to seconds | Contract coupling; independent consumers | Eventual or stream-defined    | Strong within retained history                   | State, partitions, late data, replay   |
| Federation        | Query-time              | High remote dependency                   | Reads current remote view     | Query reproducibility requires snapshots or logs | Remote performance, policy, failures   |

These are tendencies, not guarantees. A daily API pull behaves like batch; a compacted stream may represent current state; a replicated database can provide strong guarantees within a tightly controlled topology.

## ETL, Events, and CDC Are Different Abstractions

An ETL pipeline says how data is extracted and transformed for a target. CDC says how physical state changes are captured. A domain event says what happened in the business or system. One implementation may convert CDC records into domain events and later transform them into analytical tables, but the contracts and owners differ at each step.

Keeping those abstractions separate prevents downstream consumers from depending unintentionally on source internals.

## Design for Failure and Change

- Give every important flow an owner, schema or contract, freshness expectation, and observable completion or lag signal.
- Preserve correlation and lineage across batch identifiers, event offsets, API requests, and target records.
- Make retries idempotent or make duplicate effects detectable and repairable.
- Define initial load, resynchronization, deletion, late arrival, and schema evolution before production.
- Test failure at ownership boundaries, including a slow consumer, unavailable source, poison message, expired credential, and incompatible change.
- Reconcile derived state against an authoritative source where the risk warrants it.

Implementation belongs to data engineering, but the allowed failure modes and responsibilities belong to architecture.
