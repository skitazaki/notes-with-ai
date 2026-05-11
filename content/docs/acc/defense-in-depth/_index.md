+++
date = '2026-05-10T13:10:00+09:00'
title = 'Defense-in-Depth Architecture'
weight = 7
prev = '/docs/acc/ai-agents'
next = '/docs/acc/governance'
+++

Access control is strongest when identity and authorization are supported by surrounding controls that reduce the consequences of error, misuse, or compromise.

## Executive Summary

Defense in depth recognizes that no single control is sufficient. Authentication can be phished, policies can be misconfigured, tokens can be stolen, workloads can be compromised, and operators can make incorrect approvals. Layered security reduces blast radius by forcing attackers to cross multiple control domains.

For access control, those layers often include authentication strength, device trust, network segmentation, conditional access, runtime authorization, behavioral analytics, logging, and incident-response pathways.

## Core Concepts

### Layered enforcement

A high-risk request may encounter multiple gates:

1. identity proofing and MFA
2. device or workload trust evaluation
3. network and session policy
4. authorization policy for the requested action
5. anomaly detection and transaction monitoring
6. logging, alerting, and containment controls

Each layer answers a different question, and combining them prevents overloading authorization with responsibilities it cannot carry alone.

### Fail-open versus fail-closed

Critical systems must decide what happens when dependencies are unavailable. Fail-closed improves security but can harm availability. Fail-open protects continuity but can create severe exposure. The correct answer depends on business criticality, safety impact, and compensating controls.

### Break-glass access

Emergency access is necessary in real operations, but it must remain exceptional. Break-glass pathways need explicit scope, time limits, strong logging, retrospective review, and ideally out-of-band approval.

## Implementation and Operations

### Practical control stack

- strong authentication and phishing-resistant MFA
- device posture or workload attestation
- segmentation between user, service, and administrative paths
- contextual authorization at application and API layers
- runtime containment such as sandboxing and egress controls
- SIEM integration and response playbooks

### Operating break-glass safely

Break-glass access should use isolated identities, narrowly pre-defined scopes, and short expiration that is enforced automatically rather than by operator memory. The request path should capture who invoked it, why normal access was insufficient, which systems were touched, and whether out-of-band approval was obtained.

After use, the emergency grant should trigger immediate review, credential rotation where appropriate, and a root-cause check on why the standard control path failed. If break-glass becomes a frequent workflow, that is usually evidence that the normal access model or approval latency is broken.

### What to monitor

- unusual elevation or token issuance
- policy bypass attempts
- impossible travel or unusual geography for humans
- abnormal service-to-service call paths
- repeated denied actions followed by a successful privileged action

Defense in depth is effective only when the organization knows how alerts map back to identities, policies, and recovery actions.
