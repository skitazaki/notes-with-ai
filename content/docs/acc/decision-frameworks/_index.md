+++
date = '2026-05-10T13:50:00+09:00'
title = 'Decision Frameworks & Tradeoffs'
weight = 11
prev = '/docs/acc/threat-models'
next = '/docs/acc/reference-architectures'
+++

Good access-control design depends less on universal best practices than on explicit tradeoff management.

## Executive Summary

Architectural choices such as RBAC versus ABAC, JWT versus opaque tokens, centralized versus decentralized authorization, or long-lived versus ephemeral credentials each optimize for different operational realities. Teams make poor decisions when they compare only feature lists. The right comparison includes scalability, failure modes, governance cost, migration burden, and the shape of the trust boundaries involved.

## Core Concepts

### Typical decision pairs

- **RBAC vs ABAC**: stable administration versus dynamic precision
- **Centralized vs decentralized authorization**: consistency versus local autonomy
- **JWT vs opaque tokens**: local verification versus stronger server-side revocation control
- **Static vs continuous authorization**: lower runtime cost versus better adaptation to changing risk
- **Long-lived vs ephemeral credentials**: operational convenience versus containment and attribution

### Questions to ask

1. What must be explained to auditors, operators, and developers?
2. What data must be fresh at decision time?
3. Which failures are acceptable: latency, inconsistency, or reduced availability?
4. Who owns policy semantics and rollout safety?
5. How difficult is migration if the first model proves insufficient?

## Implementation and Operations

### Decision heuristics

- Prefer the simplest model that still matches the trust boundary.
- Add dynamism only when the underlying risk actually changes at runtime.
- Avoid distributing policy logic to every team unless semantic drift is tolerable.
- Prefer reversible migration paths, such as adding contextual checks around existing RBAC.
- Measure operational cost, not just theoretical expressiveness.

### JWT versus opaque token operating model

JWTs work well when many services need to verify tokens locally with low latency and limited dependence on a central introspection service. The tradeoff is that revocation, claim minimization, signing-key rotation, and audience discipline become critical because the token may be accepted by many components without a callback.

Opaque tokens shift more control back to the authorization server or gateway because the token has little meaning without introspection or lookup. That improves server-side revocation and claim changes, but it adds a dependency on online validation, cache policy, and failure handling. Many large systems therefore use JWTs at the edge for scale and opaque or reference tokens for higher-risk internal delegation paths.

Tradeoff documents are valuable because they preserve architectural intent. When teams understand why a choice was made, they are less likely to erode it through ad hoc exceptions.
