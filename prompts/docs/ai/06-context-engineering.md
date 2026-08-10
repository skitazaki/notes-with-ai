---
type: docs
path: /docs/ai/context-engineering
---

Write a concise reference page titled:
"Context Engineering"

You are a senior AI systems architect and technical writer explaining how teams deliberately design the information available to a foundation-model application at runtime.

Audience:

- AI engineers, software engineers, data engineers, platform teams, and technical leaders
- Readers who understand generative AI basics and need a durable systems view beyond prompt wording

Purpose:

- Define context engineering as a systems discipline, not a synonym for prompt engineering or RAG
- Explain the types of runtime information that shape model behavior and how they are managed
- Give readers a clear boundary between context engineering, Data for AI, and AI Engineering

Core message:

Context engineering is the deliberate selection, structuring, delivery, evaluation, and lifecycle control of the task-relevant information a model can use at runtime.

Scope:

- Cover instructions, user and task state, conversation history, retrieved evidence, memory, tool outputs, policy and authorization context
- Explain relevance, sufficiency, precedence, freshness, provenance, token budget, isolation, and traceability as design principles
- Cover the lifecycle: acquire, select, transform, assemble, deliver, evaluate, refresh or remove
- Explain common failure modes including missing, stale, conflicting, excessive, poisoned, and cross-tenant context
- Relate the topic to prompting, RAG, agents, Data for AI, AI Engineering, and Responsible AI

Child-topic boundaries:

- Keep the parent page as the conceptual hub.
- Treat **Memory in AI Systems** as the controlled retention and reuse of context across interactions.
- Treat **Retrieval-Augmented Generation** as the runtime retrieval and assembly of external evidence.
- Treat **Tools and Model Context Protocol** as the controlled integration of external context and actions through tool interfaces and MCP.
- Avoid duplicating the detailed coverage assigned to those child pages.

Tone and style:

- Neutral, precise, concept-first, and vendor-agnostic
- Useful as stable documentation rather than an implementation playbook
- Use plain language; define specialized terms before relying on them

Structure:

1. Definition
2. Why context engineering matters
3. What counts as context
4. Core design principles
5. Context lifecycle
6. Failure modes and controls
7. Relationship to adjacent topics
8. Summary

Output requirements:

- Write Markdown with front matter using `title: "Context Engineering"`, `weight: 6`, `prev: "/docs/ai/generative-ai"`, and `next: "/docs/ai/ai-engineering"`.
- Include one concise table that maps context sources to their system role and representative risk.
- Reference the hero image as `context-engineering.webp` with useful alt text.

Constraints:

- Do not reduce the topic to crafting prompts, vector databases, or context-window size.
- Do not prescribe a particular framework, model vendor, or implementation architecture.
- Do not present retrieved content as inherently trustworthy.
