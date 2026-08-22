---
date: "2026-08-22T00:00:00+09:00"
title: "Data Classification"
weight: 4
prev: "/docs/data/governance/policies-standards-and-controls"
next: "/docs/data/governance/compliance-and-auditability"
---

Data classification assigns governance-relevant attributes to data so that obligations can vary according to context. It is broader than a single security label.

## Classification Dimensions

- **Sensitivity and confidentiality:** harm or exposure expected from unauthorized disclosure.
- **Personal-data status:** whether data relates to identifiable people and which processing conditions apply.
- **Regulatory or contractual relevance:** obligations attached to a record, agreement, or jurisdiction.
- **Business criticality:** impact if data is unavailable, incorrect, or delayed.
- **Lifecycle and retention category:** required retention, archival, legal hold, and disposal behavior.
- **Sharing restrictions:** permitted audiences, purposes, locations, and onward distribution.

Dimensions should remain separate when they lead to different obligations. “Confidential” alone cannot express whether data is business-critical, subject to deletion, or shareable for an approved purpose.

Governance defines the scheme, meanings, decision authority, defaults, and resulting obligations. [Metadata](/docs/data/metadata/) represents classifications and propagates them with assets and lineage. Security and [Privacy](/docs/data/privacy/) consume relevant values to select and enforce safeguards.

Classification can be declared by an owner, inferred by discovery, inherited from a source, or derived from combinations. Automation should record provenance and confidence and route ambiguous or high-impact cases for review. Reclassification is a governed change: downstream access, retention, masking, sharing, and monitoring controls may all need reevaluation.
