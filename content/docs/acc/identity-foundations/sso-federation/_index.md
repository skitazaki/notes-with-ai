---
date: "2026-09-26T22:56:00+09:00"
title: "SSO & Federation"
aliases: ["/docs/acc/sso-federation/"]
weight: 2
prev: "/docs/acc/identity-foundations/human-identity"
next: "/docs/acc/identity-foundations/scim-provisioning"
---

Single sign-on and federation are the mechanisms that let users prove their identity once and then use that identity across multiple applications and trust domains without creating a separate password, credential, or account model for each system.

## Executive Summary

SSO is often described as a user convenience feature, but in enterprise architecture it is a trust and governance control. It reduces password sprawl, centralizes identity proofing and strong authentication, and makes risky access decisions easier to monitor. Federation extends that property across organizational boundaries so that one trust domain can accept an identity assertion from another and apply its own policy decisions.

At the architectural level, the critical distinction is between authentication and authorization. Authentication answers the question, "Who are you?" Federation and SSO are primarily about establishing and propagating that identity across systems. Authorization answers, "What may you do?" That distinction matters because teams often blur these responsibilities and end up treating SSO as if it automatically solves access governance.

Modern SSO deployments usually involve an identity provider (IdP), a relying party (SP or application), an authentication protocol, and a session model. Common patterns include SAML for enterprise browser federation, OpenID Connect for modern web and mobile apps, and OAuth 2.0 for delegated authorization. Each has a different role in the overall access-control architecture, and the real design choice is not which protocol is "best" in the abstract. It is which protocol fits the trust model, user experience, and governance needs of the environment.

## Core Concepts

### Basic trust model

An identity system is easiest to reason about when it separates the following roles:

- **Principal**: the user or actor being identified
- **Identity provider (IdP)**: the authority that verifies and asserts identity
- **Relying party (SP)**: the application or service that accepts the identity assertion and decides whether to grant access
- **Trust domain**: the security boundary in which identity rules and governance are defined
- **Assertion**: the statement that a user has authenticated and includes identity attributes or claims
- **Session**: the period during which the user is assumed to remain authenticated and authorized within a boundary

This model is why federation is governance, not just convenience. The relying party does not need to own the user's password or proofing process. It only needs to trust the IdP's evidence and apply its own local policy and risk controls.

### Why SSO exists

The strongest reason to adopt SSO is not a smoother login experience alone. It is the reduction of identity sprawl and the increase in control over how identity is verified. Without SSO, every application typically implements its own credential model, password reset flow, MFA policy, and lifecycle process. This creates operational drift, inconsistent assurance, and higher risk.

SSO centralizes several important control functions:

- consistent identity proofing and credential policy
- centralized MFA and step-up challenges
- broader observability of authentication events
- easier enforcement of conditional access
- clearer ownership of user identity governance

This is why organizations often use SSO as the user-facing access layer while leaving authorization rules to the application, policy engine, or service layer. The identity platform authenticates the user; the application still decides what that user may do.

## Federation protocols in practice

### SAML

[SAML](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf) remains common in enterprise environments, especially where browser-based SaaS applications, legacy enterprise apps, or tightly managed corporate identity flows need a standards-based federation protocol. It is widely used for enterprise-to-SaaS sign-in and for providers that have a mature federation model.

SAML's strength is the maturity of enterprise trust patterns. It fits well when organizations want strong, explicit trust relationships and a widely understood web SSO model. Its downside is that it can be verbose and less ergonomic for modern mobile or API-centric architectures compared with OIDC-based flows.

### OpenID Connect (OIDC)

[OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html) is usually a better fit for modern web, mobile, and API-driven applications. It builds on OAuth 2.0 and includes a standard user identity layer through ID tokens and discovery metadata. It has become the dominant protocol for consumer-facing and cloud-native identity integrations because it fits modern application patterns and developer tooling more naturally.

The key distinction is that [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749) is primarily an authorization framework, while OIDC adds a predictable identity layer on top of it. Security teams often use OIDC for authenticating a user to an application and rely on the application's own authorization logic to decide what a user may access. The identity provider is not automatically the final authorization authority.

### OAuth 2.0 and delegation

[OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749) matters because many modern systems need delegated access without giving a third-party application the user's password. It is designed for scenarios such as a user granting an app access to a subset of resources, or a service requesting access on behalf of a client. This is not the same as authenticating the user to every application in the same way as a standard SSO login flow.

That distinction matters operationally. Teams sometimes overuse the term "OAuth login" when they really mean "user authentication plus delegated token issuance." The architecture is stronger when it explicitly separates:

- user identity authentication
- delegated permissions
- token audience and scope
- authorization decisions in the application or policy layer

## Design patterns

### Centralized identity with local authorization

The most common enterprise pattern is a centralized IdP that authenticates users and issues tokens, while each application enforces its own authorization policy. This pattern reduces credential sprawl and makes identity assurance more consistent, while preserving application-specific entitlements and role models.

This pattern works well when:

- applications have different business contexts
- access policy varies by application or department
- local resource ownership needs to remain explicit
- the organization wants standardized authentication but not a single universal authorization model

### Federation across organizations

Federation is also critical for external identities such as partners, contractors, and customer-facing service access. In those cases, the trust domain of the identity provider is distinct from the trust domain of the application. The application accepts external assertions and then applies local policy to decide whether the actor is authorized to interact with its resources.

This pattern reduces duplication while still preserving security boundaries. It also creates the need for agreement on claims, attribute mapping, proofing assurance, and lifecycle review.

### Conditional access and step-up

SSO is not just a login mechanism. It is also the place where contextual controls such as MFA, device trust, geo restrictions, identity risk, and user context are enforced. These controls are often triggered at sign-in or when the user attempts a higher-risk action. This is why SSO systems frequently sit at the boundary between identity assurance and application access.

Examples include:

- requiring MFA for a privileged user
- blocking sign-in from unapproved devices
- enforcing step-up authentication for sensitive admin actions
- evaluating risk based on unusual network context or impossible travel

These controls improve security without requiring every application to independently implement the same identity-risk logic.

## Operational realities

### Session management is central

An often underestimated part of federation is session lifetime, session revocation, and logout semantics. A user identity that appears valid at sign-in can still become a governance challenge if sessions linger too long, refresh tokens are over-scoped, or logout does not propagate consistently across applications.

A secure SSO design needs to define:

- session lifetime and idle timeout
- refresh token rules and rotation
- logout behavior across multiple parties
- how sign-out and token revocation interact with local app sessions
- how long-lived sessions are governed for high-risk users

### Attribute mapping and identity quality

Many federation failures are not protocol failures. They are data-quality failures. The IdP may assert a username, email, group membership, or role, but the application may interpret the claim differently or accept claims from the wrong source. This creates brittle access patterns, and it undermines auditability.

Good federation design includes:

- clear attribute contracts
- explicit mapping rules for user identity, group membership, and entitlement claims
- validation of claim sources and issuer trust
- consistent handling of missing or stale attributes
- review and change management for federation configuration

### Trust review and lifecycle ownership

Federated relationships require explicit ownership. A team may know how the application authenticates users, but if no one owns the federation contract, trust relationships drift. This is particularly common when legacy applications, SaaS tools, and partner integrations all depend on the same IdP or identity gateway.

A mature program therefore reviews:

- which applications rely on which IdP
- which trust relationships are still active
- the business owner of each federation integration
- the assurance level associated with each identity source
- the exit path for decommissioning a trust relationship

## Governance and security controls

SSO should not be treated as a permission system. It is an identity assurance and trust mechanism. Authorization still belongs to the application, the platform, or the policy evaluation layer. This separation is essential because local business context often determines whether a person should be allowed to do something, and that context may differ across systems even when the user has the same asserted identity.

The security model is stronger when teams combine SSO with:

- MFA and phishing-resistant authentication
- device compliance or device trust
- conditional access based on risk, context, or business rules
- segmentation between workforce, customer, partner, and admin identities
- step-up authentication for sensitive actions
- access review and certification for federated access paths

This governance model preserves the flexibility of federation while making explicit the tradeoff between user convenience and assurance.

## Common anti-patterns

- Treating SSO as if it were the same as authorization
- Allowing each application to build its own copy of identity policy
- Using a single IdP and a single trust model for employees, contractors, partners, and customers without meaningful segmentation
- Accepting broad or poorly mapped claims without validating how the application consumes them
- Ignoring session lifecycle and logout propagation between applications
- Relying on a protocol standard without reviewing the actual trust and governance model it creates

## Summary

SSO and federation are most valuable when they are designed as identity trust systems rather than as login conveniences alone. The primary goal is to centralize identity proofing, authentication assurance, and session governance while preserving clear authorization boundaries in each application or service.

The strongest enterprise architecture treats SSO as the control plane for user identity assurance and federation as the mechanism for trust propagation across domains. This keeps identity governance consistent, makes risk controls easier to enforce, and prevents application teams from reinventing authentication logic in isolated silos.
