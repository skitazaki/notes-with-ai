---
type: image
path: /docs/swe/ai-as-software-engineering-tool/coding-agents
description: Compact coding-agent architecture cover showing interaction surfaces, model access, runtime tools, connected systems, and evidence.
---

# Image Prompt — Coding Agents Architecture

## Concept

Create a clear cover diagram titled **Coding Agents**. Show a coding agent as the central orchestrator connecting people and interaction surfaces to model capability, a local or remote repository runtime, and independent engineering systems. Focus on these architectural components and their relationships; do not depict a task lifecycle.

## Layout

Use a **16:9** landscape composition, approximately 1536 × 864 pixels. Keep the agent central and make the surrounding connections easy to trace:

```text
Developer / reviewer ↔ Interaction surface ↔ Coding agent ↔ Model interaction
                                      ↕
          Local or remote runtime ↔ External systems
                    │                         │
                    └──────→ Checks and evidence ←──────┘
                                      │
                                      └──→ Developer / reviewer
```

The runtime contains the repository checkout and local tools. External systems remain outside it and connect across a visible network boundary. Keep model interaction, runtime, and external systems as distinct groups. Use only a few direct connectors.

## Visual cues

- Exact visible title: **Coding Agents**. Use no other large text.
- Show three surface alternatives with simple icons: terminal, desktop app, editor/plugin.
- Show at least two distinct model-family groups, each containing multiple separately drawn endpoint nodes (for example, Model Family A → Endpoint A1 and Endpoint A2; Model Family B → Endpoint B1 and Endpoint B2). Make clear that a family is a model grouping and an endpoint is a separately addressable serving destination; do not use one icon per family as a substitute for endpoint nodes.
- Show access pattern as a separate choice that can apply across endpoint nodes; do not imply a fixed one-to-one family/endpoint/access-pattern pairing.
- Show a bounded runtime with a repository checkout, filesystem, Git, and shell symbols. Indicate local and remote execution as alternatives.
- Show independent external systems with concise icons for issue tracker, knowledge base, hosted repository, and CI.
- Show two distinct evidence inputs converging on **Checks and evidence**: local test, build, and static-analysis results from the runtime; CI results, issue status, and review information from external systems. Draw arrows from both sources into the evidence node, then one arrow from that node to the developer/reviewer.
- Also show context and requests flowing toward the agent and tool results returning. Do not make Checks and evidence appear to receive results only from external systems.
- Show one boundary between the agent runtime and external networked systems. Do not add a task sequence.

## Style

Use a restrained editorial systems-diagram style for a professional software-engineering documentation site: warm light background, dark navy lines, and small teal and amber accents. Use simple geometric icons, strong grouping, generous space, and legible sans-serif labels. Keep the diagram readable at documentation-column width.

## Restrictions

- No subtitle, vendor/product names, logos, metrics, fake code, watermark, or decorative circuitry.
- Do not depict the model, interaction surface, runtime tools, or external services as the same component.
- Do not represent model families with icons alone while omitting explicit endpoint nodes or labels.
- Do not imply each model family has exactly one endpoint, or that each access pattern belongs to only one endpoint.
- Do not turn independent systems into a linear workflow or imply every integration is required.
- Do not add detailed permission taxonomies, collaboration patterns, or workflow stages.
- Preserve the 16:9 ratio and keep the composition compact enough to read as a cover.
