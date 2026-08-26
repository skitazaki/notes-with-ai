---
date: "2026-08-22T00:00:00+09:00"
title: "Data Governance"
weight: 6
prev: "/docs/data/metadata"
next: "/docs/data/governance/principles-and-operating-model"
---

Data Governance is the organizational control system that determines who is accountable for data, what policies and decision rights apply, how those policies become operational controls, and how the organization verifies that governance is working.

Governance exists so people can use data with justified confidence. It makes authority, obligations, and exceptions explicit across organizational and system boundaries. Effective governance supports trusted data use through clear decision boundaries and proportionate controls. It can operate within centralized, federated, or hybrid models; no one model is an inherent target state.

Within the Data section, governance is part of the cross-cutting **Control Layer**. It establishes the rules and accountability that apply from collection through management, analysis, sharing, and retirement.

## Governance and Management

**Governance defines expectations and accountability; management performs the ongoing work required to satisfy them.** Governance may set a quality objective, retention obligation, or service expectation. [Data Management](/docs/data/management/) owns the practices that keep data reliable, usable, and sustainable. Master Data Management and Data Quality therefore remain management disciplines.

## The Governance Control Loop

Ownership and stewardship apply throughout this loop. Metadata connects policies to assets and controls, then captures the lineage, decisions, and observations needed as evidence.

![The Data Governance control loop progressing clockwise through seven topic-aligned stages from principles and operating model to review and change, centered on trusted data use across centralized, federated, and hybrid models, with accountability above and metadata below](data-governance-control-loop.webp "Data Governance Control Loop")

Traditional governance often relied on centralized committees, documents, and manual approvals. Those mechanisms can remain appropriate for high-impact decisions. Domain ownership, policy-as-code, metadata-driven controls, and federated forums add other ways to coordinate decisions at scale. These are design choices, not a universal maturity sequence.

## Major Concerns

- **Accountability and decision rights:** identify who owns an outcome, who may decide, and who performs the work.
- **Policies, standards, and controls:** translate intent into testable expectations and operational mechanisms.
- **Classification:** apply differentiated obligations according to sensitivity, personal-data status, criticality, retention, and sharing constraints.
- **Exceptions and escalation:** make departures explicit, time-bounded, approved, and reviewable.
- **Evidence and assurance:** demonstrate whether controls operate and policies achieve their objectives.
- **Federation:** preserve enterprise consistency while leaving contextual decisions with domains.

## Relationships with Neighboring Data Topics

| Domain                                             | Primary question                                                                    |
| -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Data Governance**                                | Who decides, what rules apply, and how is accountability demonstrated?              |
| [Data Management](/docs/data/management/)          | How do we keep data reliable, usable, and sustainable?                              |
| [Metadata](/docs/data/metadata/)                   | What do we know about the data and its context?                                     |
| [Data Privacy](/docs/data/privacy/)                | Under what conditions should information about people be processed?                 |
| Data Security                                      | How is data protected against unauthorized access, alteration, disclosure, or loss? |
| [Data Architecture](/docs/data/data-architecture/) | How should data systems, boundaries, and flows be structured?                       |
| [Data Teams](/docs/data/teams/)                    | Who builds, operates, analyzes, and supports the data ecosystem?                    |

These capabilities meet at interfaces rather than forming isolated silos. Governance defines classification and control objectives; Metadata represents and propagates their context; Security and Privacy implement specialized safeguards; Architecture places structural boundaries; and Management performs sustained operational work.

## Explore Data Governance

{{< cards >}}
{{< card link="principles-and-operating-model/" title="Principles and Operating Model" icon="adjustments" subtitle="Accountability, authority, forums, escalation, and the policy lifecycle" >}}
{{< card link="ownership-and-stewardship/" title="Ownership and Stewardship" icon="users" subtitle="Decision rights for domains, assets, and data products" >}}
{{< card link="policies-standards-and-controls/" title="Policies, Standards, and Controls" icon="shield-check" subtitle="From principles to enforceable controls and evidence" >}}
{{< card link="data-classification/" title="Data Classification" icon="tag" subtitle="Multiple dimensions that drive differentiated obligations" >}}
{{< card link="compliance-and-auditability/" title="Compliance and Auditability" icon="clipboard-check" subtitle="Traceability, assurance, monitoring, and demonstrable control" >}}
{{< card link="federated-data-governance/" title="Federated Data Governance" icon="share" subtitle="Enterprise consistency with contextual domain decisions" >}}
{{< /cards >}}

## Further Reading

- [ISO/IEC 38505: Governance of data](https://www.iso.org/standard/87195.html)
- [EDM Council: DCAM](https://edmcouncil.org/frameworks/dcam/)
- [COBIT](https://www.isaca.org/resources/cobit)
- [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html)
