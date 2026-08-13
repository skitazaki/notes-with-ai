---
date: "2026-08-13T16:00:00+09:00"
title: "Delivery & DevOps"
weight: 40
prev: "/docs/swe/testing-quality-engineering"
next: "/docs/swe/reliability-operations"
---

Delivery connects a source change to a controlled outcome in a running environment. DevOps connects the people, practices, and platform capabilities needed to make that path fast, repeatable, observable, and accountable.

## From change to production

A delivery system transforms source code and configuration into versioned artifacts, evaluates them, promotes them through environments, and releases behavior to users. Each transformation should preserve identity and evidence: teams need to know what changed, how it was built, which checks ran, where it was deployed, and how to recover.

Build systems turn source inputs into reproducible outputs. Artifact management gives those outputs stable identity, integrity metadata, provenance, retention rules, and controlled promotion. CI integrates changes frequently and produces rapid feedback. Continuous delivery keeps the software in a releasable state; continuous deployment goes further by automatically releasing qualified changes to production.

## Release and deployment are different

Deployment places a software version into an environment. Release exposes its behavior to users or workloads. Separating the two enables feature flags, staged exposure, dark launches, and controlled experiments.

Rolling, blue-green, and canary strategies manage replacement and exposure differently. No strategy removes risk. A safe choice depends on compatibility, state migration, traffic control, observability, rollback behavior, and the cost of running multiple versions.

Progressive delivery uses production evidence to expand or stop a release. It works only when success criteria are explicit, telemetry is timely, and the organization can respond when signals disagree.

## Infrastructure and platform capabilities

Infrastructure as Code represents environmental intent in versioned, reviewable definitions. GitOps applies reconciliation so a declared state can be compared continuously with a running environment. Both improve traceability, but neither guarantees safe change without validation, access control, drift management, and recovery procedures.

Platform engineering packages recurring delivery and operational capabilities into supported paths that product teams can use without rebuilding every mechanism. An [Internal Developer Portal](../idp/) may make those capabilities discoverable, while the platform supplies the underlying workflows, environments, policies, and services.

Developer experience is an outcome of this delivery system. Engineers need fast feedback, understandable failures, predictable environments, and a clear path from intent to production. A platform should reduce incidental complexity without concealing the system knowledge required to operate software responsibly.

## DevOps as an operating model

DevOps is not a team name or a collection of automation tools. It is an operating model that reduces the distance between development and operations through shared ownership, feedback, automation, and learning. Product teams remain connected to production outcomes, while specialists build reusable capabilities and guardrails.

Delivery metrics can reveal waiting time and system friction, but they require context. Deployment frequency, lead time, failure rate, and recovery time are useful signals when they support learning. Used as isolated targets, they can reward smaller definitions, hidden work, or unsafe behavior.

## Common misconceptions

- **A pipeline is not the whole delivery system.** Artifact stores, environments, permissions, rollout controls, telemetry, and human decisions also matter.
- **Automation does not remove accountability.** It moves decisions into code, policy, and exception handling.
- **Rollback is not always reversal.** Data migrations, messages, and external side effects may require forward recovery.
- **Standardization should not erase legitimate differences.** Good platforms standardize recurring needs while allowing explicit escape paths.

## Summary

Delivery and DevOps turn change into a traceable production outcome. Builds, artifacts, CI/CD, deployment strategies, infrastructure definitions, and platform capabilities form one feedback system whose purpose is safe, sustainable flow rather than automation for its own sake.
