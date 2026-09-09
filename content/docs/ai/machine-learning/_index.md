---
date: "2026-08-09T09:00:00+09:00"
title: "Machine Learning"
weight: 2
prev: "/docs/ai/foundations"
next: "/docs/ai/machine-learning/learning-paradigms"
---

Machine learning became central to AI because many useful tasks are too variable to solve with fixed rules alone. Fraud patterns shift, customer behavior changes, image categories multiply, and language use never stays still. Rather than encoding every condition manually, machine learning lets systems infer useful patterns from examples and feedback.

That change did not remove the need for engineering judgment. It shifted the problem. Teams now need to reason about data quality, objective design, evaluation, generalization, and operational drift. Machine learning is therefore not only a modeling technique. It is a different way of building and maintaining behavior.

![Machine-learning lifecycle showing examples and objectives informing training, evaluation, deployment, feedback, and ongoing adaptation.](machine-learning.webp)

## Definition

Machine learning is the discipline of building systems that improve task performance by learning patterns from data. Instead of specifying every decision rule explicitly, engineers define objectives, prepare examples, choose representations, and evaluate how well the resulting model generalizes beyond the training set.

This makes machine learning a subset of AI focused on learned behavior. It is distinct from purely rule-based approaches, though real systems often combine both.

## Why Machine Learning Matters

Machine learning matters when the world contains too much variation for manual logic to scale well. Ranking search results, detecting spam, forecasting demand, classifying documents, recommending products, and recognizing speech all involve patterns that are easier to learn from data than to enumerate in rules.

The tradeoff is that learned systems are probabilistic. They do not guarantee perfect behavior. They must be judged through evidence, error analysis, and operational monitoring rather than only through code inspection.

## Topic Pages

{{< cards >}}
{{< card link="learning-paradigms/" title="Machine Learning Paradigms" icon="document-text" subtitle="Supervised, unsupervised, self-supervised, and reinforcement learning" >}}
{{< /cards >}}

## The Lifecycle of a Machine Learning System

A machine-learning system begins with data collection and problem framing. Teams need to decide what signal matters, what success looks like, and how examples will be gathered or labeled. That framing step is often more decisive than algorithm choice.

Training transforms data into a model that captures useful patterns. Validation and testing check whether the model generalizes, whether it fails systematically on important subgroups, and whether performance meets the intended use case.

Inference is the point where the model is used in a live workflow. That stage introduces new concerns such as latency, freshness, feedback loops, and the gap between offline evaluation and production behavior. Monitoring is therefore part of the lifecycle, not an afterthought.

## Common Evaluation Concepts

**Generalization** is the ability to perform well on new data rather than only memorizing the training set.

**Bias and variance** describe different failure modes. A model may be too simple to capture useful structure, or too sensitive to the training data to remain stable in production.

**Overfitting and underfitting** are practical symptoms of those problems. Overfitting means the model learns the training data too specifically. Underfitting means it never learns enough useful structure.

**Offline and online evaluation** serve different needs. Offline testing offers controlled comparison. Online behavior reveals how the model performs under real user interaction, changing inputs, and feedback loops.

## Relationship to Neighboring Topics

Deep learning is a specialized family within machine learning that uses multilayer neural architectures to learn richer representations at larger scale. Foundation models build further on those deep-learning patterns through large-scale pretraining and reuse.

MLOps operationalizes machine learning by handling versioning, deployment, monitoring, retraining, and drift management. Without that operational layer, even strong models degrade as the world changes.

## Summary

Machine learning is the part of AI concerned with building useful behavior from data rather than from exhaustive hand-authored rules. Its value comes from adaptability, but that adaptability introduces dependence on data quality, evaluation discipline, and operations. Understanding the main learning paradigms and lifecycle makes the rest of modern AI easier to reason about.
