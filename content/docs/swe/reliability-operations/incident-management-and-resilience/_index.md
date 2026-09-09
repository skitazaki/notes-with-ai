---
date: "2026-09-09T00:00:00+09:00"
title: "Incident Management & Resilience"
weight: 20
prev: "/docs/swe/reliability-operations/observability-and-slos"
next: "/docs/swe/reliability-operations/twelve-factor-app"
---

Resilience is the ability to continue, degrade deliberately, or recover when components, dependencies, people, or assumptions fail. Incident management coordinates action when a disruption is occurring; incident learning changes the system afterward.

## Design for bounded failure

Timeouts limit waiting, retries handle selected transient failures, circuit breakers interrupt repeated failure, and load shedding protects constrained capacity. Redundancy and isolation reduce shared failure. Each mechanism has a cost: retries can amplify overload, failover can transfer more traffic than a standby can handle, and graceful degradation can conceal prolonged damage.

Resilience therefore begins with failure modes, budgets, and boundaries. Identify which capability must continue, which may degrade, how long recovery can take, and where state can be lost. Capacity planning, dependency limits, backups, restore tests, and operational access are part of the design.

## Respond and learn

During an incident, establish clear coordination, track impact, maintain a shared timeline, and separate investigation from communication when scale requires it. Mitigation takes priority over proving a root cause. Decision authority and escalation should be known before pressure is high.

After recovery, review the technical and organizational conditions that allowed the impact to develop. Avoid reducing the event to one person's action; people usually operate within signals, interfaces, incentives, and safeguards designed by the system. Learning is complete only when it changes code, architecture, tests, runbooks, alerts, staffing, or another relevant condition.

Exercises and game days can validate assumptions before real failure, but experiments need observable success criteria, abort conditions, and bounded impact.

## Summary

Resilience limits how failure spreads and supports recovery. Incident management creates coordinated action, while follow-through converts experience into safer design and operation.
