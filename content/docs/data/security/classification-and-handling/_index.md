---
date: "2026-08-22T00:00:00+09:00"
title: "Data Classification and Handling"
weight: 1
prev: "/docs/data/security"
next: "/docs/data/security/data-protection-techniques"
---

Data classification translates sensitivity and business criticality into handling requirements that protection, access, sharing, monitoring, retention, and disposal controls can use. A catalog label that does not change system behavior or operating decisions provides little protection.

## Classification Dimensions

- **Confidentiality** describes the consequence of unauthorized disclosure, often with levels such as public, internal, confidential, and restricted.
- **Business criticality** describes the consequence if data is corrupted, unavailable, or destroyed. Data can be critical without being confidential.
- **Regulatory or contractual sensitivity** identifies specific handling commitments. Personal information is one category, but appropriate-use decisions remain in [Data Privacy](/docs/data/privacy/).
- **Integrity and authenticity needs** identify where unauthorized changes or uncertain provenance create material harm.
- **Lifecycle state** distinguishes active, shared, archived, expired, and pending-deletion data when those states change permitted actions.

Keep levels few enough to apply consistently. Each should have a definition, examples, owner, and default handling profile.

## From Labels to Controls

| Area       | Example handling decision                                              |
| ---------- | ---------------------------------------------------------------------- |
| Storage    | Approved locations, encryption, tenant or environment isolation        |
| Access     | Eligible roles, approvals, privileged-access restrictions              |
| Processing | Whether raw values may appear in notebooks, logs, tests, or AI prompts |
| Sharing    | Approved recipients, interfaces, transformations, and boundaries       |
| Movement   | Transport protection and permitted regions or networks                 |
| Monitoring | Audit depth, alert thresholds, and review expectations                 |
| Disposal   | Deletion method and treatment of replicas and backups                  |

Detailed identities and authorization policies belong in [Access Control](/docs/acc/). Classification supplies attributes and context for those decisions.

## Classification Metadata

[Metadata](/docs/data/metadata/) makes classification portable and discoverable. Record the value, scope, source, confidence, reviewer, timestamp, and handling profile at the appropriate dataset, column, field, file, event, model-input, or output level.

Automated discovery can propose labels from schemas, names, patterns, content, and lineage. Human review remains important for ambiguous business meaning and high-impact decisions. Record confidence and provenance so a machine suggestion is not mistaken for an approved determination.

Propagate classification through lineage when derived data preserves sensitivity. Aggregation may reduce exposure, while joins can increase it, so evaluate transformation semantics rather than blindly copying the highest label.

## Operating Principles

- Classify early, before copies proliferate.
- Do not give unknown data the least restrictive default.
- Separate automated discovery from approval.
- Attach reusable handling profiles to classes.
- Reassess after new joins, consumers, destinations, or uses.
- Test that storage, export, sharing, and monitoring controls respond to labels.

## Summary

Classification connects knowledge about data to enforceable behavior. It works when understandable labels are recorded as metadata, propagated with context, and mapped to concrete controls.
