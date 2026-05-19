---
title: "Metadata Starts as Column Names"
date: "2026-05-19T10:00:00+09:00"
tags: ["Metadata", "Data", "Schema", "Architecture"]
categories: ["Technology", "Data"]
draft: false
---

Metadata sounds abstract until a CSV breaks something important.

An analyst opens a file and sees columns named `timestamp`, `value`, `region`, and `customer_id`. The data looks usable. A pipeline loads it. A dashboard renders. A downstream team joins it with another dataset and gets the wrong answer. Nothing in the column names explains whether `timestamp` is UTC or local time, whether `value` is gross revenue or net revenue, whether `region` is a sales territory or an ISO country code, or whether `customer_id` is stable across source systems.

This is where metadata usually starts: not in a catalog or governance platform, but in the uncomfortable gap between a column name and the meaning people assume from it.

The first article in this series stays deliberately close to that problem. Before metadata becomes a control plane, it first becomes a way to make fields interpretable. The core point is simple: even basic schema metadata already behaves like a contract.

It extends the foundation in [Metadata](/docs/data/metadata/) and the series overview in [Metadata Systems — From Column Comments to Distributed Control Planes](/blog/metadata/), but keeps the focus on the smallest useful unit: the field.

## Column Names Are Helpful, But Not Sufficient

Column names are compact hints. They work well when the producer and consumer are the same person, the dataset is small, and the meaning is still fresh in memory.

They break down when data crosses time, teams, or systems.

Consider this simple file:

```csv
customer_id,signup_date,plan,usage,amount
1001,2026-05-01,pro,42,199
1002,2026-05-01,team,17,399
```

Nothing here is technically invalid. The problem is that the file leaves important questions unanswered.

- Is `signup_date` a date or a timestamp truncated to day granularity?
- Is `usage` measured in API calls, gigabytes, or active minutes?
- Is `amount` stored in USD, JPY, or cents?
- Is `customer_id` an internal surrogate key or an externally meaningful identifier?
- Can `plan` contain values other than `pro` and `team`?

Those questions are not documentation polish. They affect joins, aggregations, billing logic, reproducibility, and incident response. A field name gives a label. A schema begins to define behavior.

## Metadata Inside Simple Tables

Even the most ordinary tabular data depends on metadata dimensions that are easy to underestimate.

### Type

If a field is called `amount`, the consuming system still needs to know whether it is an integer, decimal, string, or nullable value. Type determines parsing, validation, storage, and arithmetic behavior.

CSV itself does not preserve type information. Everything is text until another system decides otherwise.

That ambiguity creates failure modes such as:

- `00123` being parsed as a number and losing leading zeros
- `1.0` being treated as a float in one system and a decimal string in another
- `true` and `false` being ingested as strings rather than booleans

### Nullability

An empty field can mean at least four different things: unknown, not applicable, not yet collected, or invalid extraction. Those meanings are operationally different.

If a nullable field is treated as required downstream, missing values become runtime defects. If a required field is treated as optional, bad records pass silently into analytical outputs.

### Units

A field called `duration` is not useful enough for computation unless its unit is known. Seconds, milliseconds, minutes, and hours are all plausible. The same problem appears with distance, money, storage size, temperature, and rate fields.

Many production incidents are not caused by missing data. They are caused by correctly formatted data expressed in the wrong unit.

### Time Semantics

Time fields are especially dangerous because a name like `created_at` looks precise while still leaving major ambiguity unresolved.

Important questions include:

- Is the value a date, timestamp, or local wall-clock time?
- Which timezone applies?
- Is daylight saving time relevant?
- Is this event time, ingestion time, or processing time?

Two systems can both parse the same timestamp string and still disagree about what happened when.

### Business Meaning

Metadata is not only about technical shape. A field also needs semantic meaning.

For example, `status` may describe:

- an order lifecycle state
- a payment authorization outcome
- a customer support disposition
- a pipeline execution result

The same word can represent different finite state machines in different domains. Without business context, technically correct reuse still produces analytical mistakes.

## Why "Just Add Comments" Does Not Fully Solve It

Comments help. Field descriptions, wiki notes, and README files are useful because they capture intent that a bare schema cannot always express.

But comments alone are not enough for two reasons.

First, they are often detached from the data itself. A CSV might travel through email, object storage, notebooks, and ETL scripts while its explanatory document remains elsewhere.

Second, free-form comments are difficult for machines to validate. A human can read "amount in yen" and interpret it correctly. A pipeline cannot reliably enforce that statement unless the metadata is structured.

This is the first important escalation in the series. The moment metadata needs to travel with the data and support automated checks, it starts moving from annotation toward infrastructure.

## Field Schema As A Portable Contract

The simplest useful step beyond column names is an explicit field schema: a structured declaration of what each field is supposed to contain.

At a minimum, that schema should describe:

- field name
- logical type
- nullability or requiredness
- allowed values or constraints when relevant
- description of business meaning
- unit, format, or timezone when needed

This is why lightweight schema standards matter. They make field-level meaning portable enough to be shared across tools and teams.

One practical example is [Frictionless Data](https://frictionlessdata.io/), which provides a simple way to describe tabular resources and their fields.

```json
{
  "fields": [
    {
      "name": "customer_id",
      "type": "string",
      "description": "Stable billing system customer identifier"
    },
    {
      "name": "signup_date",
      "type": "date",
      "description": "Customer signup date in UTC"
    },
    {
      "name": "amount_jpy",
      "type": "integer",
      "description": "Monthly subscription amount in Japanese yen",
      "constraints": {
        "required": true,
        "minimum": 0
      }
    }
  ]
}
```

That schema is still small. It does not solve governance, lineage, or distributed coordination. But it already does something important: it narrows interpretation.

It tells downstream consumers that `amount_jpy` is not just a generic number. It is a non-negative integer measured in a specific currency. It tells them that `signup_date` is intended as a date in UTC, not a locale-dependent string.

Frictionless-style metadata can also be packaged alongside a resource description:

```yaml
resources:
  - name: subscriptions
    path: subscriptions.csv
    schema:
      fields:
        - name: customer_id
          type: string
          description: Stable billing system customer identifier
        - name: signup_date
          type: date
          description: Customer signup date in UTC
        - name: plan
          type: string
          constraints:
            enum: [free, pro, team]
        - name: amount_jpy
          type: integer
          description: Monthly subscription amount in Japanese yen
          constraints:
            required: true
            minimum: 0
```

This is still metadata at the edge of the system, but it already behaves like a contract between whoever produced the file and whoever consumes it next.

## What The Contract Actually Protects

Calling a schema a contract can sound overstated at first. In a small file exchange, it may seem like a convenience feature rather than a systems concern.

But field metadata already constrains behavior in several concrete ways.

### Parsing

If a field is declared as a date, timestamp, integer, or boolean, parsers can reject incompatible values early instead of allowing implicit coercion.

### Validation

Requiredness, enumerations, ranges, and formats make it possible to distinguish valid records from malformed ones before they propagate.

### Interpretation

Descriptions, units, and semantic names reduce the risk that two teams compute different metrics from the same raw field.

### Interoperability

Structured metadata can travel between local scripts, validation tools, ingestion jobs, and storage layers more reliably than prose in an external document.

### Change Detection

Once a schema exists, changes become visible. A new field, a renamed field, or a type change is no longer invisible drift. It becomes a change against an expected contract.

That last point matters more than it first appears. As soon as two systems depend on the same schema, metadata is no longer just about description. It starts coordinating expectations.

## Common Metadata Ambiguities

Field-level metadata earns its keep by preventing boring but costly mistakes.

### Timezone Drift

Suppose an application records a purchase at `2026-05-01T00:30:00` in Tokyo, but exports the value without a timezone. A downstream warehouse assumes all bare timestamps are UTC. Both systems are internally consistent. The error appears only when the data is merged.

In the application, that purchase belongs in the May 1 daily sales total for Japan. In the warehouse, the same value is interpreted as `2026-05-01 00:30 UTC`, which becomes `2026-05-01 09:30 JST` if converted back later. If the original event was actually `2026-05-01 00:30 JST`, the correct UTC value should have been `2026-04-30 15:30 UTC`. A daily rollup by UTC date will count that purchase on April 30, while a dashboard grouped by Japan local date expects it on May 1.

The result may be subtle but expensive: shifted retention windows, daily revenue totals that disagree across teams, or event sequences that appear to occur before the user action that triggered them.

### Unit Mismatch

An upstream service records `duration` in milliseconds. A downstream notebook assumes seconds. The values are numerically valid in both systems, but all percentile and cost estimates become wrong by a factor of 1,000.

### Identifier Instability

A field named `customer_id` may look canonical, but some identifiers are scoped to a product, tenant, region, or billing platform. Suppose `customer_id = 42` is unique only within each tenant. If a warehouse joins an orders table to a customer table on `customer_id` alone, orders from tenant `acme` can incorrectly attach to customer `42` from tenant `globex`. The SQL join succeeds, but the result turns one tenant-local identifier into a false global customer key.

### Silent Enum Expansion

If `plan` was originally `free`, `pro`, or `team`, downstream logic often bakes in those assumptions. The moment an upstream producer adds `enterprise`, dashboards, billing rules, and filters can all become incomplete without any obvious parser failure.

These are not edge cases. They are normal outcomes when field meaning is assumed rather than declared.

## The Boundary Of Part 1

This article stays intentionally narrow. It is not yet about schema registries, Avro compatibility rules, or lakehouse metadata trees.

The boundary here is simpler: a field schema is the first durable answer to the question, "What does this column actually mean?"

That answer has limits. A field schema can describe structure and some semantics, but it does not by itself guarantee that producers and consumers evolve together safely. It does not manage versioning strategy. It does not explain how multiple services negotiate change. It does not solve coordination once data moves continuously rather than as occasional files.

Still, the important transition has already happened. The moment a team writes down type, requiredness, meaning, units, and constraints in machine-readable form, metadata stops being just a note for humans. It becomes an interface.

## From Field Meaning To Compatibility

That interface is where the next layer begins.

Once schemas are shared across pipelines, APIs, events, or streaming topics, the problem is no longer only "What does this field mean?" It becomes "What happens when this meaning changes while other systems still depend on it?"

That is the handoff from Part 1 to Part 2.

Part 2 will look at how types become contracts in a stronger sense: versioning, backward and forward compatibility, schema registries, and the producer-consumer coordination problems that appear as soon as structured data becomes operational.
