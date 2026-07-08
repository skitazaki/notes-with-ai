---
type: docs
path: /docs/arch/pillars
---

Write a concise reference page titled:
"Pillars"

You are a senior software architect and technical writer explaining pillars as strategic architecture concepts.

Audience:

- Architects
- Engineering managers
- Platform leaders
- Senior engineers
- Technical decision makers

Purpose:

- Explain why architecture pillars exist
- Clarify how pillars differ from layers, planes, services, and runtime topology
- Show how pillars guide tradeoffs and architectural decisions

Core message:

Pillars represent architectural priorities.
They describe the qualities a system must optimize for, not the components the system is built from or the paths it executes.

Scope:

- Cover common pillars such as reliability, security, scalability, performance, cost efficiency, operability, maintainability, and developer experience
- Explain how pillars become principles, requirements, constraints, and review criteria
- Use examples from cloud architecture, platform engineering, and AI systems
- Ground the discussion in real-world hyperscaler reference documents, including AWS Well-Architected Framework, Microsoft Azure Well-Architected Framework, and Google Cloud Architecture Framework

Required source anchors:

- AWS Well-Architected Framework as a concrete example of a published pillar model:
  https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- Microsoft Azure Well-Architected Framework as a contrasting example with overlapping but differently framed priorities:
  https://learn.microsoft.com/en-us/azure/well-architected/
- Google Cloud Architecture Framework as another concrete example of how strategic qualities are organized and communicated:
  https://cloud.google.com/architecture/framework
- Use these sources to show similarities and differences, but keep the article vendor-neutral and concept-first

Tone and style:

- Practical, sober, and decision-oriented
- Avoid framework worship or vendor-specific pillar lists
- Emphasize tradeoffs instead of slogans

Structure:

1. Definition
   - Define a pillar as a strategic quality or priority used to guide architecture decisions.

2. Why pillars exist
   - Explain that pillars help answer:
     - What are we optimizing for?
     - Which qualities should shape tradeoffs?
     - How will we evaluate whether a design is acceptable?

3. Common pillars
   - Reliability
   - Security
   - Scalability
   - Performance
   - Cost efficiency
   - Operability
   - Maintainability
   - Developer experience
   - Briefly note how these ideas appear in AWS, Azure, and Google Cloud framework documents, including where names or emphasis differ

4. How pillars influence decisions
   - Show how a pillar can become a principle, policy, standard, review checklist, or design constraint.

5. Real-world framework examples
   - Include a short comparison of AWS Well-Architected Framework, Microsoft Azure Well-Architected Framework, and Google Cloud Architecture Framework.
   - Explain that these documents are useful real-world examples of pillar-based thinking, but not universal definitions.
   - When discussing **architecture pillars**, recognize that different organizations define different pillar sets. Draw examples from industry frameworks such as AWS Well-Architected, Azure Well-Architected, Google Cloud Architecture Framework, Oracle OCI Well-Architected, IBM Cloud Architecture Framework, TOGAF, ISO/IEC 25010, Software Architecture in Practice, and Data Mesh. Explain that pillars represent enduring architectural concerns (quality attributes or capability domains) rather than structural decomposition, and compare how these frameworks overlap despite using different terminology.
   - Add a short subsection on Responsible AI as a real-world example of pillar-based decision making in AI systems.
   - Explain how concerns such as fairness, safety, privacy, transparency, accountability, and reliability can function as architecture pillars that shape model selection, evaluation criteria, deployment controls, and human oversight.

6. Pillars versus layers and planes
   - Include a comparison table showing that pillars are not topology, dependency direction, ownership, or runtime paths.

7. Example: tradeoff analysis
   - Use a concrete design decision and show how different pillars push the decision in different directions.
   - Mention that an image should appear here showing pillars as decision lenses applied to one architecture choice.

8. Common mistakes
   - Listing too many pillars
   - Treating pillars as branding language
   - Ignoring tradeoffs between pillars
   - Confusing aspirational values with enforceable design criteria

Constraints:

- Do not reproduce any vendor framework as the definitive model.
- Do not turn the page into a vendor survey; use AWS, Azure, and Google Cloud documents as supporting examples.
- Do not include implementation steps.
- Do not include image-generation instructions.

---

# Industry Frameworks

If you're writing about **architecture pillars** in software architecture, it's useful to include the major industry frameworks that explicitly organize architecture into _pillars_, _principles_, _quality attributes_, or _domains_. They all use slightly different terminology, but they represent the same idea: grouping architectural concerns into enduring dimensions.

Here's a comprehensive list you can include in your content-generation prompt.

| Framework                                              | Pillars / Domains                                                                                                   |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| AWS Well-Architected Framework                         | Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability            |
| Microsoft Azure Well-Architected Framework             | Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency                            |
| Google Cloud Architecture Framework                    | System Design, Operational Excellence, Security & Privacy, Reliability, Cost Optimization, Performance Optimization |
| Oracle Cloud Infrastructure Well-Architected Framework | Security & Compliance, Reliability & Resilience, Performance & Cost Optimization, Operational Efficiency            |
| IBM Cloud Architecture Framework                       | Security, Resilience, Performance, Operations, Governance                                                           |
| Cisco Cloud Architecture Framework                     | Security, Automation, Operations, Connectivity, Governance                                                          |

## Enterprise Architecture Frameworks

These don't always call them "pillars," but define enduring architecture domains.

- The Open Group Architecture Framework
  - Business
  - Data
  - Application
  - Technology

- Gartner Enterprise Architecture
  - Business
  - Information
  - Technology
  - Security
  - Governance

- Federal Enterprise Architecture Framework
  - Performance
  - Business
  - Data
  - Applications
  - Infrastructure
  - Security

## Software Architecture Quality Attribute Models

These are not marketed as "well-architected" frameworks but are foundational references for architecture pillars.

- Software Architecture in Practice
  - Performance
  - Availability
  - Modifiability
  - Security
  - Testability
  - Usability
  - Interoperability

- ISO/IEC 25010
  - Functional Suitability
  - Performance Efficiency
  - Compatibility
  - Usability
  - Reliability
  - Security
  - Maintainability
  - Portability

## Data & AI Architecture

Useful when discussing modern platform architecture.

- Data Mesh
  - Domain Ownership
  - Data as a Product
  - Self-Serve Platform
  - Federated Computational Governance

- Lakehouse Architecture
  - Governance
  - Reliability
  - Performance
  - Openness
  - Scalability

- Responsible AI (implemented by many organizations)
  - Fairness
  - Reliability
  - Privacy
  - Transparency
  - Accountability
  - Safety

## Common Cross-Industry Architecture Pillars

Across these frameworks, a recurring set of architectural pillars emerges:

- Security
- Reliability / Resilience
- Performance / Efficiency
- Scalability
- Operational Excellence
- Maintainability
- Cost Optimization
- Sustainability
- Governance
- Observability
- Compliance
- Interoperability
- Availability
- Recoverability
- Privacy
- Automation
