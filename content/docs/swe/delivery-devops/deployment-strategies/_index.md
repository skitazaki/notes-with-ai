---
date: "2026-09-09T00:00:00+09:00"
title: "Deployment Strategies"
weight: 20
prev: "/docs/swe/delivery-devops/continuous-delivery"
next: "/docs/swe/delivery-devops/internal-developer-portal"
---

Deployment places a software version into an environment; release exposes its behavior to users or workloads. Treating these as separate decisions makes risk easier to control.

## Replacement and exposure

A rolling deployment replaces instances gradually and uses limited extra capacity, but old and new versions coexist. Blue-green deployment maintains two complete environments and switches traffic, enabling fast traffic reversal at greater infrastructure cost. Canary deployment exposes a new version to a small population before expanding it.

Feature flags separate code deployment from feature release. They support targeted exposure and rapid disabling, but flags add runtime paths and require ownership, observability, and removal dates. Dark launches exercise new components without making their outputs authoritative.

No strategy is safe by name alone. Teams must consider capacity, session state, background work, traffic control, dependency compatibility, and whether signals can distinguish versions. Progressive delivery needs explicit success and stop criteria; otherwise gradual exposure only makes failure slower.

## Recovery and data change

Rollback is straightforward only when the prior version remains compatible with current data and external effects. Database migrations should use staged, backward-compatible changes where possible. Messages, notifications, payments, and irreversible writes may require forward recovery or compensation rather than reversal.

A deployment plan therefore includes detection, decision authority, recovery steps, and validation after recovery. Rehearsing these paths is more credible than assuming a tool's rollback button is sufficient.

## Summary

Deployment strategies control how versions replace one another and how behavior is exposed. Their safety comes from compatibility, observable criteria, bounded impact, and realistic recovery—not from the strategy label.
