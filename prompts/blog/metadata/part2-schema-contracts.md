---
type: blog
path: /blog/metadata/part2-schema-contracts
---

Write a blog post (roughly 2,200-2,800 words) titled:
"Types Become Contracts"

You are a senior data infrastructure engineer and technical writer
with deep experience in schema design, streaming systems, and distributed data platforms.

Audience:

- Software engineers, data engineers, analytics engineers, and platform architects
- Readers already understand SQL, APIs, object storage, and distributed systems basics
- Readers want a practical explanation of why schema evolution becomes an operational problem

Purpose:

- Explain how typed fields become producer-consumer contracts
- Show why metadata becomes operational once multiple systems depend on a shared schema
- Clarify how compatibility rules affect real systems and migrations

Scope:

- Focus on schema evolution, compatibility, registries, and contract enforcement
- Use concrete comparisons between Avro, JSON Schema, and Protobuf
- Keep the discussion implementation-oriented rather than governance-oriented

Tone & style:

- Neutral, explanatory, and precise
- No hype or marketing language
- Use short implementation examples where they sharpen the point
- Treat compatibility as a systems concern, not a policy slogan

Structure:

1. Start from the boundary established in Part 1: field meaning is now explicit, but shared systems still need change control
2. Explain why a schema becomes a contract once multiple producers and consumers depend on it
3. Compare backward compatibility, forward compatibility, and full compatibility with concrete examples
4. Contrast Avro, JSON Schema, and Protobuf in terms of typing, evolution rules, and operational tradeoffs
5. Explain the role of schema registries in event streams and service integration
6. Show migration failure modes such as renamed fields, enum expansion, optional-to-required changes, and semantic drift
7. End by showing why contracts are still not enough once metadata starts affecting file layout and runtime performance

Include:

- Short schema snippets in JSON, Avro IDL, Protobuf, or similar formats
- At least one example of a compatible change and one incompatible change
- A concrete streaming or event-driven example such as Kafka with a schema registry
- A discussion of semantic compatibility, not only syntactic compatibility

Constraints:

- Do not turn the article into a vendor comparison or product guide
- Do not reduce the topic to generic “data contract” advocacy
- Do not drift into legal or organizational governance language
- Do not cover Parquet internals in depth here; reserve that for the next article

Ending:

Close by setting up Part 3: once data is stored in large columnar files, metadata stops being only a logical contract and starts controlling compute efficiency.
