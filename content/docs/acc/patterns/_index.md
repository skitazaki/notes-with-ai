+++
date = '2026-05-10T13:30:00+09:00'
title = 'Architecture Patterns Catalog'
weight = 9
prev = '/docs/acc/governance'
next = '/docs/acc/threat-models'
+++

Architecture patterns are reusable answers to recurring enforcement and trust-distribution problems.

## Executive Summary

Patterns matter because access control usually fails at integration points rather than at the level of individual algorithms. Reusable patterns help teams reason about where policy lives, how decisions are propagated, and where trust assumptions become dangerous.

## Core Concepts

### Centralized authorization

A central policy service evaluates decisions for many applications. This improves consistency and governance, but introduces latency, availability, and policy-distribution concerns.

### Embedded authorization

Applications evaluate policy locally in process. This improves autonomy and local resilience, but can lead to policy drift if semantics are not standardized.

### Sidecar and service-mesh enforcement

A proxy or sidecar enforces identity and coarse policy close to the workload. This pattern is strong for service-to-service controls, mTLS, and uniform telemetry, but application-specific business authorization often still needs in-app logic.

### API-gateway enforcement

Gateways are effective for authentication, token validation, tenant routing, coarse rate control, and broad API policy. They should not become the only place where sensitive business authorization is implemented.

### Multi-tenant and B2B federation patterns

Shared platforms often need tenant isolation, delegated administration, external identity federation, and partner-specific policy overlays. ReBAC and scoped delegation become important here.

## Implementation and Operations

### Pattern selection criteria

- latency tolerance
- consistency requirements
- team autonomy model
- audit and explainability needs
- trust boundary placement
- operational maturity for policy rollout and rollback

### Tenant and partner federation operations

Multi-tenant and B2B federation patterns work best when tenant identity, partner identity, and platform operator identity remain distinct in both data model and policy evaluation. In practice that means tenant-scoped identifiers, issuer-aware claim mapping, delegated administration bounded to a tenant or partner boundary, and explicit handling for home-realm discovery plus partner onboarding.

ReBAC often becomes important because partner access is rarely a flat role lookup. Policies may need to express that a reseller can administer only customers they sponsor, that a supplier can view only purchase orders tied to its own legal entity, or that a tenant admin may invite users but not cross tenant boundaries.

### Practical recommendation

Most large systems end up hybrid: centralized policy semantics, distributed enforcement, and local application checks for business invariants. The important design choice is not purity. It is making the division of responsibility explicit.
