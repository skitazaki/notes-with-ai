---
date: "2026-05-10T14:00:00+09:00"
title: "Reference Architectures"
weight: 12
prev: "/docs/acc/decision-frameworks"
next: "/docs/acc/concept-dictionary"
---

Reference architectures are not universal blueprints. They are calibrated examples that show how principles, controls, and tradeoffs fit together in realistic environments.

## Executive Summary

Three patterns appear repeatedly:

- an enterprise workforce architecture centered on federation, PAM, and governance
- a cloud-native platform architecture centered on workload identity and policy enforcement
- an AI-agent architecture centered on constrained delegation and approval boundaries

These examples help teams reason across system boundaries instead of optimizing one control domain in isolation.

## Core Concepts

### Enterprise workforce architecture

Authoritative HR feeds lifecycle events into an identity platform. Federation provides SSO to internal and SaaS applications. MFA and conditional access raise assurance. Sensitive admin paths use PAM with JIT elevation. Governance systems run access reviews and SoD checks. SIEM pipelines collect identity, policy, and privileged-session events.

### Cloud-native service architecture

Developers deploy workloads with platform-issued identities. A service mesh or gateway verifies mTLS and service policy. Fine-grained authorization is enforced at application or policy-engine level. Secrets are minimized in favor of ephemeral credentials. Observability systems correlate service identity, deployment metadata, and access decisions.

### AI-agent architecture

Agents receive task-bounded capabilities rather than ambient user privilege. Tool calls pass through policy checks. Memory is segmented by tenant and task class. High-risk actions require approval or cryptographic delegation. Decision logs capture user intent, delegated scope, selected tools, and outcome.

## Implementation and Operations

### What these architectures have in common

- explicit trust boundaries
- separate identity issuance from authorization decisions
- short-lived or revocable credentials
- centralized governance over distributed enforcement
- decision records that support reconstruction and containment

Reference architectures are most useful when adapted to local constraints such as regulatory burden, latency tolerance, and team maturity rather than copied mechanically.
