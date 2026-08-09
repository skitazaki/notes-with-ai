---
type: docs
path: /docs/ai/foundation-models
---

Write a concise reference page titled:
"Foundation Models"

You are a senior AI systems architect and technical writer explaining large reusable model families that can be adapted across many downstream tasks.

Audience:

- AI engineers, platform engineers, software architects, and senior technical leaders
- Readers who need a stable conceptual model for modern large-model systems

Purpose:

- Define foundation models and explain why they changed AI system design
- Clarify their reuse, adaptation, and modality patterns
- Distinguish foundation models from narrower task-specific models and from generative AI applications

Core message:

Foundation models are broad reusable model bases whose value comes from transferable capabilities, adaptation patterns, and ecosystem leverage across many tasks.

Scope:

- Cover language, vision, speech, code, embedding, and multimodal model families
- Explain pretraining, adaptation, prompting, fine-tuning, embeddings, tokenization, and transfer at a high level
- Clarify why these models reshape application architecture, infrastructure, and governance

Tone and style:

- Neutral, precise, and architecture-aware
- Practical rather than hype-driven
- Suitable for long-lived documentation

Structure:

1. Definition
   - Define foundation models and why they are considered reusable bases.

2. Why they matter
   - Explain reuse, transfer, broad capability surfaces, and ecosystem effects.

3. Main model families
   - Large language models
   - Vision models
   - Speech models
   - Code models
   - Multimodal models
   - Embedding models

4. Core enabling concepts
   - Pretraining
   - Tokenization
   - Embeddings
   - Adaptation and fine-tuning
   - In-context use

5. Architectural implications
   - Explain why application logic shifts toward retrieval, orchestration, evaluation, and control layers.

6. Relationship to generative AI
   - Clarify that foundation models are the reusable substrate, while generative AI describes a broader application pattern built on top of them.

Output requirements:

- Write the page in Markdown.
- Include frontmatter with the page title and `weight: 4`.
- Use headings and one concise table comparing major model families.

Constraints:

- Do not center the page on a list of vendors or current commercial offerings.
- Do not reduce the topic to language models only.
- Do not provide implementation steps for fine-tuning or serving.
