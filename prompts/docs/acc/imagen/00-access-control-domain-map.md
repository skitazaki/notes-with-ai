---
type: image
path: /docs/acc
description: A restrained conceptual map showing how principals, identity context, policy decisions, enforcement, protected resources, governance, and audit form an access-control system.
---

# Image Generation Prompt — Access Control Map

Create a polished 1536 × 1024 pixel technical illustration titled **Access Control**.

## Purpose

Create a calm, concept-first hero image that maps access control itself, not the documentation or article structure.

Show how access control determines whether a principal may perform an action on a protected resource. Identity and context inform a policy decision, enforcement applies the result, and governance plus monitoring make the system accountable and adaptable.

The image should orient the reader without summarizing every model, technology, risk, or implementation pattern.

## Reference Images and Precedence

Use these generated images as visual references:

- English reference: `/Users/skitazaki/Downloads/ChatGPT Image 2026年9月6日 12_46_14.png`
- Japanese reference: `/Users/skitazaki/Downloads/ChatGPT Image 2026年9月6日 12_46_10.png`

Use the **English reference as the base** for the overall composition, proportions, five primary cards, information density, icon treatment, typography scale, and policy-decision detail.

Use the **Japanese reference only as the authority for the outer perimeter treatment**. The requested result is not a blend of both layouts: preserve the English structure, but replace its dashed outer enclosure with the Japanese-style perimeter described below.

## Composition

Use one clear left-to-right decision flow with generous whitespace:

**Principals → Identity & Context → Policy Decision → Enforcement → Protected Resources**

### Principals

Show three compact, equally weighted principal types:

- **Human**
- **Workload**
- **AI Agent**

Group them under **Principals**. They request an action but do not connect directly to protected resources.

### Identity & Context

Show a stage that establishes who or what the principal is and captures relevant conditions. Use simple visual cues for identity, device or workload posture, environment, and request context.

### Policy Decision

Place **Policy Decision** at the visual center and make it the strongest focal point. Suggest that the decision evaluates the principal, requested action, target resource, and context. Represent the result as a restrained **Allow** or **Deny** outcome without using a table or formula.

### Enforcement

Place **Enforcement** immediately after the decision. Make clear that it mediates the requested action and prevents direct, unchecked access.

### Protected Resources

Show a small group of protected resources such as an application, API, data store, and tool under **Protected Resources**.

### Cross-Cutting Controls

Place two quiet horizontal bands beneath or around the complete flow:

- **Governance & Lifecycle** — ownership, least privilege, review, and revocation
- **Monitoring & Audit** — decision records, observability, anomaly detection, and response

These controls must visibly span the complete system rather than appear as final downstream steps.

### Outer Perimeter

Follow the Japanese reference for the outer perimeter:

- Use one continuous, thin, pale-blue solid rounded enclosure around the five-stage decision flow and both cross-cutting control bands.
- Use large, smooth corner radii so the perimeter reads as a calm protective boundary, not as another content panel.
- Center the small shield-and-lock emblem on the top edge. Let the top border visually meet or pass behind the emblem, as in the Japanese reference.
- Keep the perimeter unlabelled and visually secondary to the five-stage flow.
- Do not place arrowheads on the perimeter.
- Do not use the English reference's blue dotted perimeter, dotted return arrows, or dotted side connections.

The solid outer enclosure suggests defense in depth. Do not expand it into a separate layered-defense diagram.

## Visual Hierarchy and Style

- Make the policy decision the central focal point.
- Give human, workload, and AI-agent identities equal visual weight.
- Use icons only as supporting cues for the exact labels.
- Keep all labels legible at normal article width.
- Use a clean flat-vector editorial style with a warm off-white background.
- Use dark navy typography and outlines, a restrained blue and teal palette, and one muted accent for the decision result.
- Use consistent rounded geometry, uniform line weight, solid connectors, generous whitespace, and minimal text.
- Make the pale-blue solid outer perimeter lighter and thinner than the dark-blue card outlines and primary flow arrows.
- Keep the image vendor-neutral with no product logos or cloud branding.
- Output 1536 × 1024 pixels, 3:2 landscape, as a high-quality raster suitable for conversion to WebP.

## Required Text

Use only these exact labels:

- **Access Control**
- **Principals**
- **Human**
- **Workload**
- **AI Agent**
- **Identity & Context**
- **Policy Decision**
- **Action**
- **Allow**
- **Deny**
- **Enforcement**
- **Protected Resources**
- **Governance & Lifecycle**
- **Monitoring & Audit**

Do not add a subtitle, definition, caption, acronym expansion, product name, standard name, or explanatory paragraph inside the image.

## Do Not

- Depict the documentation hierarchy or use labels such as Introduction or Reference Materials.
- Divide the canvas into numbered article sections.
- Add comparison tables, maturity levels, long control lists, lifecycle diagrams, risk catalogs, standards, or technologies.
- Connect principals directly to resources without a decision and enforcement boundary.
- Use a dotted, dashed, segmented, or arrowed outer perimeter.
- Imply that authentication alone grants access.
- Make AI the dominant subject; it is one principal type among several.
- Use tiny text, long captions, crossed connectors, dotted lines, excessive arrows, glossy 3D, photorealistic people, stock-business imagery, neon cyberpunk styling, logos, watermarks, or interface screenshots.

## Intended Asset

- Target page: `content/docs/acc/_index.md`
- Suggested filename: `access-control-map.webp`
- Suggested title: `Access Control`
- Suggested alt text: `Access control map showing human, workload, and AI-agent principals passing through identity and context, a central policy decision, and enforcement before reaching protected resources, with governance and audit spanning the system.`
