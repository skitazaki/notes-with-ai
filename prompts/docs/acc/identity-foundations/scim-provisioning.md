---
type: docs
path: /docs/acc/identity-foundations/scim-provisioning
---

Write a concise reference article roughly 1,200-1,600 words titled:
"SCIM & Provisioning"

You are a senior identity architect and technical writer producing a practical, vendor-neutral article for security architects, platform engineers, IAM teams, and application owners.

Audience:

- IAM engineers
- Security architects
- Platform teams
- Application owners
- Governance and access review teams

Purpose:

- Explain what SCIM is and why provisioning matters
- Clarify how lifecycle management differs from authentication and federation
- Show how account creation, updates, deprovisioning, and group membership drive access hygiene
- Provide a durable architecture view of identity lifecycle operations

Scope:

- Focus on the lifecycle control plane: provisioning, synchronization, deprovisioning, reconciliation, and group propagation
- Explain SCIM as a standard for account lifecycle operations, not as an authentication protocol
- Include enterprise identity platform patterns, SaaS onboarding, and access hygiene concerns

Tone & style:

- Neutral, explanatory, and precise
- Operationally grounded, with clear security implications
- No hype or product-driven framing

Structure:

1. Executive Summary
2. Core concepts
   - provisioning, deprovisioning, reconciliation, identity lifecycle, authoritative source, group membership, attribute mapping
3. Why provisioning is a control problem
   - stale accounts
   - orphaned access
   - privilege drift
   - governance failure in joiner-mover-leaver processes
4. SCIM as a provisioning standard
   - what SCIM does well
   - how it complements SAML and OpenID Connect
   - boundaries between federation and provisioning
   - why live session authentication and lifecycle management are separate concerns
5. Common provisioning patterns
   - HR-driven provisioning to enterprise apps
   - directory sync and group propagation
   - SaaS onboarding and contractor management
   - JIT assignment versus static assignment
   - reconciliation loops and drift detection
6. Deprovisioning and access hygiene
   - revocation timing
   - group removal and entitlement cleanup
   - session invalidation and token handling
   - handling exceptions and delayed removal
7. Governance and operational controls
   - access reviews and certifications
   - change auditability
   - authoritative source ownership
   - monitoring for failed provisioning events
8. Design tradeoffs
   - push vs pull, event-driven vs periodic reconciliation, centralized vs application-owned provisioning
   - attribute mapping complexity
   - role and group model stability
   - handling external identities and partner accounts
9. Common anti-patterns
   - manual provisioning by spreadsheets or support tickets
   - deprovisioning treated as a low-priority task
   - group membership drift hidden by downstream app configuration
   - mixing lifecycle events with application authorization logic
   - assuming SSO success implies access is correctly managed
10. Summary

Constraints:

- Keep the article centered on lifecycle and provisioning, not authentication or token issuance
- Make the separation from SSO explicit throughout the article
- Explain why correct deprovisioning is often more important than a smooth login flow
- Avoid implementation recipes that are too product-specific or too vague to be useful in architecture reviews
- Keep the writing durable, referenceable, and oriented around secure access governance
