---
date: "2026-09-09T00:00:00+09:00"
title: "Continuous Delivery"
weight: 10
prev: "/docs/swe/delivery-devops"
next: "/docs/swe/delivery-devops/deployment-strategies"
---

Continuous delivery is the capability to keep software in a releasable state through frequent integration, automated evidence, and a repeatable path to production. Continuous deployment is a policy that automatically releases qualified changes; it is not required to gain the benefits of continuous delivery.

## A controlled flow of change

The delivery path begins with versioned source and produces an identifiable artifact. Build once and promote the same artifact across environments so later stages evaluate what production will run. Configuration and release metadata may vary, but the executable should not be silently rebuilt.

Pipelines coordinate checks, packaging, provenance, environment changes, and approvals. Their purpose is not automation volume. A useful pipeline makes state visible, fails clearly, and produces evidence appropriate to the risk of the change. Fast early checks protect developer flow; slower system and security checks add depth where needed.

Release readiness includes more than a green test suite. Compatibility, migrations, observability, operational documentation, access control, and recovery options all influence whether a change can be released responsibly. Small batches reduce the number of interacting assumptions and shorten diagnosis.

## Improve the system, not the metric

Lead time, deployment frequency, change failure, and recovery measures can expose queues and weak feedback. They become harmful when treated as isolated performance targets. A team can raise deployment counts by redefining a deployment without improving its ability to deliver value safely.

Continuous delivery depends on shared ownership. Product teams remain connected to production outcomes, while platform and specialist teams provide reusable capabilities and guardrails. Manual decisions can remain where judgment is valuable, provided they are timely, explicit, and supported by sufficient evidence.

## Summary

Continuous delivery creates a dependable route from source change to release decision. Reproducible artifacts, layered evidence, small batches, and visible operational readiness keep software releasable without equating speed with uncontrolled automation.
