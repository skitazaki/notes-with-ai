---
date: "2026-08-17T00:00:00+09:00"
title: "Data Architecture Principles"
weight: 1
prev: "/docs/data/architecture"
next: "/docs/data/architecture/patterns"
---

Data architecture principles are durable criteria for making decisions across changing technologies. They do not select a product or produce one ideal topology. They help teams expose trade-offs, keep local choices compatible, and recognize when an architecture no longer fits its workload or organization.

## Separate Concerns, but Preserve the Flow

Separate operational transactions, analytical processing, serving, metadata, and control when they have different change rates or reliability needs. Separation reduces interference: a month-end analytical query should not exhaust the database serving customer checkouts.

The interfaces between concerns still form one end-to-end service. A reliable warehouse that receives stale data is not a reliable analytical product. Evaluate latency, quality, lineage, and failure across the complete producer-to-consumer path.

## Use Explicit, Evolvable Interfaces

Tables, files, APIs, events, and metrics are interfaces. Give important interfaces owners, documented meaning, compatibility rules, quality expectations, and change processes. A field added to a source table may be harmless locally but break a positional file consumer; an event renamed without versioning can strand independent consumers.

[Data Products and Contracts](/docs/data/metadata/data-products/) explains how ownership and contracts make these boundaries consumable. Explicit does not mean frozen: additive change, versioning, deprecation windows, and consumer telemetry enable safe evolution.

## Prefer Loose Coupling and Interoperability

Consumers should depend on a stable interface rather than a producer's internal schema or deployment timing. An order service can publish a documented `OrderConfirmed` event instead of letting many consumers query its private transactional tables.

Loose coupling shifts work rather than eliminating it. Teams must operate schemas, identities, delivery guarantees, and discovery. Interoperability also extends beyond file formats: shared semantics, metadata, policy, and identity determine whether two compatible engines can actually exchange useful data.

## Place Computation Deliberately

Push filtering toward a source when it reduces unnecessary movement without overloading the source or leaking domain logic. Transform in a shared analytical system when reuse and common definitions matter. Compute at query time when freshness or data residency outweighs the cost of a remote dependency.

The question is not simply ETL versus ELT. It is where logic can be governed, tested, scaled, and owned with the fewest harmful dependencies.

## Minimize Unnecessary Data Movement

Every copy creates synchronization, retention, deletion, access-control, cost, and lineage obligations. Prefer projection, filtering, aggregation, remote query, or a stable domain interface when they satisfy the requirement.

Movement is sometimes the correct isolation boundary. A replicated analytical copy can protect an operational database and preserve history. The principle is to justify each copy and manage its lifecycle—not to pursue “zero copy” as an absolute.

## Design for Reliability and Replay

Define what happens when a producer, network, processor, or consumer fails. Batch flows need idempotent reruns and reconciliation. Streams need decisions about ordering, duplicates, checkpoints, state, retention, and late events. APIs need timeouts, backpressure, and bounded retries.

Keep enough source evidence or immutable history to reproduce critical results where the use case requires it. Replay without versioned code, schemas, and reference data is not reproducibility.

## Embed Security, Privacy, and Governance

Apply classification, minimization, identity, authorization, retention, and audit at the boundaries where data is collected, copied, transformed, and served. Central policy with no enforcement point is aspirational; controls embedded in only one storage layer miss APIs, exports, caches, and derived data.

Use [Metadata](/docs/data/metadata/) to connect policies with assets, lineage, ownership, and runtime evidence. Use [Data Privacy](/docs/data/privacy/) to reason about purpose and people, not only technical access.

## Make Ownership Match Control

State accountability and responsibility separately. **Accountability** means being answerable for the outcome and having authority to make or approve the final decision. It should resolve to one clearly identified role or governing body for each outcome. **Responsibility** means performing the work needed to achieve that outcome; it may be distributed across several teams. Naming an “owner” without stating which of these obligations it carries leaves the operating model ambiguous.

Accountability must match control. An accountable owner needs the authority and capability to change the system, accept risk, prioritize remediation, and resolve conflicts within the stated boundary. Assigning a domain team accountability for data while a central queue controls every schema, pipeline, and access decision makes that accountability ineffective. Giving teams autonomy without shared interfaces and governance produces fragmentation.

For every material data asset, interface, and architectural decision, document the accountable role, the responsible roles, the decision rights, and the escalation path. Make the responsibilities of source owners, platform operators, product owners, governance authorities, and consumers explicit, including where responsibilities are shared or handed off. [Ownership Boundaries](/docs/arch/ownership-boundaries/) provides a broader architectural lens.

## Design for Scale and Evolution

Scale includes volume, velocity, consumers, domains, jurisdictions, and rate of change. Partitioning and distributed processing address only some of it. Standardized self-service capabilities may be the better response to organizational scale; stable contracts may be the better response to consumer scale.

Prefer reversible decisions when uncertainty is high. Encapsulate technology-specific behavior behind interfaces, record consequential choices, and use migration paths rather than assuming a platform will never change.

## Treat Principles as Trade-offs

Principles can conflict. Minimizing movement may reduce isolation. Strong consistency may reduce availability or increase latency. Central standards may improve interoperability while slowing domain change. The architecture should state which quality attributes matter, which constraints are real, and why one compromise is acceptable.

A practical decision record includes the context, options, decision, consequences, owner, and signals that would trigger reconsideration. [Decision Frameworks](/docs/arch/decision-frameworks/) explains how to keep that reasoning visible.

## A Short Review Checklist

- Are sources of record and consumers identified?
- Are interfaces, semantics, compatibility, and owners explicit?
- Is every movement or copy justified?
- Are failure, reconciliation, replay, and observability designed end to end?
- Are security, privacy, quality, and governance attached to enforceable boundaries?
- Is one role or governing body explicitly accountable for each material outcome?
- Are the responsible roles, their work, and their handoffs explicit?
- Does the accountable role have the authority and capability to control the outcome?
- Which trade-offs were accepted, and what would cause the decision to change?
