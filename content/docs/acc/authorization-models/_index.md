+++
date = '2026-05-10T12:40:00+09:00'
title = 'Authorization Models & Policy Systems'
weight = 4
prev = '/docs/acc/human-identity'
next = '/docs/acc/workload-identity'
+++

Authorization determines whether an authenticated principal may perform a specific action on a specific resource in a specific context.

## Executive Summary

No single authorization model fits every environment. The practical problem is mapping organizational semantics to enforceable decisions while preserving scalability, auditability, and developer usability.

Classical models such as DAC and MAC still matter conceptually, but modern enterprise systems more often combine RBAC, ABAC, ReBAC, and policy-as-code. The most robust architectures use multiple layers: stable coarse-grained roles, contextual evaluation at runtime, and explicit policy engines for sensitive or shared platforms.

## Core Concepts

### Model overview

- **DAC (Discretionary Access Control)**: resource owners grant access. Useful in collaborative systems, weak for centralized governance.
- **MAC (Mandatory Access Control)**: labels and clearance levels are centrally enforced. Strong for regulated environments, rigid for fast-changing business systems.
- **RBAC (Role-Based Access Control)**: permissions map to roles, roles map to principals. Easy to explain, vulnerable to role explosion.
- **ABAC (Attribute-Based Access Control)**: decisions use attributes about subject, resource, action, and environment. Flexible, but policy sprawl is a risk.
- **ReBAC (Relationship-Based Access Control)**: access depends on graph relationships such as owner, viewer, approver, or team member. Strong for collaborative and multi-tenant products.
- **PBAC (Policy-Based Access Control)**: policy logic is expressed in a dedicated system or language and evaluated independently of application code.

### RBAC versus ABAC

RBAC is operationally attractive when responsibilities are stable. It becomes brittle when every exception requires a new role. ABAC handles dynamic conditions such as geography, device posture, transaction value, tenant classification, or time window, but can become hard to reason about when attributes and policies proliferate.

The tradeoff is not simply static versus dynamic. It is administrative simplicity versus decision precision.

### Entitlement versus capability

Entitlements and capabilities are related, but they are not interchangeable.

An **entitlement** is a granted permission structure within an administrative model. It often appears as a role assignment, group membership, policy grant, or standing permission that tells the system what a principal is generally allowed to do. Entitlements are useful for durable operating models because they align with organization structure, job function, ownership, and review workflows.

A **capability** is a bounded authority to perform a specific operation under specific conditions. It is often narrower, more contextual, and more suitable for delegation than a standing entitlement. Capabilities are frequently scoped by resource, time window, tool, transaction type, or task boundary.

In practice, the distinction often looks like this:

- **Entitlement**: "Alice belongs to the finance-approver role."
- **Capability**: "This agent may approve invoice 12345 for the next 10 minutes using only the payment-review tool."

That difference matters architecturally:

- Entitlements are usually designed for administration, review, and long-lived governance.
- Capabilities are usually designed for execution, delegation, and tight blast-radius control.
- Entitlements answer what a principal is broadly allowed to do.
- Capabilities answer what this principal may do right now, on this target, within these limits.

Systems often need both. An entitlement may establish the baseline authority to request or receive a capability, while the capability constrains the actual runtime action. This pattern is especially important for privileged operations, workflow approvals, service-to-service calls, and AI-agent delegation.

### Policy engines and evaluation flow

Modern policy systems often separate:

1. **Policy authoring**
2. **Policy distribution**
3. **Decision evaluation**
4. **Enforcement**
5. **Decision logging and explanation**

Technologies such as OPA, Cedar, Zanzibar-inspired graph systems, and XACML-style engines differ in syntax and deployment model, but they all face the same architectural concerns: latency, caching, consistency, policy rollout safety, and explainability.

## Implementation and Operations

### Practical guidance

- Use RBAC for stable baseline entitlements.
- Add ABAC for runtime conditions that should not create new permanent roles.
- Use ReBAC for sharing, delegation, and graph-shaped collaboration semantics.
- Keep policy code versioned, tested, and reviewable like application code.
- Design for explicit deny semantics where risk requires clear conflict resolution.

### Scaling concerns

At scale, the hard parts are usually not syntax. They are data freshness, cache invalidation, relationship graph consistency, and explaining why two similar requests produced different results.

A useful benchmark for maturity is whether teams can test authorization logic before deployment and replay historical decisions during incident analysis.
