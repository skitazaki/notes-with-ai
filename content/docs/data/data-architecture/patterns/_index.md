---
date: "2026-08-17T00:00:00+09:00"
title: "Data Architecture Patterns"
weight: 2
prev: "/docs/data/data-architecture/principles"
next: "/docs/data/data-architecture/integration-and-flow"
---

Data architecture patterns are recurring arrangements of responsibilities, storage, movement, and ownership. They are useful as recognition tools, not complete designs. Real data estates combine patterns, and the same label can describe a storage technology, processing model, integration style, or organizational model.

## Do Not Flatten the Taxonomy

A warehouse, lake, and lakehouse primarily describe analytical storage and processing arrangements. Event-driven and streaming describe interaction and computation. Data Mesh describes an operating model built around domain ownership, data products, a self-service platform, and federated governance. “Centralized” and “federated” describe placement of authority or execution.

These dimensions can coexist. A domain-oriented organization can publish products through a shared lakehouse, distribute changes as events, and serve governed metrics through a [semantic layer](/docs/data/metadata/semantic-layer/).

## Centralized Analytical Architecture

Data from many sources is integrated into a centrally operated warehouse or analytical platform. Shared models and controls support enterprise reporting and cross-domain analysis.

This pattern is useful when consistency, consolidated metrics, and concentrated expertise dominate. It can create a delivery bottleneck, distance modeling from domain context, and make the central platform a large failure and coordination boundary.

## Hub-and-Spoke

A shared hub provides integration, storage, governance, or canonical data, while spokes serve domains, business units, or workloads. The hub can reduce duplicated foundations and support cross-domain views; spokes preserve some local optimization.

The difficult decision is what belongs in the hub. Too much central logic recreates a monolith. Too little leaves inconsistent identity, semantics, and controls. Define whether the hub owns physical data, metadata, exchange, policy, or only shared platform services.

## Shared Data Platform

A platform team provides reusable ingestion, storage, processing, orchestration, catalog, security, quality, and serving capabilities. Producer and consumer teams build on those capabilities rather than each assembling infrastructure.

The platform is a good fit when many teams have recurring needs and self-service can reduce coordination. It fails when “self-service” is only a ticket queue or when the platform forces unlike workloads through one path. Treat platform interfaces as products with users, service expectations, and an adoption strategy.

## Warehouse, Lake, and Lakehouse

- A **warehouse** emphasizes managed analytical tables, query performance, and governed modeling.
- A **lake** emphasizes scalable retention of varied data in object or distributed storage with multiple processing options.
- A **lakehouse** adds table transactions, schema management, and analytical access patterns over lake-style storage.

These approaches can coexist through tiers or workload boundaries. Evaluate table semantics, catalog authority, engine compatibility, workload isolation, governance, operational maturity, and total cost. “Open format” can improve portability without making catalogs, security models, or SQL behavior identical.

## Event-Driven Architecture

Producers publish facts about meaningful state changes, and consumers react without the producer coordinating each action. This enables independent consumers and near-real-time workflows.

The pattern is useful for integration across autonomous systems. It requires durable event contracts, clear semantics, idempotency, correlation, ordering expectations, replay strategy, and end-to-end observability. Events should express domain facts rather than expose a producer's private database log by default.

## Streaming Architecture

Continuous records are processed incrementally rather than waiting for bounded batches. Stateful processors can aggregate windows, join streams, detect patterns, and update serving stores.

Streaming fits low-latency decisions and continuously changing state. Operational complexity includes backpressure, checkpoints, late and out-of-order events, state growth, deployment compatibility, and replay. A streaming transport alone does not create a streaming architecture if all useful work still waits for a nightly job.

## Lambda and Kappa

**Lambda architecture** uses a batch path for complete recomputation and a speed path for low-latency results, merging them at serving time. It addresses the historical tension between completeness and latency, but duplicates logic and operations.

**Kappa architecture** argues for a primary streaming path and reprocessing through replay of the retained log. It can reduce duplicated code when the event history is complete and stream processing supports the required recomputation. Long retention, state migrations, reference data, and corrections remain real constraints.

## Federated Architecture

Data, computation, or authority remains distributed while shared protocols and controls coordinate access. Federation can preserve autonomy, residency, and workload locality. Query federation and organizational federation are related but not identical: one distributes execution; the other distributes decision rights.

Remote availability, performance, identity, semantic alignment, policy evaluation, and responsibility for failures become architectural concerns. Federation works through explicit agreements, not through the absence of central design.

## Domain-Oriented Architecture and Data Mesh

Domain-oriented architecture places responsibility near teams with business and operational context. [Data Mesh](/docs/data/metadata/data-mesh/) makes this a broader socio-technical model through domain ownership, [data products](/docs/data/metadata/data-products/), self-service platform capabilities, and [federated governance](/docs/data/metadata/federated-governance/).

This model can reduce central bottlenecks and improve contextual ownership. It also increases the need for interoperable interfaces, common policy, product discovery, and organizational capability. Renaming datasets “products” or assigning domain labels does not implement the pattern.

## Logical and Physical Centralization

A logically unified experience does not require one physical store. A catalog, semantic layer, access gateway, or federated query surface can present distributed assets coherently. Conversely, placing all files in one bucket does not create shared meaning, governance, or ownership.

Separate these questions:

- Where is data physically stored and processed?
- Where are metadata, identity, policy, and semantics coordinated?
- Who has decision rights and operational responsibility?
- What interface does a consumer experience?

## Comparing Patterns

| Pattern                | Primary strength                            | Primary pressure                                       |
| ---------------------- | ------------------------------------------- | ------------------------------------------------------ |
| Centralized analytical | Consistency and cross-domain analysis       | Central bottlenecks and context loss                   |
| Hub-and-spoke          | Shared foundation with local specialization | Defining and governing the hub boundary                |
| Shared platform        | Reuse and self-service                      | Product discipline and workload diversity              |
| Event-driven           | Loose coupling and timely reaction          | Contracts, delivery semantics, and observability       |
| Streaming              | Low-latency incremental computation         | Stateful continuous operations and replay              |
| Federated              | Autonomy, locality, and residency           | Cross-boundary semantics, policy, and failure handling |
| Domain-oriented        | Contextual ownership and scaling teams      | Interoperability and organizational readiness          |

Select patterns by constraints and quality attributes, then make their combination explicit.
