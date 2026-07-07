---
type: docs
path: /docs/arch/decision-frameworks
---

Write a concise reference page titled:
"Decision Frameworks"

You are a senior software architect and technical decision facilitator explaining how teams use architecture concepts to make better decisions.

Audience:

- Architects
- Senior engineers
- Engineering managers
- Platform leaders
- Technical reviewers

Purpose:

- Show how architecture dimensions, pillars, views, and tradeoffs support decisions
- Provide a practical framework for choosing the right architecture representation for a decision
- Help readers move from terminology to judgment

Core message:

Architecture concepts are useful when they improve decisions.
A good decision framework connects the concern, the relevant dimension, the tradeoffs, the stakeholders, and the evidence needed to decide.

Scope:

- Cover concern framing, decision drivers, constraints, options, tradeoffs, risks, evidence, and consequences
- Explain how to choose between layers, planes, flows, ownership boundaries, and views depending on the decision
- Include lightweight guidance for architecture decision records without making the page an ADR tutorial

Tone and style:

- Practical, precise, and decision-oriented
- Avoid process-heavy governance language
- Emphasize clarity over ceremony

Structure:

1. Definition
   - Define an architecture decision framework as a repeatable way to connect concerns, options, tradeoffs, and consequences.

2. Why decision frameworks matter
   - Explain that architecture decisions often fail when teams argue terminology instead of clarifying the question being answered.

3. Start with the concern
   - Identify the stakeholder, decision, risk, constraint, and success criteria.

4. Choose the relevant dimension
   - Structural concerns usually need layers, modules, components, or dependency views.
   - Operational concerns usually need planes, flows, or runtime views.
   - Strategic concerns usually need pillars, principles, or quality attributes.
   - Ownership concerns usually need domain, team, data, or platform boundaries.
   - Communication concerns usually need audience-specific views.

5. Compare options
   - Include a decision table with:
     - Option
     - Benefits
     - Costs
     - Risks
     - Reversibility
     - Evidence needed

6. Example decision
   - Use a concrete decision, such as centralized versus distributed policy enforcement, platform service boundaries, or control-plane/data-plane separation.
   - Mention that an image should appear here showing the decision process from concern to dimension to view to decision.

7. Recording the decision
   - Briefly explain what to capture:
     - Context
     - Decision
     - Alternatives
     - Consequences
     - Review trigger

8. Common mistakes
   - Choosing a diagram before identifying the decision
   - Treating pillars as equal in every context
   - Ignoring reversibility
   - Recording conclusions without tradeoffs

Constraints:

- Do not write a full ADR template.
- Do not include implementation steps.
- Do not include image-generation instructions.

---

# Architecture Decision Records (ADRs)

**There is no single official standards document** for Architecture Decision Records (ADRs). Instead, the industry has converged around a handful of influential sources that have become de facto standards.

The closest thing to a canonical lineage is:

1. **Michael Nygard's "Documenting Architecture Decisions" (2011)** [^nygard]
   - This is widely regarded as the origin of the modern ADR.
   - Introduced the now-familiar sections:
     - Title
     - Status
     - Context
     - Decision
     - Consequences

   - The original article is still the document most people cite when explaining ADRs.

2. **Thoughtworks Technology Radar** [^thoughtworks]
   - Thoughtworks has repeatedly recommended ADRs as an engineering practice.
   - Their guidance helped popularize ADRs across the software industry.
   - They also maintain templates and examples.

3. **ADR GitHub Organization** [^adr]
   - The community-maintained GitHub organization has become the practical reference.
   - It contains:
     - multiple ADR templates
     - markdown conventions
     - tooling
     - examples

   - Many companies adopt these templates almost verbatim.

## The "canonical" template

Today, if you ask 100 software architects to write an ADR, most would produce something very close to this:

```text
ADR-0007: Use PostgreSQL

Status
Accepted

Context
We need a transactional relational database...

Decision
Use PostgreSQL for all production workloads.

Consequences
+ Mature ecosystem
+ Strong replication
- Requires DBA expertise
```

Some teams extend it with:

- Alternatives considered
- Assumptions
- Risks
- Compliance implications
- Links
- Supersedes / Superseded by
- Date
- Decision drivers

## There are several established formats

Although Nygard's template is the most influential, several variants have become common.

| Format                                   | Origin                  | Characteristics                                     |
| ---------------------------------------- | ----------------------- | --------------------------------------------------- |
| Nygard ADR [^nygard]                     | Michael Nygard          | Minimal, elegant                                    |
| MADR (Markdown ADR) [^madr]              | Community               | Rich metadata, decision drivers, alternatives       |
| Tyree & Akerman Decision Template        | Enterprise architecture | Much more formal and comprehensive                  |
| Arc42 ADRs [^arc42]                      | Arc42                   | Integrated with software architecture documentation |
| AWS Architecture Decision Records [^aws] | Internal practice       | Cloud-focused adaptations                           |

## Why there is no ISO or IEEE standard

ADRs deliberately evolved as **lightweight engineering artifacts**, not governance documents.

Unlike architecture descriptions, which are standardized in ISO/IEC/IEEE 42010 [^iso42010], ADRs are intended to be:

- easy to write
- stored alongside code
- version controlled
- inexpensive to maintain

The philosophy is:

> Record the decision while the reasoning is still fresh.

rather than

> Produce exhaustive design documentation.

## Relationship to ISO 42010

This distinction is often overlooked:

- **ISO 42010** [^iso42010] defines **how to describe an architecture**:
  - stakeholders
  - concerns
  - viewpoints
  - views
  - architecture description

- **ADRs** describe **why specific architectural decisions were made**.

In other words:

```
Architecture Description
    ├── Viewpoints
    ├── Views
    └── ...
           ▲
           │ supported by
           │
Architecture Decision Records
```

Many organizations use ADRs as the rationale supporting an ISO 42010-compliant architecture description.

---

## If you're writing about software architecture

Given your recent work on architectural dimensions, planes, and reasoning models, I'd recommend treating ADRs not simply as "decision logs," but as **records of architectural reasoning**.

A useful framing is:

- **Architecture descriptions** answer: _What is the architecture?_
- **Architecture views** answer: _How should we reason about it?_
- **Architecture Decision Records** answer: _Why did we choose this?_
- **Architecture principles** answer: _What should consistently guide future decisions?_

This positions ADRs as one part of a broader architectural knowledge system, alongside principles, viewpoints, patterns, and governance. That perspective aligns well with modern architecture practices and provides a richer conceptual model than treating ADRs as isolated Markdown files.

[^nygard]: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

[^thoughtworks]: https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records

[^adr]: https://adr.github.io/

[^madr]: https://adr.github.io/madr/

[^arc42]: https://arc42.org/overview

[^aws]: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html

[^iso42010]: https://www.iso.org/standard/74393.html
