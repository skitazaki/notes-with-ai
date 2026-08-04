---
type: docs
path: /docs/ai
---

Write a comprehensive documentation hub titled:
"Artificial Intelligence (AI)"

You are a senior AI architect and technical writer
creating a section landing page for a large AI documentation library.

This page is not a textbook and should not attempt to teach every AI topic in depth.
Treat it as the top-level overview for a section that will have many child pages.
Its job is to establish the conceptual map, explain how the section is organized, and direct readers toward deeper pages that will be written later.

Audience:

- Software architects, data engineers, platform engineers, AI engineers, and experienced developers
- Technical leaders and enterprise architects who need a stable mental map of the AI landscape
- Readers want orientation and navigation, not implementation guidance

Purpose:

- Explain what Artificial Intelligence encompasses
- Organize a very broad ecosystem into understandable categories
- Help readers quickly locate the topic they are looking for
- Show relationships between technologies rather than presenting isolated definitions
- Distinguish foundational concepts from implementation technologies
- Provide a durable mental map that remains useful as the field evolves

Scope:

- Focus on organizing the AI landscape, not exhaustively teaching each topic
- Treat the page as a section landing page that explicitly anticipates future child pages
- Emphasize enduring concepts, categories, and relationships over transient tools or products
- Cover both foundational disciplines and modern engineering concerns
- Leave room for deeper follow-up pages instead of trying to resolve every subtopic here

Tone & style:

- Clear, structured, vendor-neutral, and technically accurate
- Approachable and concise without oversimplifying
- Neutral, explanatory, and practical
- Avoid hype, marketing language, and trend-chasing

Structure:

1. Orientation

Open with a short explanation of what AI is, why the field has become so broad, and why understanding the ecosystem is more valuable than memorizing tools.
Introduce AI as a collection of connected disciplines rather than a single technology.

2. AI as a documentation section

Explain why AI should be treated as a documentation library rather than one long article.
Clarify that AI overlaps with adjacent domains such as software architecture, software engineering, data, security, and governance.

3. Core organizing lenses

Provide a concise framework for how the documentation is organized.
For example, explain that readers may approach AI through lenses such as:

- foundations
- learning and models
- data and context
- engineering and operations
- governance and risk
- applications and platforms

Show that these lenses overlap.

4. The main domains in this library

Organize the section into major child-page domains. Include, at minimum, the following top-level areas:

- Foundations
- Machine Learning
- Deep Learning
- Foundation Models
- Generative AI
- AI Engineering
- AI Infrastructure
- Data for AI
- MLOps and LLMOps
- Responsible AI
- Enterprise AI
- AI Applications

Within each domain, briefly explain:

- what the domain covers
- why it matters in the broader AI landscape
- how it relates to neighboring domains
- which representative subtopics belong there

Use examples such as the following to make the taxonomy concrete without becoming exhaustive:

- Foundations: history, AI vs. ML vs. deep learning, symbolic AI, statistical learning, neural networks, probabilistic methods, cognitive systems
- Machine Learning: supervised learning, unsupervised learning, reinforcement learning, feature engineering, training, evaluation, optimization
- Deep Learning: CNNs, RNNs, LSTMs, transformers, diffusion models, representation learning
- Foundation Models: large language models, vision models, speech models, multimodal models, embeddings, tokenization
- Generative AI: prompt engineering, context engineering, RAG, fine-tuning, agents, agentic systems, tool calling, structured outputs, memory, planning, reasoning
- AI Engineering: AI applications, APIs, SDKs, frameworks, evaluation, testing, deployment, versioning
- AI Infrastructure: GPUs, accelerators, distributed training, inference, vector databases, model serving, AI gateways, caching, orchestration
- Data for AI: data engineering, data quality, data governance, knowledge graphs, metadata, embeddings, synthetic data, labeling
- MLOps and LLMOps: CI/CD, experiment tracking, model registry, monitoring, drift detection, evaluation pipelines, continuous improvement
- Responsible AI: ethics, fairness, explainability, privacy, security, compliance, governance, AI safety
- Enterprise AI: AI platforms, enterprise architecture, integration, identity, security, cost management, operations, organizational models
- AI Applications: software development, search, customer support, healthcare, manufacturing, finance, robotics, scientific discovery

5. Relationships across the landscape

Show how major areas depend on and build on each other.
Include examples such as:

- LLMs rely on transformer architectures
- RAG combines retrieval systems with foundation models
- AI agents build on language models plus planning and tool execution
- MLOps supports production ML systems
- LLMOps extends MLOps for foundation-model-based systems
- Governance spans every stage of the AI lifecycle

Encourage internal cross-navigation between related sections.

6. Recommended reading flow

Add a section that explicitly positions this page as the entry point to a future documentation tree.
Include a recommended reading flow using navigation cards for future child pages.
It is acceptable to label the destination pages as TBD when the child pages do not exist yet.

Include cards or planned destinations for the main domains above.

7. Suggested starting points

Provide concise navigation guidance for different reader intents, such as:

- conceptual orientation
- building modern AI applications
- operating production AI systems
- enterprise governance and risk

8. Summary

Conclude by reinforcing that AI evolves rapidly while the documentation structure should remain stable by organizing knowledge around enduring concepts and clearly separated child domains.

Output requirements:

- Write the page in Markdown
- Use hierarchical headings and short explanatory paragraphs
- Use concise tables where appropriate
- Include navigation-oriented prose rather than a long encyclopedic survey
- Include a card-based reading flow that points to future child pages
- Make the result feel like a section landing page that can grow into a larger documentation tree

Constraints:

- Do not turn the page into a textbook or tutorial
- Do not provide implementation steps or vendor comparisons
- Do not center the document on current products, frameworks, or market hype
- Do not try to fully explain every major AI subtopic on this page
- Keep the emphasis on information architecture, orientation, and durable conceptual structure
- Preserve space and clarity for future child pages to carry the detailed explanations
