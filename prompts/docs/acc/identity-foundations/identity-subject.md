---
type: docs
path: /docs/acc/identity-foundations
---

Write a concise reference article roughly 1,200-1,600 words titled:
"Identity Foundations"

You are a senior identity architect and technical writer creating a durable, vendor-neutral hub page for security architects, platform engineers, IAM teams, and application owners.

Audience:

- Security architects
- IAM engineers
- Platform and application teams
- Engineering leaders
- Governance and access review teams

Purpose:

- Explain why identity is the foundation of trust, accountability, and access
- Introduce the distinction between human and non-human identity subjects
- Show how common identity capabilities apply across subjects in different ways
- Frame the rest of the Identity Foundations section and its child pages

Scope:

- Focus on conceptual framing, not protocol implementation detail
- Cover identity subjects, lifecycle, authentication, credentials, trust, provisioning, and authorization as connected concerns
- Include AI agents as an emerging non-human identity class without treating them as a separate architecture silo
- Preserve the existing child-page structure and URLs

Tone & style:

- Neutral, explanatory, and precise
- Architecture-oriented and durable
- Clear enough for senior engineers and architects
- No hype, no vendor bias, no marketing language

Structure:

1. Executive Summary
2. Why identity matters
   - identity as the foundation of accountability
   - identity subject as the thing being recognized and governed
   - distinction between subject and mechanism
3. Identity subjects
   - Human Identity
   - Non-Human Identity
   - examples of people, workloads, machines, services, and AI agents
4. Cross-cutting identity capabilities
   - authentication
   - federation
   - provisioning and deprovisioning
   - credential management and rotation
   - lifecycle governance and auditability
5. Identity lifecycle
   - create or enroll
   - establish trust
   - authenticate
   - bind attributes and permissions
   - use the identity
   - rotate, revalidate, revoke, and deprovision
6. Identity and authorization
   - identity answers who or what is acting
   - authorization answers what it is allowed to do
   - how this applies to human and non-human subjects
7. Relationship to the existing child pages
   - Human Identity & Enterprise IAM
   - SSO & Federation
   - SCIM & Provisioning
   - Workload, Machine, and Non-Human Identity
8. Summary

Constraints:

- Do not define identity as only a username or only authentication
- Do not present human and non-human identity as two completely separate silos; they are two classes of identity subject
- Make the subject-versus-capability distinction explicit throughout the article
- Keep the article concise and conceptual, not a large comparison matrix
- Maintain the current child-page URLs and organization; do not rename or relocate pages unless there is a clear reason
- Explain that AI agents are an emerging form of non-human identity, not simply traditional service accounts
- Avoid implementation recipes, vendor-specific framing, and over-detailed product references
- Keep the writing durable, referenceable, and suitable for architecture reviews

- Use examples where they clarify the model
- Keep the article from becoming a detailed child-page duplication
- Keep the focus on the conceptual model that makes the rest of the section legible
