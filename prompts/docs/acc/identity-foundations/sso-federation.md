---
type: docs
path: /docs/acc/identity-foundations/sso-federation
---

Write a concise reference article roughly 1,200-1,600 words titled:
"SSO & Federation"

You are a senior identity architect and technical writer producing a practical, vendor-neutral article for security architects, platform engineers, and enterprise engineering teams.

Audience:

- Security architects
- IAM engineers
- Platform and application teams
- Enterprise architects
- Software engineers designing multi-app authentication

Purpose:

- Explain what SSO and federation are
- Clarify the difference between authentication, session continuity, and authorization
- Show how trust boundaries, identity providers, and relying parties fit together
- Provide durable conceptual guidance for designing enterprise identity flows

Scope:

- Focus on user-facing federation, identity protocols, trust models, and operating patterns
- Treat SSO as a user experience and trust model, not as a single protocol
- Include modern enterprise and SaaS patterns, but avoid product-specific marketing language

Tone & style:

- Neutral, explanatory, and precise
- Technical but readable for senior engineers and architects
- No hype, no vendor bias, no unsupported claims

Structure:

1. Executive Summary
2. Core concepts
   - principal, IdP, SP, federation, trust domain, session, assertion
3. Why SSO exists
   - reduced credential sprawl
   - stronger UX
   - centralized identity assurance
   - policy enforcement at identity layer
4. Federation protocols in practice
   - SAML for browser-based enterprise federation
   - OpenID Connect for modern web and mobile applications
   - OAuth 2.0 as authorization framework rather than user authentication by itself
   - when to use each and why the distinction matters
5. Design patterns
   - centralized IdP with multiple applications
   - partner and customer federation
   - external SaaS access with conditional access and MFA
   - step-up authentication and context-aware access
6. Operational realities
   - session lifetime and refresh patterns
   - logout and SLO expectations
   - identity propagation and attribute mapping
   - stale trust relationships and misconfigured federation
7. Governance and security controls
   - MFA, device trust, conditional access, phishing resistance, risk-based authentication
   - separation between authentication and authorization responsibilities
   - trust review and federation lifecycle management
8. Common anti-patterns
   - treating SSO as a universal solution for all access problems
   - using different protocols without clear ownership
   - mixing authentication and authorization responsibilities
   - reusing a single federation model across user types without boundary separation
9. Summary

Constraints:

- Do not frame SCIM as part of the live login flow; clearly distinguish it from SSO
- Do not collapse authentication into authorization or vice versa
- Do not treat session management as a minor detail; explain why it is central to secure federation
- Do not write a step-by-step implementation guide unless the section explicitly requires design tradeoffs
- Keep the article durable and referenceable for architecture reviews
