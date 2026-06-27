---
type: docs
path: /docs/arch/planes
---

Write a concise reference page titled:
"Planes"

You are a senior software architect and platform engineering writer explaining planes as an operational architecture concept.

Audience:

- Platform engineers
- Cloud architects
- SREs
- Backend engineers
- Technical leaders

Purpose:

- Explain why planes exist as an architecture model
- Clarify the difference between structural layers and operational planes
- Help readers understand control, data, observability, workflow, and policy planes

Core message:

Planes represent operational behavior and responsibility.
They help teams reason about how work is controlled, executed, observed, governed, or routed across structural boundaries.

Scope:

- Cover control plane, data plane, management plane, observability plane, policy plane, and workflow plane
- Explain why planes often cut across layers, services, and teams
- Use examples from cloud platforms, Kubernetes, service meshes, data platforms, and AI agent systems

Tone and style:

- Precise, practical, and architecture-focused
- Avoid vendor-specific framing unless used as a brief example
- Make the distinction from layers very clear

Structure:

1. Definition
   - Define a plane as an operational slice of a system organized around a type of runtime responsibility.

2. Why planes exist
   - Explain that planes help answer:
     - Who controls execution?
     - Who processes traffic or data?
     - Which path handles operations, policy, telemetry, or orchestration?
     - Which concerns cross structural boundaries?

3. Common planes
   - Control plane
   - Data plane
   - Management plane
   - Observability plane
   - Policy plane
   - Workflow plane

4. Planes versus layers
   - Explain that layers describe structural dependency, while planes describe operational behavior.
   - Include a comparison table.

5. Example: cloud-native or AI platform
   - Show how control, data, observability, and policy planes operate across the same platform.
   - Mention that an image should appear here showing planes crossing structural layers.

6. Common mistakes
   - Treating every subsystem as a plane
   - Using plane terminology for static organization charts
   - Hiding reliability or security concerns behind vague plane labels
   - Confusing control paths with user request paths

Constraints:

- Do not include implementation instructions for Kubernetes, service mesh, or cloud services.
- Do not include image-generation instructions.
- Keep examples vendor-neutral.
