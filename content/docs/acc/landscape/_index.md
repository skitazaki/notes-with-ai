+++
date = '2026-05-10T12:20:00+09:00'
title = 'Landscape Overview'
weight = 2
prev = '/docs/acc/vision'
next = '/docs/acc/human-identity'
+++

The access-control landscape is best understood as an ecosystem of interacting systems rather than a single product category.

## Executive Summary

At minimum, a modern architecture spans identity proofing, authentication, authorization, credential issuance, enforcement points, telemetry, governance, and recovery workflows. Enterprises often implement these functions using multiple systems: identity providers, directories, federation brokers, policy engines, PAM tools, secret managers, certificate authorities, workload identity platforms, API gateways, and SIEM pipelines.

The core design task is not choosing a single control. It is defining how these systems cooperate without producing inconsistent decisions or operational dead zones.

## Core Concepts

### The main control domains

- **Identity providers and directories** establish who the principal is.
- **Federation systems** let one trust domain accept assertions from another.
- **Authentication factors** raise confidence in the asserted identity.
- **Authorization systems** decide whether a requested action is permitted.
- **Credential systems** issue tokens, certificates, and keys.
- **Enforcement points** apply those decisions at applications, gateways, sidecars, and infrastructure boundaries.
- **Governance systems** review, certify, and revoke entitlements.
- **Observability systems** record decisions and detect misuse.

### Authorization model taxonomy

Different models optimize for different environments:

- **DAC** favors owner discretion and simplicity.
- **MAC** favors centrally imposed classification and strict hierarchy.
- **RBAC** favors administratively stable job-function mapping.
- **ABAC** favors contextual and dynamic decisions.
- **ReBAC** favors graph-shaped collaboration and sharing models.
- **PBAC** favors decoupled policy expression and programmable governance.

These models are not mutually exclusive. A single system may use RBAC for coarse entitlement, ABAC for runtime context, and ReBAC for sharing semantics.

### Why the ecosystem keeps expanding

Two forces drive complexity. First, distributed systems create more non-human identities than human users. Second, AI-assisted and event-driven workflows create requests that are no longer initiated directly by a logged-in human. The landscape therefore expands from workforce IAM to full trust-orchestration.

## Implementation and Operations

### A practical mental model

Think in four layers:

1. **Identity layer**: proofing, lifecycle, authentication, federation
2. **Decision layer**: policies, roles, attributes, relationships, risk signals
3. **Enforcement layer**: application, gateway, mesh, database, SaaS, runtime
4. **Governance layer**: review, audit, testing, exception handling, incident response

### Common integration mistakes

- Treating token issuance as equivalent to authorization
- Assuming authentication strength automatically implies resource entitlement
- Centralizing policy semantics but leaving exception handling undocumented
- Building machine identity outside the enterprise trust model
- Adding AI agents before defining delegation and approval boundaries

The rest of this library examines each of these domains in depth.
