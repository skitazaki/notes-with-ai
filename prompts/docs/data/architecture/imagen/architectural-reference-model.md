---
type: image
path: /docs/data/architecture
description: Reference model showing the main data flow from sources to consumers, supported by a cross-cutting control plane.
---

# Image Generation Prompt - Data Architecture Reference Model

Create a polished 1672 × 941 pixels (16:9) technical infographic titled exactly **Data Architecture Reference Model**.

Communicate one clear idea: data commonly moves from sources through integration, storage and processing, and serving interfaces to consumers, while a shared control plane applies across every stage. Present the model as a useful architectural lens, not as a mandatory linear pipeline.

## Composition

Use a clear left-to-right flow with exactly five equal conceptual stages:

**Sources → Ingestion & Integration → Storage & Processing → Serving & Semantic Access → Consumers**

Give each stage a distinct bounded area with one simple icon and the following concise labels:

### 1. Sources

- **Applications**
- **Operational Databases**
- **SaaS & APIs**
- **Events, Devices & External Data**

### 2. Ingestion & Integration

- **Batch & Files**
- **CDC & Replication**
- **APIs & Messaging**
- **Event Streaming**

### 3. Storage & Processing

- **Warehouse, Lake & Lakehouse**
- **Stream Processing**
- **Specialized Databases**

### 4. Serving & Semantic Access

- **SQL & Semantic Layers**
- **APIs & Data Products**
- **Search, Features & AI Context**

### 5. Consumers

- **Analytics**
- **Applications**
- **ML & AI Agents**
- **Other Systems**

Connect adjacent stages with restrained directional arrows. Keep the arrows secondary to the stage headings and make the overall flow easy to scan at documentation-column width.

## Cross-Cutting Control Plane

Place one continuous horizontal foundation beneath all five stages. Label it exactly **Cross-Cutting Control Plane** and include exactly these terms:

**Metadata · Governance · Security · Privacy · Reliability · Observability**

Use a shared underlay to show that the control plane applies to every stage and creates enforcement points at multiple boundaries. Do not depict it as a sixth sequential stage or a final downstream step.

## Non-Linear Architecture Cues

The primary structure should remain left to right, but add no more than three thin, understated bypass cues to show that the model is not a mandatory pipeline:

- a request may move from a source directly to serving
- a stream may feed a consumer directly
- a federated query may reach a source at consumption time

Do not label these bypass cues with explanatory sentences. Use restrained visual paths that remain clearly subordinate to the primary flow.

## Visual Direction

Match the established Notes with AI illustration style: solid opaque white or very light neutral background, large dark-navy title, crisp sans-serif typography, flat vector graphics, thin consistent outlines, subtle pale fills, restrained blue, teal, green, orange, and purple accents, generous whitespace, strong alignment, and minimal shadows.

Use one coherent visual system for all five stages. Keep icons abstract and recognizable, text large enough to read at article width, and the control plane visually quieter than the main flow. Render every specified title, stage heading, item label, and control-plane term exactly once and exactly as written.

Do not add vendor or product logos, cloud-provider symbols, people, architecture-pattern names, implementation instructions, code, detailed schemas, decorative networks, dense explanatory prose, photorealism, 3D effects, gradients, watermarks, or a second title. Do not make every connection equally prominent, and do not imply that every data flow must pass through all five stages.
