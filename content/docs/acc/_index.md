---
date: "2026-05-10T12:00:00+09:00"
title: "Access Control"
weight: 5
next: "/docs/acc/vision"
---

Access control is the architectural discipline that decides who or what may do what, under which conditions, and with what degree of assurance.
In modern systems, that question spans employees, customers, workloads, APIs, third-party services, and AI agents operating across cloud and on-premises boundaries.

This section is organized as a security architecture library rather than a single long report.
Orientation material establishes the shared model, core domains cover the main access-control capabilities, cross-cutting practices address operation and oversight, and reference materials support design decisions. Each collection leads to focused topic pages so readers can move from principles to implementation without mixing different kinds of guidance.

![Access control map showing human, workload, and AI agent principals passing through identity and context, a central policy decision, and enforcement before reaching protected resources, with governance and lifecycle plus monitoring and audit spanning the system](access-control-map.webp "Access Control")

The recommended reading flow is:

1. Vision and principles
2. Landscape and taxonomy
3. Human identity, authorization, workload identity, and AI-agent control models
4. Defense in depth and governance
5. Patterns, threat models, tradeoffs, and reference architectures

Every document follows a similar shape:

- **Executive Summary** for orientation
- **Core Concepts** for the conceptual model
- **Implementation and Operations** for architecture tradeoffs and operating guidance

## Start Here

Begin with the principles and landscape that frame the rest of the library. These are orientation pages, not access-control domains.

{{< cards >}}
{{< card link="vision/" title="Vision & Principles" icon="sparkles" subtitle="North-star principles for identity-centric security" >}}
{{< card link="landscape/" title="Landscape Overview" icon="map" subtitle="A map and taxonomy of the access-control ecosystem" >}}
{{< /cards >}}

## Core Access-Control Domains

Explore the capabilities that establish identities, make authorization decisions, and extend those controls to emerging kinds of principals and execution.

{{< cards >}}
{{< card link="identity-foundations/" title="Identity Foundations" icon="users" subtitle="Human, workload, machine, and non-human identity" >}}
{{< card link="authorization-systems/" title="Authorization Systems" icon="shield-check" subtitle="Authorization models, policy systems, and evaluation tradeoffs" >}}
{{< card link="ai-emerging-systems/" title="AI & Emerging Systems" icon="chip" subtitle="Agent identities, constrained execution, and approval boundaries" >}}
{{< /cards >}}

## Cross-Cutting Practices

Apply operational safeguards and governance across every access-control domain.

{{< cards >}}
{{< card link="security-operations/" title="Security Operations" icon="shield-exclamation" subtitle="Layered controls, threat models, monitoring, and response" >}}
{{< card link="governance-compliance/" title="Governance & Compliance" icon="clipboard-list" subtitle="Evidence, explainability, entitlement governance, and regulation" >}}
{{< /cards >}}

## Reference Library

Use these reusable materials while comparing designs, selecting patterns, or reviewing an architecture.

{{< cards >}}
{{< card link="reference-materials/" title="Reference Materials" icon="book-open" subtitle="Patterns, decision frameworks, architectures, and shared terminology" >}}
{{< /cards >}}
