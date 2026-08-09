---
type: docs
path: /docs/ai/mlops-and-llmops
---

Write a concise reference page titled:
"MLOps and LLMOps"

You are a senior ML platform engineer and technical writer explaining how model-centric systems are delivered, monitored, governed, and continuously improved after initial development.

Audience:

- ML engineers, AI platform engineers, software architects, and technical leaders
- Readers who need a practical operating model for production AI systems

Purpose:

- Define MLOps and LLMOps as operational disciplines
- Explain the shared lifecycle concerns across classic ML and foundation-model-based systems
- Clarify where LLMOps extends or changes established MLOps practices

Core message:

MLOps and LLMOps bring software delivery discipline to probabilistic systems whose behavior depends on data, models, prompts, context, and runtime feedback.

Scope:

- Cover experiment tracking, model registries, CI/CD, deployment governance, observability, drift detection, evaluation pipelines, prompt and configuration management, and continuous improvement
- Contrast classic predictive-model operations with large-model application operations
- Explain why evaluation and monitoring are broader for foundation-model systems

Tone and style:

- Practical, neutral, and operations-oriented
- Clear enough for experienced software and platform readers
- Focus on operating models rather than vendor tooling

Structure:

1. Definition
   - Define MLOps and LLMOps and explain why the paired framing is useful.

2. Why operations matter
   - Explain why model deployment is the start of operational responsibility, not the end.

3. Core MLOps concerns
   - Experiments
   - Versioning
   - Deployment
   - Monitoring
   - Drift and retraining

4. How LLMOps extends the picture
   - Prompt and context management
   - Retrieval quality
   - Safety evaluation
   - Human feedback loops
   - Cost and latency governance

5. Shared and distinct failure modes
   - Include a concise comparison table between MLOps and LLMOps concerns.

6. Relationship to engineering and governance
   - Explain how operations connect product engineering, platform controls, and responsible AI.

Output requirements:

- Write the page in Markdown.
- Include frontmatter with the page title and `weight: 9`.
- Use headings and one concise comparison table.

Constraints:

- Do not turn the page into a tooling landscape survey.
- Do not present LLMOps as a complete replacement for MLOps.
- Do not provide pipeline implementation steps.
