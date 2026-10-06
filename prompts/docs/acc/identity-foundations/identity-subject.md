---
type: docs
path: /docs/acc/identity-foundations
---

# Task: Strengthen the Identity Foundations hub with a Human vs. Non-Human Identity framing

Update the Identity Foundations hub page of the `notes-with-ai` Hugo documentation site.

## Goal

The current Identity Foundations hub introduces identity as covering people, workloads, machines, and other non-human actors, but it goes directly from that statement to a list of technology/topic pages.

Improve the conceptual framing by introducing a fundamental distinction between:

- **Human Identity**
- **Non-Human Identity**

This should become the first conceptual lens for understanding the Identity Foundations section.

The purpose is not to create two completely separate silos. Instead, explain that identity systems deal with different **identity subjects**, while capabilities such as authentication, federation, provisioning, credentials, lifecycle management, and authorization apply across those subjects in different ways.

The resulting page should help a reader answer:

> "What kind of thing are we identifying, and what identity mechanisms do we need to establish trust and accountability for it?"

## Proposed information architecture

Restructure the page around these concepts:

### 1. Identity as the foundation of accountability

Start with a concise introduction explaining that identity establishes a recognizable and governable subject to which authentication, permissions, actions, and accountability can be associated.

Emphasize that an identity subject may be:

- a person
- a workload
- a machine/device
- a service
- an AI agent
- another non-human actor

Avoid defining identity merely as "a username" or "authentication."

### 2. Identity Subjects

Introduce a prominent conceptual section:

**Identity Subjects**

Split it into two major categories.

#### Human Identity

Examples:

- Workforce identities
- Customer / external identities
- Privileged identities

Mention that human identity commonly involves:

- account lifecycle
- authentication
- SSO/federation
- provisioning/deprovisioning
- MFA
- privileged access
- governance

Link relevant existing pages where appropriate, especially:

- Human Identity & Enterprise IAM
- SSO & Federation
- SCIM & Provisioning

#### Non-Human Identity

Examples:

- Workload identities
- Machine/device identities
- Service identities
- AI agent identities

Mention that non-human identity commonly involves:

- workload/runtime identity
- machine identity
- certificates and keys
- short-lived credentials
- workload attestation
- credential rotation
- service-to-service authentication
- machine/agent trust

Link to the existing:

- Workload, Machine, and Non-Human Identity

Also make clear that AI agents are an emerging form of non-human identity rather than treating them as simply equivalent to traditional service accounts.

### 3. A cross-cutting identity lifecycle

After the Human vs. Non-Human comparison, introduce a second conceptual axis:

**Identity Lifecycle**

Explain that both human and non-human identities have lifecycle concerns, although the mechanisms differ.

Use a concise lifecycle such as:

```text
Create / Enroll
      ↓
Establish Trust
      ↓
Authenticate
      ↓
Provision / Bind Attributes
      ↓
Use Identity
      ↓
Rotate / Revalidate
      ↓
Suspend / Revoke / Deprovision
```

Do not imply that every identity follows exactly this sequence.

### 4. Identity → Authorization

End the conceptual introduction by showing how identity connects to access control:

```text
Identity Subject
      ↓
Identity / Authentication
      ↓
Attributes / Context
      ↓
Authorization Policy
      ↓
Access Decision
      ↓
Accountability / Audit
```

The key point should be:

> Identity answers "who or what is acting?" while authorization answers "what is it allowed to do?"

For non-human identities, "who" should naturally be understood as "which workload, machine, service, or agent."

## Recommended visual presentation

Use a clear, modern documentation layout consistent with the existing site.

Prefer a conceptual two-column comparison near the top:

| Human Identity                | Non-Human Identity                              |
| ----------------------------- | ----------------------------------------------- |
| People                        | Workloads, machines, services, agents           |
| Workforce / customer accounts | Runtime / workload identities                   |
| Passwords, passkeys, MFA      | Certificates, keys, workload credentials        |
| SSO / federation              | Workload federation / identity federation       |
| Provisioning / deprovisioning | Registration / issuance / rotation / revocation |
| Human lifecycle               | Runtime / machine lifecycle                     |
| Privileged users              | Privileged workloads / service identities       |

Do not overfill the table. The point is to establish the conceptual distinction, not create a complete comparison matrix.

If the site's existing design system has suitable cards, callouts, diagrams, tabs, or Mermaid support, reuse those mechanisms rather than introducing a new visual framework.

## Important conceptual nuance

Do NOT present "human" and "non-human" as completely independent identity architectures.

Make the following distinction explicit:

**Human vs. non-human is a classification of the identity subject.**

Other concerns are cross-cutting dimensions:

- lifecycle
- authentication
- federation
- credentials
- trust
- provisioning
- authorization
- governance
- auditability

For example:

```text
                    Identity Subject
                    /              \
               Human              Non-Human
                 |                    |
          +------+------+      +------+------+
          |      |      |      |      |      |
       Auth   Lifecycle Trust  Auth Lifecycle Trust
          \      |      /      \      |      /
           \     |     /        \     |     /
              Authorization & Accountability
```

This conceptual model is more important than adding lots of prose.

## Relationship to the existing child pages

Preserve the existing child-page structure and URLs.

The current child topics are:

1. Human Identity & Enterprise IAM
2. SSO & Federation
3. SCIM & Provisioning
4. Workload, Machine, and Non-Human Identity

Do not rename or relocate these pages unless there is a compelling reason.

Instead, make the hub page explain how they fit together.

A possible mapping:

```text
Identity Foundations
│
├── Identity Subjects
│   ├── Human
│   │   └── Human Identity & Enterprise IAM
│   │
│   └── Non-Human
│       └── Workload, Machine, and Non-Human Identity
│
├── Cross-Cutting Identity Capabilities
│   ├── SSO & Federation
│   └── SCIM & Provisioning
│
└── Identity → Authorization
```

Do not force this exact hierarchy into the site's navigation if the current Hugo navigation structure does not support it cleanly. This is primarily a conceptual model for the hub page.

## Content style

Match the existing `notes-with-ai` documentation style.

The site is technical documentation, so:

- concise
- architecture-oriented
- precise terminology
- explanatory rather than marketing-oriented
- avoid unnecessary vendor-specific terminology
- prefer concepts over product names
- use examples where they clarify the model

Do not make the page substantially longer just for the sake of length.

The goal is to make the conceptual model clearer, not to duplicate the detailed content of the child pages.

## Terminology

Use these terms carefully:

- **Identity subject** — the person, workload, machine, service, or agent represented by an identity.
- **Human identity** — identity representing a person.
- **Non-human identity** — identity representing a workload, machine/device, service, agent, or other automated actor.
- **Authentication** — establishing confidence that an actor controls or represents an identity.
- **Authorization** — determining what an authenticated identity is permitted to do.
- **Federation** — establishing trust and exchanging identity/authentication information across security domains.
- **Provisioning** — creating, updating, associating, and removing identities or their access-related information.

Avoid treating "identity" and "authentication" as synonyms.

## AI agents

Include AI agents briefly as an emerging non-human identity case.

The important conceptual point is that an AI agent may need an identity that is:

- independently attributable
- bound to an owner or accountable principal
- constrained by authorization policy
- represented distinctly from the human who initiated it
- auditable across its actions

Do not turn this hub page into a detailed AI-agent security page. The existing AI & Emerging Systems section should remain the place for deeper treatment.

## Implementation requirements

1. Inspect the repository and identify the source file for the Identity Foundations hub.
2. Inspect nearby Access Control hub/child pages to match the site's existing Markdown/front matter/component conventions.
3. Inspect the current theme/components before introducing new HTML or CSS.
4. Modify only what is necessary.
5. Preserve existing navigation and URLs.
6. Reuse existing components/styles wherever possible.
7. Keep the page responsive and readable on mobile.
8. Ensure all internal links use the site's existing link conventions.
9. Run the appropriate Hugo build/check commands.
10. Check for broken internal links or malformed front matter.
11. If possible, render/preview the page and verify that the new Human vs. Non-Human framing is visually clear.

## Acceptance criteria

The task is complete when:

- The Identity Foundations page clearly establishes **Human Identity vs. Non-Human Identity** as the fundamental classification of identity subjects.
- The distinction appears before the detailed topic navigation.
- The page explains that lifecycle, authentication, federation, provisioning, trust, authorization, and governance are cross-cutting concerns.
- Existing child pages remain discoverable and correctly linked.
- The distinction between identity and authentication is clear.
- AI agents are acknowledged as an emerging non-human identity category without dominating the page.
- The page visually communicates the model rather than presenting it as a large block of prose.
- The page remains consistent with the existing site's design language.
- No existing URLs are broken.
- Hugo builds successfully.

## Deliverable

Implement the changes directly in the repository.

At the end, report:

1. Files changed
2. Summary of the conceptual/content changes
3. Any new components/styles introduced
4. Validation/build commands run
5. Any remaining concerns or suggested follow-up work
