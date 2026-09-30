---
type: prompt
path: /docs/data/architecture/data-mesh
draft: true
---

Create a documentation topic page titled:

# Data Mesh

Write the page as a clear architecture-oriented topic under the Data Architecture section.
This page should consolidate the core principles previously described in the metadata-focused article about Data Mesh and make them the main organizing structure for the new topic page.

The key objective is to present Data Mesh as a domain-oriented data architecture pattern, with metadata treated as an enabling capability rather than the page’s primary subject.

## Writer role

You are a senior data architect and technical writer with deep experience in distributed data organizations, domain-oriented architecture, and platform design.

## Audience

- Data architects
- Platform leaders
- Engineering managers
- Senior data engineers
- Technical leaders designing shared data operating models

## Purpose

- Define what Data Mesh is and why it emerged
- Explain the architectural trade-offs it is meant to solve
- Show how the four core principles work together as a coherent model
- Clarify where metadata, standards, and platform capabilities fit in the overall design
- Help readers decide when Data Mesh is appropriate and when it is not

## Scope

Focus on architectural thinking and operating model design, not product marketing or implementation checklists.

Treat this page as the architecture-level counterpart to the more metadata-oriented treatment in the existing Data Mesh & Metadata page.
The new page should synthesize the following four principles as the heart of the article:

1. Domain ownership
2. Data as a product
3. Self-serve data platform
4. Federated governance

Use these as the central organizing principles rather than as a sidebar or appendix.

## Core message

Data Mesh is not simply a decentralized storage pattern. It is a way to distribute ownership and accountability while preserving interoperability through common standards, platform capabilities, and governance at the edges.

The page should explain that the architecture works when:

- domains own their data and its semantics
- data is packaged and treated as a product with clear contracts
- platform capabilities let teams publish, discover, and consume data without heavy central bottlenecks
- governance is shared, explainable, and applied across domains instead of being centralized into a single control tower

## Required structure

Write the article with this structure:

1. Introduction and problem framing
   - Why organizations move from centralized data platforms toward domain-oriented operating models
   - The coordination problem that Data Mesh is trying to solve

2. What Data Mesh is
   - Definition of the pattern
   - Distinction from simple data decentralization
   - Why ownership and accountability matter

3. The four principles as a unified model
   - Domain ownership: local accountability, domain semantics, and product boundaries
   - Data as a product: discoverability, contracts, quality, lifecycle, and consumption expectations
   - Self-serve data platform: platform capabilities that reduce dependency on centralized delivery teams
   - Federated governance: shared standards, policy, compliance, and interoperable controls across domains

4. Why metadata matters in a mesh
   - Metadata as an enabling control plane, not the main topic
   - Ownership metadata, product metadata, contract metadata, lineage, quality, and policy context
   - How metadata supports trust and interoperability in a distributed model

5. Architectural operating model
   - Domain teams as primary producers and stewards
   - Central platform teams as enablers of common capabilities
   - Shared standards and interfaces that keep autonomy from turning into fragmentation

6. Benefits and trade-offs
   - Speed and domain alignment
   - Better accountability and clearer ownership
   - Improved discoverability and productization
   - Risks of weak standards, duplicated efforts, fragmented semantics, and organizational drift

7. When Data Mesh fits and when it does not
   - Good fit: large, domain-rich organizations with meaningful autonomy and platform maturity
   - Weak fit: small organizations, early-stage data programs, or teams that require stronger central control

8. Summary
   - Re-state the core architectural idea
   - Emphasize that Data Mesh is a coordination model as much as an architecture

## Tone and style

- Neutral, explanatory, and precise
- Written for senior technical practitioners
- Clear conceptual framing before detail
- No hype or marketing language
- No step-by-step implementation guide unless a brief practical note is necessary

## Constraints

- Do not treat metadata as the entire page topic; keep it clearly subordinate to the architectural concept
- Consolidate the four principles into a cohesive explanation rather than a list of disconnected concepts
- Avoid repeating the same ideas from the metadata-specific article verbatim; synthesize them into a more architecture-focused framing
- Keep the content evergreen and reusable as a reference page
- Include links to related concepts where relevant, such as Data Architecture, Data Products, Federated Governance, Semantic Layer, and Metadata, but do not force the page into a catalog of adjacent topics

## Target destination

The final article should be saved at:

`content/docs/data/architecture/data-mesh/_index.md`

The generated page should be written in English and suitable for the repository’s documentation style.
