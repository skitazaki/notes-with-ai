---
date: "2026-08-13T00:00:00+09:00"
title: "Data Spaces"
weight: 4
prev: "/docs/data/sharing/data-clean-rooms"
next: "/docs/data/sharing/open-data"
---

A data space is a federated environment in which independent participants share and use data through common rules, trust mechanisms, and interoperable services. It coordinates an ecosystem without requiring all data, infrastructure, or authority to be centralized in one platform.

“Data space” names a family of organizational and architectural approaches, not one universal protocol. Implementations differ by industry, jurisdiction, governance, technical stack, and the degree of control retained by each participant.

## Why a Data Space Is Different

A bilateral share connects a producer and consumer. A marketplace coordinates offers and entitlements. A data space goes further by establishing reusable participation rules and services for many parties that may act as producers, consumers, intermediaries, or operators over time.

The objective is not necessarily to create a shared data lake. Data may remain with participants and be accessed through APIs, files, live shares, federation, clean rooms, or other [exchange mechanisms](/docs/data/sharing/data-exchange-mechanisms/).

## Architectural Building Blocks

| Building block          | Core question                                                                |
| ----------------------- | ---------------------------------------------------------------------------- |
| Participant identity    | How is an organization, person, or workload recognized across the ecosystem? |
| Trust and onboarding    | What evidence and agreements are required to participate?                    |
| Catalog and discovery   | How are products, services, policies, and participants found?                |
| Data products           | What stable, owned interface is being offered?                               |
| Exchange services       | How are data, queries, events, or results delivered?                         |
| Policy and contracts    | How are permitted purposes, duties, and restrictions expressed?              |
| Semantics               | How are identifiers, vocabularies, units, and concepts aligned?              |
| Provenance and evidence | How can origin, transformation, use, and decisions be traced?                |
| Governance              | Who changes rules, resolves disputes, and holds participants accountable?    |

Interoperability must be evaluated across these layers. A shared file format does not make identity or policy portable. A common catalog vocabulary does not guarantee that two participants interpret a business concept or enforcement obligation the same way.

## Governance Model

Data spaces require constitutional governance as well as technical control. Participants need to know:

- who defines and changes membership rules
- what rights and duties attach to participation
- which standards or profiles are mandatory
- how certification or conformity is assessed
- how incidents, complaints, and disputes are handled
- how costs and shared services are funded
- how a participant or product exits the ecosystem

Federation does not mean the absence of central coordination. It means central responsibilities are deliberately bounded while data ownership and enforcement may remain distributed.

## Data Sovereignty and Control

Data-space discussions often use “data sovereignty” to express a participant's ability to determine how its data is used. This intent must be translated into concrete controls and realistic limits.

Live access can be revoked more directly than a downloaded copy. Machine-readable policy can communicate permitted use but does not guarantee compliance. Contracts can cover behavior outside technical visibility but require enforcement and evidence. A useful architecture states which controls are preventive, detective, contractual, or dependent on participant trust.

[ODRL](https://www.w3.org/TR/odrl-model/) provides a standard model for expressing permissions, prohibitions, duties, parties, assets, and constraints. It can support policy exchange, but participating systems still need shared profiles, decision logic, enforcement points, and audit behavior.

## Semantic and Catalog Interoperability

Participants need enough shared meaning to discover and combine products without erasing legitimate domain differences. [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) can support interoperable catalog descriptions and federated discovery. A [semantic layer](/docs/data/metadata/semantic-layer/) or explicit vocabulary mappings can align business concepts, identifiers, units, and classifications.

The goal is bounded agreement: standardize what must cross the ecosystem boundary and preserve local models where they do not prevent use or governance.

## Relationship to Data Mesh

[Data Mesh](/docs/data/metadata/data-mesh/) addresses decentralized ownership inside or across organizational domains. A data space applies related principles to an ecosystem whose participants may have separate legal authority, infrastructure, and incentives.

[Federated Governance](/docs/data/metadata/federated-governance/) provides the operating logic for balancing local control with shared policy. Data products provide the consumable boundary. The data space adds ecosystem membership, cross-organization trust, and shared services.

## Reference Models and Maturity

The archived [Data Spaces Support Centre Blueprint v2.0](https://archive.dssc.eu/space/BVE2/1071251457/Data+Spaces+Blueprint+v2.0+-+Home) preserves concepts and building blocks developed during the DSSC initiative. It is useful as historical design context, not as a currently maintained specification or proof of interoperability.

Production ecosystems should distinguish aspirational principles, reference architectures, profiles, tested implementations, and actual cross-participant conformance. Using the same vocabulary does not establish technical compatibility.

## Common Failure Modes

- Creating a central platform while describing ownership as federated
- Focusing on connectors before establishing participation and accountability
- Treating sovereignty as a product feature rather than a layered control model
- Assuming common formats guarantee semantic or policy interoperability
- Defining governance without sustainable funding and operational ownership
- Launching an ecosystem without a clear consumer problem or measurable value

## Summary

A data space coordinates governed data use among independent participants. Its architecture combines federation, shared rules, identity, catalogs, data products, exchange services, policy, semantics, provenance, and ecosystem governance.

The durable design question is not whether a platform is called a data space. It is whether participants can cross organizational boundaries with explicit trust, interoperable interfaces, enforceable responsibilities, and enough shared value to sustain the ecosystem.
