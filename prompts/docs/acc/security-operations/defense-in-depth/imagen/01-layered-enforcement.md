---
type: image
path: /docs/acc/security-operations/defense-in-depth
description: A defense-in-depth diagram showing six complementary gates around a high-risk access request and monitoring that spans the full path
---

# Image Generation Prompt — Layered Enforcement

Create a polished 1600 × 900 pixel technical illustration titled **Layered Enforcement**.

## Purpose

Create a concept-first diagram for the “Layered enforcement” section of the Defense-in-Depth Architecture page. Show that a high-risk access request is protected by multiple complementary control domains. The central message is that no single control, including authorization, is sufficient alone: combined layers reduce blast radius and enable detection and containment.

## Composition

Use one calm left-to-right request path. Place a small **High-risk request** card at the left and a small **Protected action** card at the right. Between them, place six equally emphasized, evenly spaced rounded gate cards in this exact order:

1. **Identity proofing & MFA**
2. **Device / workload trust**
3. **Network & session policy**
4. **Authorization policy**
5. **Anomaly detection & transaction monitoring**
6. **Logging, alerting & containment**

Use fine solid directional lines only. Do not use a dramatic funnel, maze, attack narrative, or make authorization the sole or final authority.

Below the full path, add a restrained horizontal band labeled **Continuous monitoring & response**. Connect it subtly to every gate and add one small feedback connection toward the earlier gates, showing that detection can initiate containment or recovery. It is a cross-cutting control, not a final step.

## Gate details

Use one simple icon and a short label per gate; do not add explanatory paragraphs.

- Identity proofing & MFA: confirm a person or workload identity with a phishing-resistant verification cue.
- Device / workload trust: assess device posture, workload attestation, or execution-state evidence.
- Network & session policy: show segmentation or session conditions without treating a perimeter as sufficient by itself.
- Authorization policy: contextually evaluate the requested action; do not emphasize allow over deny.
- Anomaly detection & transaction monitoring: identify unusual behavior, request patterns, or transaction risk.
- Logging, alerting & containment: record decisions and connect alerts to response or isolation.

## Visual style

- Clean editorial flat-vector style on a warm off-white background.
- Dark navy text and outlines; restrained blue, teal, pale indigo, and muted green. Use a quiet amber accent only for risk or alert.
- Make all gate labels readable at normal article width, with generous whitespace, consistent rounded forms, uniform icon weights, and thin solid connectors.
- Keep vendor-neutral: no product names, provider or standards logos, compliance badges, product UI, tables, or implementation configuration.
- Output 16:9 landscape, 1600 × 900 pixels, as a high-quality raster suitable for WebP conversion.

## Text to render in the image

Use only the following text, exactly as written:

- **Layered Enforcement**
- **High-risk request**
- **Identity proofing & MFA**
- **Device / workload trust**
- **Network & session policy**
- **Authorization policy**
- **Anomaly detection & transaction monitoring**
- **Logging, alerting & containment**
- **Protected action**
- **Continuous monitoring & response**

## Exclusions

- Do not depict an attacker journey, breach timeline, or kill chain.
- Do not imply a request is always allowed after an earlier gate; every gate may deny, challenge, contain, or stop it.
- Do not imply that a firewall, MFA, or authorization policy alone is complete protection.
- Do not use hooded figures, hackers, binary-code backgrounds, giant padlocks, fortress walls, server-rack photography, neon cyberpunk, glossy 3D, gradients, or watermarks.
- Do not add long explanations, screenshots, implementation steps, invented metrics, or controls beyond the six gates and monitoring band.

## Target asset

- Target page: `content/docs/acc/security-operations/defense-in-depth/_index.md`
- Suggested filename: `layered-enforcement.webp`
- Suggested title: `Layered Enforcement`
- Suggested alt text: `A high-risk access request passes through identity proofing and MFA, device or workload trust, network and session policy, authorization policy, anomaly detection and transaction monitoring, and logging with containment, while continuous monitoring and response span the full control path.`
