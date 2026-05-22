---
title: "Types Become Contracts"
date: "2026-05-20T10:00:00+09:00"
tags: ["Metadata", "Data", "Schema", "Architecture"]
categories: ["Technology", "Data"]
draft: false
---

Part 1 ended at an important boundary. Once field meaning becomes explicit, ambiguity drops, but coordination work does not.

A team can document that `customer_id` is a string, `created_at` is UTC, and `plan` belongs to a small enum. That already improves validation and interpretation. The harder problem begins when several producers and consumers depend on the same shape at the same time. A field definition is no longer only descriptive. It starts constraining change.

That is the moment when types become contracts.

This article extends [Metadata Starts as Column Names](/blog/metadata/part1-field-schema/) and the series overview in [Metadata Systems - From Column Comments to Distributed Control Planes](/blog/metadata/). The focus here is narrower than governance language usually implies. The practical question is not whether contracts are a good idea in the abstract. It is how schema changes behave once streams, services, warehouses, and jobs are all relying on them.

## A Schema Becomes A Contract When Change Has Consequences

Inside one script, a type annotation is mostly local. If you rename a field, you update the same codebase and move on.

Across systems, the same change is different. A producer may publish an event to Kafka, a stream processor may transform it, a storage job may land it in object storage, and several consumers may materialize views or trigger workflows from the same topic. None of those systems deploy in lockstep.

Suppose an order service publishes this event:

```json
{
  "order_id": "o-1001",
  "customer_id": "c-42",
  "status": "paid",
  "amount_jpy": 12000,
  "created_at": "2026-05-20T08:15:00Z"
}
```

That payload carries more than data values.

- Consumers assume `order_id` is stable.
- Billing systems assume `amount_jpy` is an integer in yen, not a decimal in major currency units.
- Status handling code assumes values such as `paid` and `cancelled` have specific business meaning.
- Monitoring and alerting logic assumes `created_at` is event time, not processing time.

Once those assumptions are encoded in multiple places, the schema has become an interface between independently changing systems. Any modification has to answer a concrete operational question: what happens to consumers that have not changed yet?

That is what a contract protects. It does not guarantee that the business meaning is correct. It guarantees that producers and consumers can coordinate change without relying on simultaneous deployment.

## Compatibility

Most schema discussions eventually reduce to compatibility rules because those rules determine whether a changed producer can safely talk to an unchanged consumer, or vice versa.

The three common terms are backward compatibility, forward compatibility, and full compatibility. They sound simple, but they are only useful when grounded in an actual producer-consumer relationship.

### Backward

Backward compatibility means new consumers can read data produced with an older schema.

Start with a simple Avro-style record:

```avdl
record OrderCreated {
  string order_id;
  string customer_id;
  int amount_jpy;
}
```

Now imagine adding an optional field with a default:

```avdl
record OrderCreated {
  string order_id;
  string customer_id;
  int amount_jpy;
  union { null, string } coupon_code = null;
}
```

This is typically backward compatible. A new consumer that expects `coupon_code` can still read older messages because the missing field resolves to its default.

An incompatible example is changing the type of `amount_jpy` from `int` to `string` without a migration boundary. Old data remains encoded as numbers. A new consumer expecting strings can no longer interpret the field consistently.

### Forward

Forward compatibility means old consumers can read data produced with a newer schema.

Using the same example, an old consumer that knows only `order_id`, `customer_id`, and `amount_jpy` can usually ignore the newly added `coupon_code` field. That change is often forward compatible.

Renaming a field is usually not. If the producer changes `amount_jpy` to `amount_minor` and the old consumer still expects `amount_jpy`, there is no automatic bridge unless the format or tooling supports aliases and every relevant component uses them correctly.

### Full

Full compatibility requires both directions to remain safe across adjacent versions. In practice, it favors changes that are additive, defaulted, or explicitly aliased rather than destructive.

The safe-looking part matters. A field rename often looks harmless to a human reviewer because the values did not change. For distributed systems, rename is not cosmetic. It changes how the field is located and decoded.

The reason compatibility matters so much is deployment reality. Producers and consumers change at different times. A compatibility rule is a way to survive that gap.

## Change Patterns

Teams often learn compatibility rules as a checklist, but the rules express asymmetry in how systems evolve.

These changes are usually compatible when handled carefully:

- adding an optional field
- adding a field with a default value
- expanding a message with data that older consumers can ignore
- widening certain numeric types when the format supports it and the consumer logic can still interpret the values

These changes are commonly incompatible:

- renaming a field without alias support and migration handling
- changing a required field to a different logical type
- making an optional field required without a backfill plan
- reusing an enum value name for a different semantic meaning
- changing units without changing the field name and contract description

That last case is where purely syntactic compatibility becomes misleading. If `latency` used to be milliseconds and is now seconds, the schema may still parse. The contract has still been broken.

## Format Tradeoffs

[Avro](https://avro.apache.org/), [JSON Schema](https://json-schema.org/), and [Protobuf](https://protobuf.dev/) are often discussed together because all three describe structure. Operationally, they make different tradeoffs around typing, encoding, and evolution.

### Avro

Avro is strongly oriented toward data pipelines and event streams. Schema is central, and compatibility rules are explicit enough that registries can enforce them in a predictable way.

Avro records are field-based rather than tag-based. That makes names and defaults important to schema evolution.

```json
{
  "type": "record",
  "name": "OrderCreated",
  "fields": [
    { "name": "order_id", "type": "string" },
    { "name": "customer_id", "type": "string" },
    { "name": "amount_jpy", "type": "int" },
    {
      "name": "coupon_code",
      "type": ["null", "string"],
      "default": null
    }
  ]
}
```

Operational strengths:

- clear defaults and unions support additive evolution
- registry tooling commonly supports backward and forward checks
- compact binary encoding works well in streaming systems

Operational limits:

- schema design discipline matters because field names and defaults carry a lot of migration weight
- certain changes that look small, such as renames, require deliberate handling rather than casual refactors

### JSON Schema

JSON Schema is flexible and widely used for APIs and validation boundaries. It is excellent at expressing constraints, but that same flexibility makes evolution rules less uniform across tooling.

```json
{
  "type": "object",
  "properties": {
    "order_id": { "type": "string" },
    "customer_id": { "type": "string" },
    "amount_jpy": { "type": "integer", "minimum": 0 },
    "coupon_code": { "type": ["string", "null"] }
  },
  "required": ["order_id", "customer_id", "amount_jpy"],
  "additionalProperties": false
}
```

Operational strengths:

- expressive validation rules for objects, patterns, ranges, and nested structures
- natural fit for HTTP payload validation and JSON-native systems
- easy for humans to inspect and reason about

Operational limits:

- compatibility policy is less intrinsic than in Avro; teams must define what counts as safe
- permissiveness varies with schema style, especially around `additionalProperties`, defaults, and loose typing
- binary transport and compact evolution are not the primary design center

JSON Schema is best understood as a strong validation language, not as a single standardized evolution strategy.

### Protobuf

Protobuf is optimized for service communication and binary efficiency. Evolution works differently because fields are identified by numeric tags, not only names.

```proto
syntax = "proto3";

message OrderCreated {
  string order_id = 1;
  string customer_id = 2;
  int32 amount_jpy = 3;
  string coupon_code = 4;
}
```

Operational strengths:

- compact binary encoding and generated clients work well for service boundaries
- unknown fields can be ignored by older readers in many scenarios
- numeric tags provide a stable identity even if display names change

Operational limits:

- tag reuse is dangerous; once a field number is published, it effectively becomes part of the long-term contract
- presence, defaults, and optional semantics can be subtle depending on version and language runtime
- service teams may mistake syntactic success for semantic safety because decoding still works after a meaning change

Protobuf tends to make safe additive evolution straightforward, but it punishes careless field retirement and tag recycling.

## Schema Registries

Once events move through a shared stream, compatibility rules need somewhere to live. This is why schema registries matter.

Consider a Kafka topic called `orders.created`. A producer service writes messages, a fraud service consumes them in real time, a storage sink lands them into object storage, and an analytics pipeline reads the stored data later. Without a registry, each component may carry its own copy of the schema, its own parsing assumptions, and its own release timing.

A registry centralizes several operational functions:

- schema version storage
- compatibility validation at registration time
- schema lookup by identifier during serialization and deserialization
- shared visibility into which subject or topic uses which contract

In practice, teams rarely implement this layer from scratch. They usually adopt registry tooling that is already integrated with their event platform, serializer stack, or cloud environment. Common examples include [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html), which is closely associated with Kafka and Avro-centric workflows, [Apicurio Registry](https://www.apicur.io/registry/), which supports multiple schema and API artifact types in a more general registry model, [Karapace](https://karapace.io/), which provides a Schema Registry-compatible option commonly used in Kafka deployments, and [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html), which targets managed streaming and event-driven integration inside AWS environments.

Those tools differ in packaging, ecosystem assumptions, and supported artifact models, but they solve the same operational problem: making schema compatibility checks happen before bad messages spread through a running system.

The important effect is not centralization for its own sake. It is the ability to reject a bad change before it hits a hot path.

For example, if the current schema for `orders.created` requires `amount_jpy` and a producer attempts to register a new version that renames it to `amount_minor` without an allowed compatibility path, the registry can fail the registration. That failure is cheap compared with discovering the problem through broken consumers after deployment.

In streaming systems, that difference matters because messages are not polite. Once published, they propagate quickly into state stores, compacted topics, dead-letter queues, and long-retained storage. Rejecting an incompatible schema up front is often the lowest-cost control point.

Registries also make contract scope visible. A schema attached to one internal topic is not the same as a schema attached to a public event stream consumed by many teams. The compatibility setting may need to be stricter for the latter because deployment coordination is weaker.

## Migration Failures

Initial schemas are rarely perfect, but most production pain comes from how they change.

### Field Renames

Field rename is one of the most common mistakes because it looks harmless in source control.

From the producer perspective, changing `customer_id` to `account_id` might reflect a better domain model. For existing consumers, it removes the field they depend on and introduces one they do not recognize. Unless the migration keeps both names temporarily, or the format supports aliases in a way every consumer actually uses, this is a breaking change.

### Enum Expansion

Adding enum values looks additive, but downstream logic often treats enum domains as closed.

Suppose an order status enum originally contains `pending`, `paid`, and `cancelled`. A producer later adds `refunded`.

```proto
enum OrderStatus {
  ORDER_STATUS_UNSPECIFIED = 0;
  PENDING = 1;
  PAID = 2;
  CANCELLED = 3;
  REFUNDED = 4;
}
```

Parsing may still succeed. Consumer business logic may not. Dashboards can drop the new state. Alerting rules can misclassify it. State machines can fall into default branches that were never meant for valid production traffic.

This is a good example of the difference between wire compatibility and behavioral compatibility.

### Requiredness Changes

Changing a field from optional to required is often a contract violation disguised as cleanup.

If older producers omit `coupon_code`, a new consumer that now requires it cannot safely process historical messages or lagging producers. Even in request-response systems, rolling deployments mean some nodes will still send the older shape for a while.

The safe path is usually staged:

1. Add the field as optional.
2. Backfill or populate it consistently.
3. Verify population across producers.
4. Only then consider tightening validation where every participant can meet the stronger requirement.

### Semantic Drift

Semantic drift is the most expensive failure mode because schema validators cannot fully catch it.

Imagine that `amount_jpy` initially means gross order amount including tax. Later, the producer changes it to net amount before tax to satisfy a new finance process, but keeps the field name unchanged to avoid breaking parsers.

Everything still deserializes. Nothing is syntactically broken. Revenue dashboards, fraud thresholds, refund logic, and anomaly detection all start operating on a different meaning.

This is why contracts cannot stop at type-level compatibility. A field name, description, unit, and business definition are all part of what consumers rely on.

## Semantic Compatibility

Schema tooling is good at checking structure. It is weaker at checking meaning.

Two payloads can be structurally compatible while being operationally incompatible:

- currency changes from yen to dollars while the integer type stays the same
- `created_at` changes from event time to ingestion time while remaining a timestamp
- `customer_id` changes from a global identifier to a tenant-local identifier while staying a string

These failures often arrive during migrations because teams focus on parser success. Parser success is a necessary condition, not a sufficient one.

A practical contract therefore needs both machine-checkable structure and human-maintained semantic guarantees. That usually means keeping descriptions, units, ownership, and migration notes close to the schema rather than in disconnected prose. It also means reviewing changes with consumer behavior in mind, not only serializer behavior.

One useful question in review is simple: if an unchanged consumer silently accepts this new message, could it still produce the wrong answer? If the answer is yes, the change may be syntactically compatible but semantically unsafe.

## Beyond Contracts

At this stage, metadata is already operational.

It controls whether events can be published, whether consumers can decode them, whether validators reject bad payloads, and whether rolling deployments remain safe. That is a major shift from the Part 1 world of column names and field descriptions.

It is still not the whole system.

Contracts protect logical interpretation across producers and consumers. They do not explain how metadata affects scan cost, predicate pruning, encoding choices, row-group layout, or file-level planning once data lands in large analytical storage formats. A stream contract can tell a consumer that `created_at` is a timestamp. It cannot tell a query engine how many row groups can be skipped before reading a Parquet file.

That next step matters because metadata eventually stops being only an interface between applications. It becomes part of compute efficiency itself.

Part 3 moves into that boundary. Once data is stored in large columnar files, metadata is no longer only a logical contract between producer and consumer. It starts controlling what work the engine has to do.
