---
type: image
path: /docs/acc/landscape
description: An English conceptual diagram of an access control architecture composed of four complementary layers: identity, decision, enforcement, and governance
---

# Image Generation Prompt — Four Layers of Access Control

Create a polished 1600 × 900 pixel technical illustration titled **Four Layers of Access Control**.

## Purpose

Create a conceptual diagram that supports the “Practical landscape” section of the Access Control Landscape page.

Show modern access control as an architecture of four layers that answer different questions while complementing one another—not as a single product or a linear authorization flow. Readers should be able to understand at a glance that establishing identity, making decisions, enforcing decisions, and governing the system are all necessary, and that no one layer is sufficient on its own.

## Composition

Place four large rounded layers of equal width in a vertical stack at the center of a warm off-white canvas. Each layer is an interdependent control domain supporting an access request, not an independent processing step. Leave generous space between layers and use only fine, short connector lines to suggest their relationship. Do not use heavy arrows, numbered steps, or a decision tree.

Place the title at the top, followed by the four layers in this exact order:

1. **Identity layer**
2. **Decision layer**
3. **Enforcement layer**
4. **Governance layer**

At the right of the stack, add a small, restrained vertical annotation reading **Consistent trust and accountability** to convey the intention spanning all four layers. Do not make it appear to be a fifth layer or a downstream step.

## Layer content

### Identity layer

The top layer establishes who or what is requesting access. Include three small, neutral icons representing a person, a workload, and an AI agent. Use restrained supporting symbols for identity proofing, lifecycle, authentication, and federation.

### Decision layer

The second layer evaluates whether an access request should be allowed. Put a simple policy-evaluation symbol at its center, surrounded by four small input elements for roles, attributes, relationships, and risk signals. Do not overemphasize an allow-or-deny outcome; show that the decision depends on context.

### Enforcement layer

The third layer puts decisions into effect at real access boundaries. Represent applications, API gateways, service mesh, databases, SaaS, and runtime environments with a small set of simple icons. Make clear that policy decisions are applied consistently in these places, without drawing a direct path from a principal to a resource.

### Governance layer

The bottom layer supports the correctness and continuing review of access control. Represent review, audit, testing, exception handling, and incident response with balanced small icons and short labels. Show this as a control domain that continuously validates and improves the three layers above, not as a log archive alone.

## Visual style

- Use a clean, editorial flat-vector style; do not use realistic people or UI screenshots.
- Use dark navy text and outlines. Distinguish the layers with blue, teal, pale indigo, and restrained green; do not use alarming, saturated warning colors.
- Make the four layer headings the most legible elements. Supporting labels must remain readable at normal article width.
- Keep corner radii and line weights consistent across all cards, icons, and lines; use generous whitespace.
- Remain vendor-neutral. Do not add product names, cloud-provider logos, standards logos, or compliance badges.
- Produce a 16:9 landscape, 1600 × 900 pixel, high-quality raster image suitable for WebP conversion.

## Text to render in the image

Use only the following text, exactly as written:

- **Four Layers of Access Control**
- **Identity layer**
- **Identity proofing**
- **Lifecycle**
- **Authentication**
- **Federation**
- **Decision layer**
- **Policy**
- **Roles**
- **Attributes**
- **Relationships**
- **Risk signals**
- **Enforcement layer**
- **Applications**
- **API gateways**
- **Service mesh**
- **Databases**
- **SaaS**
- **Runtime environments**
- **Governance layer**
- **Review**
- **Audit**
- **Testing**
- **Exception handling**
- **Incident response**
- **Consistent trust and accountability**

## Exclusions

- Do not depict the four layers as a workflow executed in order from top to bottom.
- Do not imply that authentication alone grants access.
- Do not make one central product, key, shield, login screen, or lock the dominant visual subject.
- Do not use hooded figures, hackers, binary-code backgrounds, server-rack photography, giant padlocks, neon cyberpunk styling, glossy 3D treatment, excessive shadows, gradients, or watermarks.
- Do not add long explanatory copy, comparison tables, product logos, standards names, expanded acronyms, invented metrics, or numbers.

## Target asset

- Target page: `content/docs/acc/landscape/_index.md`
- Suggested filename: `access-control-layers.webp`
- Suggested title: `Four Layers of Access Control`
- Suggested alt text: `Conceptual diagram of a modern access control architecture with four complementary layers: identity, decision, enforcement, and governance.`
