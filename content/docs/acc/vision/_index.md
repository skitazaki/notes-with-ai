---
date: "2026-05-10T12:10:00+09:00"
title: "Vision & Principles"
weight: 1
prev: "/docs/acc"
next: "/docs/acc/landscape"
---

Access control is no longer a narrow authorization concern at the edge of an application. It is a system-wide discipline for continuously establishing trustworthy intent between principals, resources, policies, and execution environments.

## Executive Summary

Modern environments are distributed, API-driven, and increasingly autonomous. A user session may trigger actions across SaaS applications, internal APIs, cloud services, data platforms, and AI-assisted workflows. In that environment, perimeter assumptions fail quickly. Identity, policy, and telemetry become the durable control plane.

An effective access-control strategy is guided by several principles:

- **Identity-centric security** treats humans, workloads, and agents as first-class principals.
- **Least privilege** limits standing access and narrows blast radius.
- **Continuous verification** assumes context can change after authentication.
- **Policy-driven architecture** separates decision logic from application code where it improves consistency and governance.
- **Defense in depth** assumes every control can fail and therefore layers compensating controls.

## Core Concepts

### Zero Trust as an operating assumption

Zero Trust does not mean that nothing is trusted. It means trust is not inherited from network location or historical presence alone. Each request should be evaluated using available evidence such as identity, device posture, workload attestation, session risk, environmental context, and requested action.

### Identity classes

Most organizations now operate at least three identity classes:

- **Human identities** for employees, contractors, partners, and customers
- **Machine identities** for services, workloads, pipelines, devices, and APIs
- **Agent identities** for AI systems acting through delegated tools and bounded tasks

The architectural mistake is to secure these domains independently. A modern strategy treats them as separate principal types within one trust model.

### Trust boundaries and policy domains

Access-control architecture is strongest when trust boundaries are explicit. Common boundaries include tenant boundaries, network zones, control-plane versus data-plane operations, production versus development, and human-approved versus autonomous actions.

Policies should align to these boundaries. A policy model that ignores them tends to collapse into broad roles, opaque exceptions, and fragile manual review.

## Implementation and Operations

### Design principles for teams

- Prefer short-lived credentials over long-lived secrets.
- Prefer explicit delegation over credential sharing.
- Prefer centrally governed policy semantics even when enforcement is distributed.
- Prefer explainable decisions over black-box authorization.
- Prefer revocable capabilities over broad ambient privilege.

### What success looks like

An organization with mature access control can answer five operational questions quickly:

1. Who or what performed this action?
2. Why was it allowed?
3. Which policy granted the capability?
4. What is the blast radius if the principal is compromised?
5. How can the permission be revoked or constrained immediately?

If those answers require manual investigation across disconnected systems, the problem is architectural rather than procedural.
