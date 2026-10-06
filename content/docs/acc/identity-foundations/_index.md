---
date: "2026-05-10T12:02:00+09:00"
title: "Identity Foundations"
weight: 2
prev: "/docs/acc"
next: "/docs/acc/identity-foundations/human-identity"
---

Identity foundations establish how people, workloads, machines, services, and other actors are recognized, verified, governed, and connected to accountable access decisions.

The first question is not only "Which protocol should we use?" but "What kind of thing are we identifying?" Human identity and non-human identity are different classes of identity subject, even though the underlying identity capabilities are often shared.

## Why identity matters

Identity is the foundation of accountability. It gives a system a recognizable subject to which authentication, permissions, actions, and review can be attached. Without a durable identity, there is no clear answer to who or what performed an action or which policy should apply.

An identity is not merely a username or a login flow. It is the representation of a subject that can be governed over time. That subject may be a person, a workload, a machine, a service, a device, or an AI agent. The mechanisms used to establish trust and control access may differ by subject, but the accountability problem remains the same.

## Identity subjects

The clearest way to organize this section is by the subject being identified.

### Human Identity

Human identity represents people, including workforce users, customers, partners, contractors, and privileged administrators. It usually involves account lifecycle, proofing, authentication, federation, MFA, provisioning, deprovisioning, and governance.

Human identity concerns are often anchored in business accountability. The question is not only whether someone can sign in, but whether the right person is granted the right permissions, under the right conditions, for the right period of time.

This is the domain covered in the human identity and enterprise IAM topic, which addresses lifecycle controls, access reviews, federation, and privileged access management.

### Non-Human Identity

Non-human identity represents workloads, machines, devices, services, and other automated actors. In many systems, these identities are issued and managed through runtime identity, workload attestation, short-lived credentials, certificates, keys, or service-to-service trust.

This includes:

- workload identities that run inside containers, VMs, or serverless runtimes
- machine and device identities used to represent endpoints or infrastructure components
- service identities used for application-to-application access
- AI agent identities, which are increasingly important as autonomous or semi-autonomous actors become part of the runtime environment

AI agents are not simply traditional service accounts. They are an emerging class of non-human identity whose actions may need to be attributable, constrained, and auditable even when they are delegated by a human or orchestrated by a system.

## Cross-cutting identity capabilities

Human and non-human identity share many operational concerns, even though the concrete mechanisms differ.

These are cross-cutting capabilities rather than separate identity architectures:

- authentication, or establishing confidence that the subject controls or represents the identity
- federation, or establishing trust and exchanging identity information across domains
- provisioning and deprovisioning, or creating and removing the identity and its access relationships
- credential and secret management, including rotation, revocation, and renewal
- lifecycle governance, including review, revalidation, and auditability
- authorization, or determining what the authenticated subject is allowed to do

The key distinction is this: human vs. non-human describes the identity subject; the other items describe the capabilities used to manage trust and access for that subject.

| Human Identity                                 | Non-Human Identity                                       |
| ---------------------------------------------- | -------------------------------------------------------- |
| People                                         | Workloads, machines, services, agents                    |
| Workforce and customer accounts                | Runtime and infrastructure identities                    |
| Passwords, passkeys, MFA, and session controls | Certificates, keys, short-lived credentials, attestation |
| SSO and federation across user-facing domains  | Service-to-service trust and workload identity patterns  |
| Provisioning, deprovisioning, privilege review | Registration, rotation, revocation, and runtime trust    |
| Human lifecycle and governance                 | Machine and runtime lifecycle governance                 |

The point of the comparison is conceptual clarity, not exhaustive completeness. The same identity discipline applies to both sides: establish the subject, prove control, bind trust, grant scope, and maintain accountability over time.

## Identity lifecycle

Both human and non-human identities move through lifecycle stages, although the mechanisms differ:

```text
Create / Enroll
      ↓
Establish Trust
      ↓
Authenticate
      ↓
Bind Attributes / Entitlements
      ↓
Use Identity
      ↓
Rotate / Revalidate
      ↓
Suspend / Revoke / Deprovision
```

Not every identity follows this flow in exactly the same way. A human workforce identity may be driven by HR or directory provisioning, while a workload identity may be issued at startup and rotated automatically. The pattern is the same: identities are created, bound to trust, used under policy, and later revoked or revalidated as conditions change.

## Identity and authorization

Identity and authorization are related but distinct concerns.

- Identity answers: "Who or what is acting?"
- Authorization answers: "What is it allowed to do?"

For a human identity, the answer is a person. For a non-human identity, it may be a workload, a machine, a service, or an agent. In either case, identification and authorization are separate layers: identity establishes the subject, while policy determines the allowed scope of action.

A common model is:

```text
Identity Subject
      ↓
Authentication / Proof of Control
      ↓
Attributes / Context
      ↓
Authorization Policy
      ↓
Access Decision
      ↓
Accountability / Audit
```

This is why a strong authentication mechanism does not automatically solve the broader governance problem. A system still needs policy, lifecycle controls, trust boundaries, and auditability to turn identity into safe, accountable access.

## How this section fits together

This section is a conceptual map for the child topics that follow:

- the Human Identity & Enterprise IAM topic covers people and enterprise access governance
- SSO & Federation explains user-facing trust and single sign-on patterns
- SCIM & Provisioning explains lifecycle synchronization and deprovisioning controls
- Workload, Machine, and Non-Human Identity covers runtime identity, machine trust, and automated actors

Taken together, these topics show that identity is not a single technology area. It is a set of patterns for representing subjects, establishing trust, governing lifecycle, and connecting those subjects to policy and accountability.

## Explore Identity Foundations

{{< cards >}}
{{< card link="human-identity/" title="Human Identity & Enterprise IAM" icon="users" subtitle="Lifecycle, federation, PAM, and governance" >}}
{{< card link="sso-federation/" title="SSO & Federation" icon="key" subtitle="User authentication, trust domains, and identity protocols" >}}
{{< card link="scim-provisioning/" title="SCIM & Provisioning" icon="switch-horizontal" subtitle="Lifecycle synchronization, entitlement hygiene, and deprovisioning" >}}
{{< card link="nonhuman-identity/" title="Workload, Machine, and Non-Human Identity" icon="server" subtitle="Dynamic runtime identity, credentials, and machine trust" >}}
{{< /cards >}}
