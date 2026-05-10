+++
date = '2026-05-10T12:00:00+09:00'
title = 'Access Control'
weight = 2
+++

Access control is the architectural discipline that decides who or what may do what, under which conditions, and with what degree of assurance.
In modern systems, that question spans employees, customers, workloads, APIs, third-party services, and AI agents operating across cloud and on-premises boundaries.

This section is organized as a security architecture library rather than a single long report.
It separates guiding principles, technical domains, operational controls, and reusable reference material so readers can move from strategy to implementation without losing the conceptual model.

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

<!-- deno-fmt-ignore-start -->

{{< cards >}}
{{< card link="vision/" title="Vision & Principles" icon="sparkles" subtitle="North-star principles for identity-centric security" >}}
{{< card link="landscape/" title="Landscape Overview" icon="document-text" subtitle="Taxonomy of the access-control ecosystem" >}}
{{< card link="human-identity/" title="Human Identity & Enterprise IAM" icon="users" subtitle="Lifecycle, federation, PAM, and governance" >}}
{{< card link="authorization-models/" title="Authorization Models & Policy Systems" icon="shield-check" subtitle="DAC, MAC, RBAC, ABAC, ReBAC, PBAC, and policy engines" >}}
{{< card link="workload-identity/" title="Workload & Machine Identity" icon="document-text" subtitle="Machine-to-machine trust in distributed systems" >}}
{{< card link="ai-agents/" title="AI Agents & Autonomous Authorization" icon="document-text" subtitle="Agent identities, constrained execution, and approval boundaries" >}}
{{< card link="defense-in-depth/" title="Defense-in-Depth Architecture" icon="document-text" subtitle="Layered controls across identity, network, runtime, and telemetry" >}}
{{< card link="governance/" title="Governance, Compliance & Auditability" icon="document-text" subtitle="Evidence, explainability, entitlement governance, and regulation" >}}
{{< card link="patterns/" title="Architecture Patterns Catalog" icon="document-text" subtitle="Reusable enforcement and deployment patterns" >}}
{{< card link="threat-models/" title="Threat Model Catalog" icon="document-text" subtitle="Common failure modes, attack paths, and mitigations" >}}
{{< card link="decision-frameworks/" title="Decision Frameworks & Tradeoffs" icon="scale" subtitle="How to choose between competing designs" >}}
{{< card link="reference-architectures/" title="Reference Architectures" icon="document-text" subtitle="End-to-end example architectures" >}}
{{< card link="concept-dictionary/" title="Concept Dictionary" icon="book-open" subtitle="Shared terminology for principals, policies, scopes, and trust boundaries" >}}
{{< /cards >}}

<!-- deno-fmt-ignore-end -->
