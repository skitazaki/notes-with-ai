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
