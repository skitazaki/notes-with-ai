---
date: "2026-05-10T12:00:00+09:00"
title: "Access Control"
weight: 5
---

Access control is the architectural discipline that decides who or what may do what, under which conditions, and with what degree of assurance.
In modern systems, that question spans employees, customers, workloads, APIs, third-party services, and AI agents operating across cloud and on-premises boundaries.

This section is organized as a three-level security architecture library rather than a single long report.
The field overview leads to domain hubs, and each hub leads to focused topic pages. This structure separates guiding principles, technical domains, operational controls, and reusable reference material so readers can move from strategy to implementation without losing the conceptual model.

![Access control map showing human, workload, and AI-agent principals passing through identity and context, a central policy decision, and enforcement before reaching protected resources, with governance and audit spanning the system](access-control-map.webp "Access Control")

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

## Explore Access Control Domains

Use these hubs to move from the overall access-control landscape into a specific domain, operating concern, or reference collection.

{{< cards >}}
{{< card link="introduction/" title="Introduction" icon="map" subtitle="Vision, principles, and a map of the access-control landscape" >}}
{{< card link="identity-foundations/" title="Identity Foundations" icon="users" subtitle="Human, workload, machine, and non-human identity" >}}
{{< card link="authorization-systems/" title="Authorization Systems" icon="shield-check" subtitle="Authorization models, policy systems, and evaluation tradeoffs" >}}
{{< card link="ai-emerging-systems/" title="AI & Emerging Systems" icon="chip" subtitle="Agent identities, constrained execution, and approval boundaries" >}}
{{< card link="security-operations/" title="Security Operations" icon="shield-exclamation" subtitle="Layered controls, threat models, monitoring, and response" >}}
{{< card link="governance-compliance/" title="Governance & Compliance" icon="clipboard-list" subtitle="Evidence, explainability, entitlement governance, and regulation" >}}
{{< card link="reference-materials/" title="Reference Materials" icon="book-open" subtitle="Patterns, decision frameworks, architectures, and shared terminology" >}}
{{< /cards >}}
