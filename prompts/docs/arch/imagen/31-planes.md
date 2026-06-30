---
type: image
path: /docs/arch/planes
description: Real-world example diagram showing runtime planes across a customer support AI platform.
---

# Image Generation Prompt - Planes Example

Create a clean architecture example diagram titled:

"Example: AI Support Platform as Planes"

Use case:

A customer support AI platform serves ticket-answering requests while separate runtime responsibilities manage configuration, traffic, policy, telemetry, and audit evidence.

Image content:

Show shared platform components:

- support portal
- API gateway
- orchestration service
- retrieval service
- model gateway
- policy engine
- queue
- audit store
- observability sink

Overlay four operational planes across those shared components:

- Control plane: configuration, routing, rollout controls
- Data plane: ticket request, retrieval, model response
- Policy plane: authorization, prompt policy, output checks
- Observability plane: traces, metrics, audit events

Use distinct paths or bands for each plane while keeping the same underlying components visible.

Style:

- precise technical architecture diagram
- clean vector paths and component boxes
- light background
- restrained color coding per plane
- 16:9 aspect ratio
- suitable for documentation

Text rules:

- Use short component and plane labels only.
- Do not include captions, slogans, or summary text.
- Avoid dense microtext.

Do:

- make the runtime responsibilities concrete
- keep the use case vendor-neutral
- show that multiple planes cross the same components

Do not:

- show people, desks, screens, or room interiors
- duplicate the full platform once per plane
- use cloud provider logos or brand marks
