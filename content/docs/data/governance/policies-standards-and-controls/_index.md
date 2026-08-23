---
date: "2026-08-22T00:00:00+09:00"
title: "Policies, Standards, and Controls"
weight: 3
prev: "/docs/data/governance/ownership-and-stewardship"
next: "/docs/data/governance/data-classification"
---

Governance connects intent to observable behavior through a rule hierarchy.

The hierarchy prevents two common problems: high-level statements that cannot be implemented, and technical controls that have no clear policy purpose. Each layer should be traceable to the layer above it while remaining appropriate to its own audience. Executives and policy owners state required outcomes; domain and technical specialists translate those outcomes into common requirements; delivery and platform teams operate the controls.

## The Hierarchy

| Element       | Purpose                                                 | Example                                                          |
| ------------- | ------------------------------------------------------- | ---------------------------------------------------------------- |
| **Principle** | Stable direction for decisions                          | Collect only data with a justified purpose                       |
| **Policy**    | Mandatory outcome and scope                             | Personal data must have an approved purpose and retention period |
| **Standard**  | Testable common requirement                             | Record purpose and retention category using defined values       |
| **Control**   | Mechanism that prevents, detects, or corrects deviation | Block publication when required metadata is absent               |
| **Evidence**  | Record that demonstrates design and operation           | Validation result, approval, exception, or audit event           |

The terms are related but not interchangeable. A principle guides judgment when no detailed rule exists. A policy makes an outcome mandatory for a defined scope. A standard reduces unnecessary variation by describing a testable requirement. A control is an action or mechanism, not another document. Evidence is the retained result that supports review and assurance.

A **control objective** states the result a control must achieve without prescribing one implementation. Preventive controls stop an unacceptable action; detective controls reveal it; corrective controls restore an acceptable state. Each can be manual or automated.

For example, a policy may require restricted data to be accessible only for approved purposes. A control objective could require access to be authorized and periodically reviewed. One system might implement that objective through group membership and quarterly certification; another might use time-limited entitlements and continuous monitoring. The implementations differ, but evidence should still demonstrate that the common objective was met.

## Designing and Operating Controls

Control design should identify the owner, trigger, inputs, expected result, failure behavior, frequency, evidence, and remediation path. A control that reports a failure without assigning remediation may create visibility without reducing risk. Likewise, a preventive control with no exception route may block legitimate work and encourage teams to bypass the governed path.

Manual controls are appropriate when interpretation is essential or the event is rare. Automated controls are useful for high-volume, repeatable decisions with reliable inputs. Many operating models combine them: automation handles routine cases, while ambiguous or high-impact cases are routed to an accountable person.

Policy-as-code expresses testable parts of policy in versioned, executable rules. It improves consistency and speed but cannot encode every contextual judgment. Rule ownership, input quality, explanation, override authority, and evidence retention remain governance concerns.

Policy-as-code should therefore be treated as a managed representation of policy, not as the policy's sole source of meaning. Changes to executable rules need review, testing, versioning, deployment controls, and a link back to the approved requirement. A machine decision should be explainable enough for an owner, affected team, or reviewer to understand which rule and inputs produced it.

## Interfaces

[Metadata](/docs/data/metadata/) represents assets, classifications, ownership, lineage, and rule results. Security implements protection mechanisms. [Data Privacy](/docs/data/privacy/) defines conditions for processing information about people. [Data Management](/docs/data/management/) operates quality and lifecycle practices. Platforms automate common controls. Governance coordinates their objectives without absorbing their specialist work.

Exceptions should identify the affected requirement, rationale, risk acceptance, compensating control, approver, and expiry. Evidence must show both that the control exists and that it operated over the relevant period.

Policies, standards, and controls should also have review and retirement conditions. Keeping obsolete rules can be as harmful as missing rules: teams may follow requirements that no longer address the risk, or encounter conflicting controls. Review should consider incidents, exceptions, operational cost, false positives, and changes to the governed environment.
