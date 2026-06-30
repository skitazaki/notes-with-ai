---
type: image
path: /docs/arch/flows-and-pipelines
description: Real-world example diagram showing an end-to-end support ticket AI assistant flow.
---

# Image Generation Prompt - Flows and Pipelines Example

Create a clean architecture example diagram titled:

"Example: Support Ticket AI Flow"

Use case:

A support engineer asks an internal AI assistant to draft an answer for a customer ticket.
The request must pass through identity checks, policy validation, retrieval from internal knowledge, model execution, safety review, audit logging, and asynchronous quality evaluation.

Image content:

Create a left-to-right flow with these stages:

- support engineer
- support portal
- identity check
- policy validation
- ticket context
- knowledge retrieval
- model gateway
- safety check
- draft response
- audit log
- async evaluation job

Show one queue or asynchronous handoff after audit logging.
Show one alternate path for human review when the safety check fails.
Use boundary boxes for user-facing app, platform services, data sources, and governance controls.

Style:

- precise technical flow diagram
- clean vector sequence layout
- light background
- restrained colors
- 16:9 aspect ratio
- documentation-ready

Text rules:

- Use short stage and system labels only.
- Do not include captions, takeaways, or explanatory notes.
- Avoid long annotations.

Do:

- show synchronous and asynchronous movement clearly
- make the support ticket scenario concrete
- include audit, retry, and review behavior

Do not:

- show people, desks, screens, or room interiors
- draw every internal microservice call
- use product logos or vendor-specific UI
