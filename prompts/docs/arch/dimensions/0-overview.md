---
type: docs
path: /docs/arch/dimensions
---

Write a concise reference page titled:
"Architecture Dimensions"

You are a senior software architect and technical writer explaining how engineers use different architecture dimensions to reason about the same system.

Audience:

- Senior engineers
- Architects
- Platform engineers
- Engineering managers

Purpose:

- Define the idea of an architecture dimension
- Explain why architecture is not one model, diagram, or taxonomy
- Provide a stable framework that connects the rest of the architecture documentation library

Core message:

Architecture dimensions are complementary lenses.
Each dimension answers a different primary question and hides details that are not relevant to that question.

Scope:

- Cover structural, operational, strategic, ownership, and communication dimensions
- Explain how dimensions differ from diagrams and views
- Use a single running example, such as a cloud-native AI platform, to show how each dimension highlights different concerns

Tone and style:

- Neutral, conceptual, and precise
- Practical enough for working architects
- Avoid academic taxonomy for its own sake

Structure:

1. Definition
   - Define an architecture dimension as a reasoning lens for a system.

2. Why dimensions matter
   - Explain why teams struggle when they mix dependency structure, runtime behavior, strategic priorities, and team ownership in one model.

3. The core dimensions
   - Structural: what is built and what depends on what
   - Operational: how work moves, executes, and is controlled
   - Strategic: what qualities and principles drive decisions
   - Ownership: who is responsible for domains, services, data, and change
   - Communication: how selected concerns are presented to an audience

4. Comparison table
   - Include a table with columns:
     - Dimension
     - Primary question
     - Common concepts
     - Useful for
     - Common mistake

5. Example: one platform, many dimensions
   - Show how the same platform can be described through each dimension.
   - Mention that an image should appear here showing one system projected into multiple architecture dimensions.

6. Relationship to views
   - Explain that dimensions are used for reasoning, while views are produced for communication.
   - Introduce the chain:
     - Concern
     - Dimension
     - Reasoning
     - View

Constraints:

- Do not turn the page into a dictionary of architecture terms.
- Do not rank dimensions as better or worse.
- Do not include implementation steps.
- Do not include image-generation instructions.
