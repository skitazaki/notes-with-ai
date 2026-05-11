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

Workload trust is the idea that a system should trust a running software entity because it can prove what it is, not merely because it sits on a familiar network segment. That distinction matters in Kubernetes, multi-cloud, and auto-scaling environments where IP addresses, hosts, and runtime placement change constantly.

SPIFFE, the Secure Production Identity Framework For Everyone, is the specification layer. It standardizes how workload identity is represented, most visibly through the SPIFFE ID URI format such as `spiffe://company.internal/payments/api`. The role of the identifier is similar to a login identifier for a human, except that it names a service, workload, or runtime identity inside a trust domain.

SPIRE, the SPIFFE Runtime Environment, is the reference implementation that makes this practical. It attests nodes and workloads, decides whether a workload really is what it claims to be, and then issues short-lived identity documents. Those documents are usually X.509 SVIDs for mTLS or JWT-SVIDs for token-based cases, where SVID means SPIFFE Verifiable Identity Document.

In practice, the flow looks like this: a pod or service starts, SPIRE verifies runtime evidence such as node, namespace, service account, or platform metadata, assigns a SPIFFE ID, and rotates short-lived credentials for the workload. Other services can then authenticate that workload cryptographically and make authorization decisions based on identity instead of IP location.

This is why SPIFFE/SPIRE shows up frequently in zero-trust architectures, service meshes, and Kubernetes security designs. Systems such as Istio often rely on SPIFFE-form identities internally, which makes SPIFFE less of a niche feature and more of a general identity foundation for machine-to-machine trust.

Official references: [SPIFFE home](https://spiffe.io/), [SPIFFE overview and specifications](https://spiffe.io/docs/latest/spiffe-about/overview/), [SPIRE project](https://spiffe.io/spire/).

## Implementation and Operations

### Recommended patterns

- Use federated workload identity where cloud platforms support it.
- Replace broad service accounts with narrowly scoped runtime identities.
- Bind identities to platform evidence such as pod, namespace, cluster, image signature, or build provenance.
- Separate authentication of the workload from authorization of its actions.
- Rotate credentials automatically and monitor issuance anomalies.

### SPIFFE and federation deployment choices

SPIFFE and SPIRE are most useful when teams need portable workload identity across clusters, runtimes, or platforms instead of relying only on platform-specific service-account semantics. The strongest deployment pattern is to bind issuance to attestation evidence and keep credentials short-lived enough that compromise windows stay narrow.

Workload federation can also use OIDC or OAuth tokens rather than certificates, especially when one cloud or CI system needs to assume identity in another environment. The operational question is less "certificate versus token" than whether issuance is short-lived, audience-bound, and tied to verifiable runtime evidence. In environments that already use a service mesh, SPIFFE-compatible identities often become the common layer that allows mTLS, policy checks, and telemetry correlation to line up.

### High-risk areas

- CI/CD systems with broad production credentials
- Shared robot or batch identities reused across business processes
- API clients with non-expiring tokens
- Kubernetes service accounts mounted into over-privileged workloads
- Device fleets without revocation or attestation support

The operational goal is to turn machine trust from a secret-distribution problem into an identity-and-policy problem.
