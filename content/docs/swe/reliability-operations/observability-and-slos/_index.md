---
date: "2026-09-09T00:00:00+09:00"
title: "Observability & SLOs"
weight: 10
prev: "/docs/swe/reliability-operations"
next: "/docs/swe/reliability-operations/incident-management-and-resilience"
---

Observability provides the evidence needed to investigate system behavior. Service-level objectives focus that evidence on reliability that users can experience and teams can manage.

## From telemetry to understanding

Logs record events, metrics summarize behavior over time, and traces connect work across boundaries. Profiles, deployment markers, topology, configuration, and business context may also be necessary. Collecting every signal is neither sufficient nor sustainable: data needs consistent identity, useful dimensions, retention rules, access control, and a relationship to operating questions.

Dashboards answer recurring known questions. Exploratory queries help investigate unfamiliar failure modes. Alerts should identify conditions that require action, include relevant context and ownership, and avoid training responders to ignore noise.

## Objectives and error budgets

A service-level indicator measures a user-relevant behavior, such as successful request proportion or end-to-end latency. A service-level objective defines an acceptable target over a window. The difference between perfect performance and the objective forms an error budget that can guide the balance between change and stability.

Objectives should reflect real user journeys and dependency responsibilities. Internal component metrics are useful for diagnosis but may not describe customer impact. Too many objectives dilute attention; targets that demand perfection can make normal change impossible without producing proportional value.

SLOs are decision tools, not contractual promises or individual performance scores. Teams need an agreed response when a budget is consumed, such as prioritizing reliability work, reducing rollout risk, or revisiting an unrealistic target.

## Summary

Observability makes behavior investigable; SLOs make reliability priorities explicit. Together they connect telemetry, user impact, alerts, and engineering decisions.
