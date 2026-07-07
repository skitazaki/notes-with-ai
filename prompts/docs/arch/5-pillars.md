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

5. Pillars versus layers and planes
   - Include a comparison table showing that pillars are not topology, dependency direction, ownership, or runtime paths.

6. Real-world framework examples
   - Include a short comparison of AWS Well-Architected Framework, Microsoft Azure Well-Architected Framework, and Google Cloud Architecture Framework.
   - Explain that these documents are useful real-world examples of pillar-based thinking, but not universal definitions.

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
