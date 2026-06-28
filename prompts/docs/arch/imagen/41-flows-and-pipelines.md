---
type: image
path: /docs/arch/flows-and-pipelines
description: Concrete example figure showing an end-to-end AI assistant request flow with checks, handoffs, and feedback.
---

# Image Generation Prompt - Flows and Pipelines Example

Create a publication-quality example figure titled:

"Example: One End-to-End Flow"

Purpose:

Illustrate an internal AI assistant request flowing through identity, policy, retrieval, model execution, safety checks, audit logging, and asynchronous evaluation.

Style:

- technical process infographic
- clean vector sequence layout
- light background
- readable handoff arrows and annotations
- sober documentation tone
- 16:9 aspect ratio

Composition:

Create a left-to-right flow beginning with a support engineer user request.
Include major stages such as:

- user request
- identity and access check
- policy validation
- retrieval from internal knowledge base
- model invocation with bounded tools
- output safety check
- response returned to user
- audit log capture
- asynchronous evaluation or review job

Show at least one queue or async handoff and at least one retry or alternate review path.

Central message:

Flow views explain sequence, transformation, handoffs, and failure paths that static structure alone cannot show.

Do:

- show both synchronous and asynchronous movement
- make trust or control boundaries visible
- keep the end-to-end story concrete and readable

Do not:

- draw every internal microservice call
- make the diagram look like a generic UML sequence screenshot
- omit audit, retry, or review behavior
