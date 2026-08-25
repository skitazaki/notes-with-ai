---
type: image
path: /docs/data/architecture/modern-data-architecture
description: Conceptual graph of interacting capabilities in a heterogeneous modern data estate.
---

# Image Generation Prompt - Modern Data Architecture Capabilities

Create a polished 1672 × 941 pixels (16:9) technical infographic titled exactly **Modern Data Architecture**.

Communicate one clear idea: a modern data estate is a graph of interacting capabilities, not one mandatory pipeline or one central technology. Show how diverse sources, movement mechanisms, storage and processing capabilities, serving interfaces, and consumers form several coordinated paths under shared controls.

## Composition

Use a spacious left-to-right capability graph with six main areas. Keep **Sources**, **Movement**, **Serving**, and **Consumers** on the primary horizontal axis. Between **Movement** and **Serving**, stack **Storage** above **Processing** as two parallel capability areas:

```text
                          ┌→ Storage ────┐
Sources → Movement ───────┤      ↕       ├→ Serving → Consumers
                          └→ Processing ─┘
```

Do not reproduce this text diagram literally. Create a balanced editorial composition with restrained arrows and clear grouping. The upper path should show movement into storage before serving. The lower path should show movement directly into processing and then serving, making it immediately clear that streaming and similar flows can skip storage. Use the vertical bidirectional relationship between **Storage** and **Processing** to show that processing may read from or write to storage without collapsing them into one sequential pipeline.

Render the six areas with these exact headings and contents:

### 1. Sources

**Applications · SaaS · Files · Events · External Data**

Use a compact cluster of source symbols rather than a single database icon.

### 2. Movement

**Batch · APIs · CDC · Messaging · Streaming**

Use a directional exchange or routing symbol.

### 3. Storage

**Object Storage · Warehouse · Lakehouse · Specialized Stores**

Use a grouped storage symbol that suggests several fit-for-purpose stores without depicting vendor products.

### 4. Processing

**Batch Processing · Stream Processing · Orchestration**

Use a transformation or coordinated-processing symbol.

### 5. Serving

**SQL · Semantic Layer · APIs · Search · Features · Data Products**

Use an interface or access-layer symbol.

### 6. Consumers

**BI · Applications · ML · Generative AI**

Use a compact set of consumption or outcome symbols.

## Required Relationships

Show exactly these primary relationships:

- **Sources → Movement**
- **Movement → Storage**
- **Movement → Processing**
- **Storage ↔ Processing**
- **Storage → Serving**
- **Processing → Serving**
- **Serving → Consumers**

Place **Storage** directly above **Processing** and make their vertical bidirectional relationship visually distinct. Branch **Movement** into both areas and converge both areas into **Serving**. The lower **Movement → Processing → Serving** path must remain visually continuous so readers can recognize a path that bypasses storage. The graph should reveal multiple valid paths through the estate while remaining easy to scan. Do not add arrows that are not listed above.

## Cross-Cutting Capabilities

Place one continuous, visually quiet control layer beneath **Movement**, **Storage**, **Processing**, and **Serving**. Label it exactly **Cross-Cutting Capabilities** and include exactly these terms:

**Metadata · Reliability · Lineage · Security · Governance · Observability**

Use a shared underlay to show that these capabilities apply across the four central areas. Do not depict them as another sequential stage, separate perimeter callouts, or six independent control boxes.

## Visual Direction

Match the established Notes with AI illustration style: solid opaque white or very light neutral background, large dark-navy title, crisp sans-serif typography, flat vector graphics, thin consistent outlines, restrained geometric shapes, subtle pale fills, generous whitespace, strong alignment, and minimal shadows. Use coordinated blue, teal, green, orange, and purple accents to distinguish capability areas without making them look like unrelated product cards.

Keep the capability graph more prominent than the individual examples. Make all headings and labels legible at documentation-column width. Render every specified title, heading, content line, and cross-cutting term exactly once and exactly as written.

The image must feel like a conceptual map of interoperating capabilities. It must not imply that every organization needs every capability, that data always follows one end-to-end route, or that the diagram is a prescribed target topology.

Do not add vendor names, product logos, cloud-provider symbols, people, architecture-pattern labels, implementation instructions, detailed pipelines, extra databases, dashboards, robots, decorative AI imagery, dense prose, photorealism, 3D effects, gradients, watermarks, or a second title.
