---
type: image
path: /docs/arch/decision-frameworks
description: Real-world example diagram showing an architecture decision for control-plane orchestration.
---

# Image Generation Prompt - Decision Frameworks Example

Create a clean architecture example diagram titled:

"Example: Control-Plane Orchestration Decision"

Use case:

An AI workflow platform team must decide whether control-plane orchestration should be separated from the main ticket-answering request path.
The decision affects reliability, latency, policy consistency, ownership, and operational recovery.

Image content:

Show a compact decision artifact with these areas:

- Concern: reliability, security, operability, latency
- Option A: separate control-plane orchestration
- Option B: combine orchestration with main request path
- Evidence: runtime path, failure mode, ownership, latency budget
- Decision notes: rationale, accepted risk, review trigger

Include small architecture sketches for both options using shared components:

- support portal
- gateway
- workflow service
- policy service
- queue
- model gateway
- observability

Style:

- precise architecture decision diagram
- clean vector layout
- light background
- restrained colors
- 16:9 aspect ratio
- suitable for documentation

Text rules:

- Use short labels and brief note fragments only.
- Do not include generic process explanation, slogan, or summary statement.
- Avoid dense ADR boilerplate.

Do:

- keep the decision tied to a plausible AI support workflow platform
- show both options as credible alternatives
- make the decision artifact concrete without declaring a universal answer

Do not:

- show people, desks, screens, or room interiors
- turn the image into a generic business flowchart
- use logos, real company names, or vendor-specific icons
