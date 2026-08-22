---
date: "2026-08-22T00:00:00+09:00"
title: "Policies, Standards, and Controls"
weight: 3
prev: "/docs/data/governance/ownership-and-stewardship"
next: "/docs/data/governance/data-classification"
---

Governance connects intent to observable behavior through a rule hierarchy.

## The Hierarchy

| Element       | Purpose                                                 | Example                                                          |
| ------------- | ------------------------------------------------------- | ---------------------------------------------------------------- |
| **Principle** | Stable direction for decisions                          | Collect only data with a justified purpose                       |
| **Policy**    | Mandatory outcome and scope                             | Personal data must have an approved purpose and retention period |
| **Standard**  | Testable common requirement                             | Record purpose and retention category using defined values       |
| **Control**   | Mechanism that prevents, detects, or corrects deviation | Block publication when required metadata is absent               |
| **Evidence**  | Record that demonstrates design and operation           | Validation result, approval, exception, or audit event           |

A **control objective** states the result a control must achieve without prescribing one implementation. Preventive controls stop an unacceptable action; detective controls reveal it; corrective controls restore an acceptable state. Each can be manual or automated.

Policy-as-code expresses testable parts of policy in versioned, executable rules. It improves consistency and speed but cannot encode every contextual judgment. Rule ownership, input quality, explanation, override authority, and evidence retention remain governance concerns.

## Interfaces

[Metadata](/docs/data/metadata/) represents assets, classifications, ownership, lineage, and rule results. Security implements protection mechanisms. [Data Privacy](/docs/data/privacy/) defines conditions for processing information about people. [Data Management](/docs/data/management/) operates quality and lifecycle practices. Platforms automate common controls. Governance coordinates their objectives without absorbing their specialist work.

Exceptions should identify the affected requirement, rationale, risk acceptance, compensating control, approver, and expiry. Evidence must show both that the control exists and that it operated over the relevant period.
