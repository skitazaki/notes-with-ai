---
type: image
path: /docs/ai/mlops-and-llmops
description: Conceptual overview figure for the MLOps and LLMOps topic page, showing the shared operational lifecycle and the extra concerns introduced by foundation-model systems.
---

# Image Generation Prompt - MLOps and LLMOps

Create a publication-quality conceptual illustration titled:

"MLOps and LLMOps"

Purpose:

Help readers compare the shared operational lifecycle of model systems and the broader operating surface introduced by large-language-model applications.

Core message:

Both MLOps and LLMOps bring lifecycle discipline to probabilistic systems, but LLM-centered systems add prompts, retrieval, safety, and runtime composition as operational concerns.

Composition:

- Create a paired lifecycle diagram: two parallel loops that meet at a clearly labeled shared operational backbone in the center.
- The left loop, **MLOps**, represents the lifecycle of a purpose-built predictive model. Show these distinct inputs and activities in that lane:
  - Training data and feature/data quality
  - Model training and experiment tracking
  - Model registry, release, and prediction-quality monitoring
- The right loop, **LLMOps**, represents the lifecycle of an application assembled around a foundation model. Show these distinct inputs and activities in that lane:
  - Prompt and model-configuration versioning
  - Retrieval corpus/index quality and grounding
  - Safety and output-quality evaluation
  - Runtime cost, latency, and human-feedback signals
- Put the shared stages on the center backbone, visibly applying to both lanes:
  - Versioning and release
  - Deployment
  - Monitoring
  - Evaluation
  - Continuous improvement
- Make the distinction legible at a glance: MLOps optimizes a trained model and its data; LLMOps operates a composed application whose behavior also depends on prompts, retrieval, guardrails, and inference-time choices.
- Use connected overlays on the LLMOps loop rather than isolated badges, so the extra concerns visibly affect runtime behavior and feed back into evaluation.

Alternative composition if the paired loops become crowded:

- Use one shared horizontal lifecycle pipeline with an **MLOps** row above and an **LLMOps additions** row below. Attach each LLMOps addition to the lifecycle stage it changes.
- Or use a nested composition: an MLOps lifecycle ring as the foundation, with an outer LLMOps ring labeled "application composition and runtime controls." Keep the outer ring visibly additive rather than a replacement.

Style:

- precise editorial infographic
- vector-style lifecycle diagram
- light background
- clear loop arrows and minimal text
- coordinated dual-lane color system
- 16:9 aspect ratio

Do:

- make shared concerns and distinct concerns easy to compare
- keep the image simple enough to read in seconds
- emphasize operational discipline rather than tooling

Do not:

- turn the figure into a detailed CI/CD pipeline
- imply that LLMOps replaces MLOps entirely
- use vendor logos or product badges
