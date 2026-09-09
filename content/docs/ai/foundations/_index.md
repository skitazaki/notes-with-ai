---
date: "2026-08-09T09:00:00+09:00"
title: "Foundations"
weight: 1
prev: "/docs/ai"
next: "/docs/ai/foundations/ai-paradigms"
---

Artificial Intelligence is easiest to misunderstand when it is treated as one recent technology wave. In practice, it is a broad field formed from several traditions that each try to answer a different question about intelligent behavior. Some traditions focus on rules and reasoning, some on search and planning, some on uncertainty and probability, and some on learning patterns from data.

That broader view matters because modern AI systems are rarely explained well by one tradition alone. A retrieval-based assistant may depend on neural language models, probabilistic ranking, symbolic policy rules, and explicit workflow control at the same time. Foundations provide the conceptual map that keeps those layers distinct.

![Conceptual map of artificial intelligence, showing the relationships among rules and reasoning, search and planning, probability, and learning from data.](ai-foundations.webp)

## Definition

Artificial Intelligence is the discipline of building systems that can perform tasks associated with perception, reasoning, learning, generation, decision-making, or action. The field is broader than any single algorithm family or model architecture. It includes approaches based on explicit rules, search procedures, statistical inference, and learned representations.

The practical value of this definition is that it makes room for several valid ways of building capable systems. AI is not only machine learning, and machine learning is not only deep learning.

## Why Foundations Matter

Teams make better choices when they understand which AI tradition they are actually using. A rule-heavy domain such as access control, compliance, or deterministic workflow routing often depends on explicit logic and traceable reasoning. A perception-heavy domain such as image recognition or speech transcription often depends more on learned representations. A recommendation or ranking system may rely on statistical learning, experimentation, and optimization rather than symbolic reasoning.

Without that distinction, conversations become vague. Engineers may say they are "doing AI" when what they really mean is classification, generation, retrieval, search, forecasting, or policy automation. Foundations help turn those vague labels into design-relevant categories.

## Topic Pages

{{< cards >}}
{{< card link="ai-paradigms/" title="AI Paradigms and Boundaries" icon="document-text" subtitle="Competing traditions, field boundaries, and enduring tensions that shape AI" >}}
{{< /cards >}}

## Why This Still Matters Now

Modern AI systems combine these traditions rather than replacing them cleanly. Foundation models depend on deep learning. Retrieval systems depend on search and ranking. Governance often depends on symbolic constraints and policy logic. Agents frequently blend language generation with tool use, state tracking, planning, and approval gates.

That is why foundations remain useful. They provide the vocabulary for describing what a system is actually doing, where its strengths come from, where its limits will appear, and which neighboring disciplines must be involved to make it reliable.

## Summary

AI is not one method and not one era. It is a family of approaches for building systems that can act intelligently under different assumptions and constraints. Understanding the major traditions inside that family makes modern topics such as machine learning, foundation models, agents, and governance easier to place in context.
