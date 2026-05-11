+++
date = '2026-05-10T12:30:00+09:00'
title = 'Human Identity & Enterprise IAM'
weight = 3
prev = '/docs/acc/landscape'
next = '/docs/acc/authorization-models'
+++

Human identity remains the foundation of enterprise access control because business accountability, approvals, and legal obligations are still anchored to people.

## Executive Summary

Enterprise IAM manages workforce and external-user identities from onboarding to offboarding. The design challenge is balancing usability and assurance across employees, contractors, partners, vendors, and customers, each of whom may require different proofing, federation, review, and privilege controls.

Mature IAM programs focus on lifecycle integrity rather than only login experience. The critical failure modes are not limited to weak authentication. They include stale entitlements, orphaned accounts, broken joiner-mover-leaver processes, excessive delegated administration, and privileged access that bypasses governance.

## Core Concepts

### Lifecycle management

Human access begins with identity proofing and authoritative source systems such as HR, partner records, or customer registration systems. Provisioning should follow these sources rather than becoming an independent manual process.

The core lifecycle includes:

- **Joiners**: create accounts, baseline roles, MFA enrollment, device registration
- **Movers**: adjust entitlements when team, geography, legal entity, or responsibility changes
- **Leavers**: revoke sessions, disable accounts, rotate shared credentials, transfer ownership

### Federation and access experience

SSO, SAML, OpenID Connect, SCIM, and directory synchronization reduce operational sprawl when designed around clear trust boundaries. Federation is most valuable when paired with strong session controls, MFA, conditional access, and risk-based step-up.

### Governance and privileged access

Not all permissions should be granted through ordinary role assignment. Sensitive capabilities often require:

- separation of duties constraints
- approval workflows
- time-bounded elevation
- session recording or command logging
- recurring access certification

PAM sits at the intersection of identity, approval, and runtime monitoring. It should not be treated as a disconnected vault product.

## Implementation and Operations

### Design patterns

- Use authoritative systems for lifecycle triggers.
- Keep role design stable at job-function level, not individual exception level.
- Prefer JIT provisioning or JIT elevation for sensitive systems.
- Make delegated administration scoped, auditable, and revocable.
- Align access reviews to risk, not only to calendar schedules.

### Federation protocols in practice

SSO is the user-facing outcome, not a single protocol. In enterprise deployments, SAML is still common for browser-based federation to SaaS, OpenID Connect is usually the better fit for modern web and mobile applications, and SCIM is used to provision and deprovision accounts rather than to authenticate a live session.

That separation matters operationally. A team may use SAML or OpenID Connect for sign-in, SCIM for lifecycle synchronization, and directory sync for group or attribute propagation. Incidents often occur when these responsibilities are blurred, for example when login succeeds but SCIM deprovisioning lags and leaves stale entitlements behind.

### Operating PAM as a control plane

Privileged Access Management (PAM) should be designed as a control plane for high-risk operations, not as a password locker alone. Effective PAM programs bind approval, JIT elevation, session recording, command logging, and revocation into one operating flow.

In practice, that means privileged paths should use separate identities or elevation workflows, short-lived access grants, and strong post-use review. Break-glass accounts may still exist for recovery, but they should remain isolated from day-to-day administration and be governed like emergency controls rather than convenience shortcuts.

### Common anti-patterns

- Manual spreadsheet-based provisioning
- Persistent administrator roles for operational convenience
- Group nesting so deep that effective permission review becomes impossible
- Contractor identities handled outside normal offboarding controls
- Customer identity and workforce identity combined without boundary separation

The objective is not frictionless access at any cost. It is fast, explainable, and revocable access grounded in business accountability.
