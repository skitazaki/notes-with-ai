+++
date = '2026-05-10T12:50:00+09:00'
title = 'Workload & Machine Identity'
weight = 5
prev = '/docs/acc/authorization-models'
next = '/docs/acc/ai-agents'
+++

Machine identity is now one of the fastest-growing parts of access-control architecture because modern systems contain far more services, workloads, pipelines, and devices than human operators.

## Executive Summary

Workload identity answers a foundational trust question: how does one machine know what another machine is, and under what conditions should it trust it? Traditional answers relied heavily on static secrets and long-lived service accounts. Modern answers favor attestation, short-lived credentials, certificate-based identity, and tightly scoped service-to-service authorization.

This domain spans Kubernetes, serverless platforms, CI/CD pipelines, APIs, service meshes, robotic automation, and IoT fleets. The security challenge is not only authenticating workloads. It is ensuring those workloads receive the minimum identity and capability required for their runtime role.

## Core Concepts

### Identity forms

Machine identity commonly appears as:

- service accounts and cloud roles
- X.509 certificates and mTLS identities
- OIDC or OAuth tokens for workload federation
- signed workload attestations
- hardware-backed device identities

### Why static secrets fail

Long-lived shared secrets create large blast radius, weak attribution, and difficult rotation. They also obscure which workload is acting because multiple services may present the same credential.

Short-lived, automatically issued credentials improve containment and observability when combined with attestation, rotation, and policy checks tied to workload metadata.

### SPIFFE, SPIRE, and workload trust

Frameworks such as SPIFFE/SPIRE formalize workload identity using standardized identifiers and issuance workflows. The architectural value is not only interoperability. It is the explicit binding of identity to a verifiable workload context.

## Implementation and Operations

### Recommended patterns

- Use federated workload identity where cloud platforms support it.
- Replace broad service accounts with narrowly scoped runtime identities.
- Bind identities to platform evidence such as pod, namespace, cluster, image signature, or build provenance.
- Separate authentication of the workload from authorization of its actions.
- Rotate credentials automatically and monitor issuance anomalies.

### High-risk areas

- CI/CD systems with broad production credentials
- Shared robot or batch identities reused across business processes
- API clients with non-expiring tokens
- Kubernetes service accounts mounted into over-privileged workloads
- Device fleets without revocation or attestation support

The operational goal is to turn machine trust from a secret-distribution problem into an identity-and-policy problem.
