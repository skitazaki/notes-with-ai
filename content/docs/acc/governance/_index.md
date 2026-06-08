---
date: "2026-05-10T13:20:00+09:00"
title: "Governance, Compliance & Auditability"
weight: 8
prev: "/docs/acc/defense-in-depth"
next: "/docs/acc/patterns"
---

Access control becomes trustworthy at organizational scale only when permissions, policies, and exceptions are governable, explainable, and reviewable over time.

## Executive Summary

Governance is the discipline that connects technical authorization with institutional accountability. It addresses who may approve access, how entitlements are reviewed, how policy changes are tested, and how evidence is produced for auditors, regulators, customers, and internal risk functions.

Compliance frameworks such as SOC 2, ISO 27001, HIPAA, PCI DSS, and GDPR do not prescribe one architecture, but they do require demonstrable control over access, least privilege, evidence, and incident handling.

## Core Concepts

### Entitlement governance

Permissions must have an owner, purpose, review path, and revocation path. Entitlements without ownership tend to accumulate until they become unreviewable.

Strong governance typically includes:

- access request and approval workflows
- periodic access certification
- segregation-of-duties rules
- policy exception handling
- privileged-access review

### Auditability and explainability

An audit log is not enough if it records events without meaning. Effective auditability requires the ability to reconstruct:

- which principal acted
- which resource and action were involved
- which policy or approval allowed it
- what context influenced the decision
- what changed afterward

### Policy testing and evidence

Policy changes should be testable before rollout. Evidence should be generated as a side effect of normal operations rather than assembled manually during audits.

## Implementation and Operations

### Operating model

- define policy owners and entitlement owners separately when necessary
- classify systems and permissions by criticality
- set review frequency based on risk
- keep immutable or tamper-evident decision records where regulation requires it
- map controls to regulatory obligations without making regulation the architecture driver

### Common failure modes

- audits based on screenshots and email threads
- policy changes deployed without simulation or regression checks
- exceptions granted permanently because temporary paths are unavailable
- no distinction between business approver and technical implementer
- logs present but impossible to correlate across systems

Good governance reduces not only audit pain, but also the mean time to understand and contain access-related incidents.
