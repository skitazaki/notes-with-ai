---
date: "2026-08-13T00:00:00+09:00"
title: "Data Exchange Mechanisms"
weight: 1
prev: "/docs/data/sharing"
next: "/docs/data/sharing/data-marketplaces"
---

Data exchange mechanisms are the technical means by which a sharing relationship delivers data, exposes a query surface, or permits computation against an asset. They implement part of [Data Sharing](/docs/data/sharing/), but they do not by themselves define the complete producer-consumer relationship.

A mechanism can move a copy, expose live state, deliver changes, or execute a request near the data. The right choice depends on freshness, scale, sensitivity, interoperability, cost, revocation, and the degree of runtime dependency that participants can accept.

## Exchange Is Not the Whole Share

An exchange mechanism belongs primarily to the data plane. A governed share also needs a control plane for discovery, identity, entitlement, policy, contracts, lineage, and usage evidence.

This distinction prevents a common architectural mistake: selecting a transport and assuming the sharing problem is solved. A file can arrive without an owner or license. An API can authenticate a caller without preserving the purpose for which data may be used. A live table share can avoid a managed copy while still leaving semantic and contractual questions unresolved.

## Mechanism Families

| Family                               | Primary behavior                                 | Main strength                                    | Main tradeoff                                       |
| ------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | --------------------------------------------------- |
| Batch and file delivery              | Publishes periodic files or snapshots            | Simple, portable, and easy to reconcile          | Copies drift and are difficult to revoke            |
| API access                           | Returns bounded data or operations on request    | Domain-oriented interface and selective exposure | Runtime coupling and request-scale limits           |
| Events and streams                   | Delivers changes continuously                    | Low-latency reaction to state changes            | Ordering, replay, and contract complexity           |
| Replication                          | Maintains a managed consumer-side copy           | Local performance and workload isolation         | Synchronization, residency, and lifecycle cost      |
| Live table or warehouse sharing      | Exposes provider-managed analytical objects      | Fresh access without export pipelines            | Platform compatibility and runtime dependency       |
| Object-storage and open-table access | Grants access to data objects and table metadata | Large-scale analytical access across engines     | Storage access alone does not supply governance     |
| Query federation                     | Executes queries across remote systems           | Data can remain under local control              | Performance, availability, and semantic variability |

These families can coexist. A product may publish a daily snapshot for audit, a stream for operational change, and an API for selective lookup. The mechanisms should represent different consumer needs rather than accidental duplication.

## Copy, No-Copy, and Zero-Copy

Copy-based exchange creates an independently stored representation for the consumer. This can improve resilience, local performance, and engine freedom, but it creates obligations for synchronization, deletion, retention, provenance, and correction.

No-copy or live-sharing patterns leave the authoritative object under provider control and give the consumer a remote query or storage access path. Revoking credentials is usually easier than recalling a file, and consumers can see provider-managed updates. However, availability, performance, and policy enforcement remain coupled to the provider or intermediary.

“Zero-copy” should be interpreted narrowly. It generally means the sharing service does not create and manage another full dataset copy. Clients may still transfer bytes, cache results, materialize derivatives, or export data after access is granted.

## Open Protocols, Formats, and Implementations

An open table format defines how table state and files are represented. A catalog protocol defines how clients discover and update table metadata. A sharing protocol defines how a provider grants a recipient access to shared assets. A vendor implementation may support one or more of these layers, sometimes with additional proprietary features.

[Delta Sharing](https://github.com/delta-io/delta-sharing) provides an open protocol and reference implementations for sharing analytical data. [OpenSharing](https://opensharing.io/) extends that protocol model toward tables, file volumes, models, and agent skills; it is a developing specification and ecosystem. The [Apache Iceberg REST Catalog specification](https://iceberg.apache.org/rest-catalog-spec/) defines a common catalog API and supports secure table access through credential vending or remote signing. Apache Iceberg remains a table format and catalog ecosystem rather than a complete usage-governance system.

These distinctions matter when evaluating interoperability. Two products can both support an open format while differing in identity, policy, filtering, version, or sharing-protocol behavior.

## Selection Questions

Choose a mechanism by asking:

1. Does the consumer need a copy, a query interface, a change stream, or only a derived result?
2. What latency and historical replay behavior are required?
3. Which party should bear storage and compute cost?
4. Can the consumer depend on provider availability at query time?
5. How will schema and semantic changes be communicated?
6. What must happen to local copies and derivatives after revocation?
7. Which engines, clouds, and identity systems must interoperate?
8. What usage evidence must the producer retain?

The answer is often a small portfolio of mechanisms behind one governed [data product](/docs/data/metadata/data-products/), not one protocol for every consumer.

## Common Failure Modes

- Calling an export job a data product without ownership, documentation, or service expectations
- Claiming zero-copy while ignoring client caches and downstream materialization
- Selecting streaming for low latency without defining replay, ordering, and compatibility
- Assuming an open storage format makes policy and identity portable
- Creating consumer copies without retention, correction, and deletion procedures
- Coupling critical consumers to a remote query path without availability and cost controls

## Summary

Data exchange mechanisms determine how a sharing boundary behaves technically. Files, APIs, streams, replication, live shares, open tables, and federation each move different responsibilities between producer and consumer.

The durable design principle is to select the data-plane mechanism together with its control plane. A share remains governable only when access, meaning, policy, provenance, change, usage, and withdrawal travel with the technical interface.
