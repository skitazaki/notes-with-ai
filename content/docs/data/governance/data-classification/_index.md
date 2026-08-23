---
date: "2026-08-22T00:00:00+09:00"
title: "Data Classification"
weight: 4
prev: "/docs/data/governance/policies-standards-and-controls"
next: "/docs/data/governance/compliance-and-auditability"
---

Data classification assigns governance-relevant attributes to data so that obligations can vary according to context. It is broader than a single security label.

Without classification, an organization must either treat all data alike or rely on people to rediscover its context for every decision. The first approach applies excessive controls to low-risk data or inadequate controls to high-risk data. The second is slow and inconsistent. Classification creates a shared basis for selecting proportionate access, handling, retention, sharing, and monitoring requirements.

## Classification Dimensions

- **Sensitivity and confidentiality:** harm or exposure expected from unauthorized disclosure.
- **Personal-data status:** whether data relates to identifiable people and which processing conditions apply.
- **Regulatory or contractual relevance:** obligations attached to a record, agreement, or jurisdiction.
- **Business criticality:** impact if data is unavailable, incorrect, or delayed.
- **Lifecycle and retention category:** required retention, archival, legal hold, and disposal behavior.
- **Sharing restrictions:** permitted audiences, purposes, locations, and onward distribution.

Dimensions should remain separate when they lead to different obligations. “Confidential” alone cannot express whether data is business-critical, subject to deletion, or shareable for an approved purpose.

Classification schemes should use the smallest set of dimensions and values that produce meaningful decisions. More labels do not automatically create better governance. Each value needs a definition, examples, an accountable decision authority, and a statement of which obligations it triggers. Where dimensions interact, the scheme should explain whether the strictest obligation wins or whether a specific combination has its own rule.

## Assigning and Reviewing Classifications

Classification begins by identifying the governed object and the context in which it is used. The same field can have different implications when isolated, combined with other fields, published as an aggregate, or used to make a consequential decision. Classification may therefore apply to a field, dataset, record set, domain, data product, or use case; the applicable scope should be recorded.

Governance defines the scheme, meanings, decision authority, defaults, and resulting obligations. [Metadata](/docs/data/metadata/) represents classifications and propagates them with assets and lineage. Security and [Privacy](/docs/data/privacy/) consume relevant values to select and enforce safeguards.

Classification can be declared by an owner, inferred by discovery, inherited from a source, or derived from combinations. Automation should record provenance and confidence and route ambiguous or high-impact cases for review. Reclassification is a governed change: downstream access, retention, masking, sharing, and monitoring controls may all need reevaluation.

Declared classifications are useful when the owner understands the business context. Automated discovery can locate patterns at scale but may not know whether a value is real, synthetic, public, or used in a regulated process. Inheritance preserves source obligations through copies and transformations, but it needs explicit rules for aggregation, de-identification, and derived data. No single assignment method is sufficient for every asset.

Classification should be reviewed when meaning, composition, use, ownership, jurisdiction, or lifecycle state changes. The review should identify affected downstream assets through lineage and notify the owners of controls that depend on the changed value. This makes classification an operational governance mechanism rather than a static catalog tag.

## From Labels to Obligations

A classification becomes useful only when it changes a decision. Business-critical data may require stronger availability and quality monitoring. A retention category may determine archival and deletion schedules. Sharing restrictions may require purpose approval or prohibit onward distribution. Personal-data status may trigger a privacy assessment, while confidentiality may select security safeguards. Governance defines these mappings; the neighboring disciplines implement and operate the specialized controls.
