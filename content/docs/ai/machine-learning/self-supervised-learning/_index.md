---
date: "2026-10-19T09:00:00+09:00"
title: "Self-Supervised Learning"
weight: 4
prev: "/docs/ai/machine-learning/unsupervised-learning"
next: "/docs/ai/machine-learning/reinforcement-learning"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.


Self-supervised learning trains a model using targets generated from the input data itself. It turns an unlabeled collection into prediction tasks, allowing a model to learn patterns and representations without manually annotating every example. The resulting model is usually a starting point for later use, rather than proof that a downstream task has been solved.

## How the learning signal is created

A training objective hides, transforms, or relates parts of an example and asks the model to predict a useful target. A language model may predict the next token or recover masked content. An image model may learn that two transformed views come from the same image, or predict missing image regions. Audio and time-series models can predict future segments or align related views.

The objective determines which regularities the model is encouraged to represent. A model trained to predict nearby words may capture syntax and associations, but this does not ensure that its outputs are factually correct. Data coverage, objective design, and evaluation all influence which capabilities emerge.

## Pretraining and adaptation

Self-supervised learning is often used for pretraining on large unlabeled corpora. The learned parameters can then be adapted to a narrower task with labeled examples, parameter-efficient updates, or a task-specific prediction head. In other settings, embeddings from the pretrained model are used for retrieval, clustering, or similarity comparison.

Pretraining can reduce the amount of labeled data needed for a downstream task, but does not eliminate task-specific evaluation. A representation useful for one population or domain may transfer poorly to another. Adaptation can also change model behavior, so evaluation should cover the final system and its intended context.

## Relationship to unsupervised learning

Self-supervised learning is often discussed alongside unsupervised learning because neither requires human-provided labels for every example. The distinction is that self-supervised methods construct explicit targets from the data, while unsupervised methods more broadly seek structure without a supplied target. Terminology varies across disciplines, so it is useful to state the learning signal being used.

## Applications and limitations

Language, image, speech, and multimodal foundation models commonly use self-supervised objectives to learn reusable representations from large corpora. Domain-specific systems can use the same idea when unlabeled data is abundant but annotation is expensive, such as logs, medical signals, industrial imagery, or scientific measurements.

Large-scale pretraining requires substantial compute and data governance. Unlabeled data can still contain private information, duplication, harmful content, and historical biases. Models may reproduce those patterns. Training success on a proxy objective is not evidence of safety, factuality, or fitness for a particular use; downstream tests and operational safeguards remain necessary.

## Summary

Self-supervised learning derives training targets from the data to learn reusable representations without manual labels for every example. Its value depends on the objective, data, and quality of downstream adaptation and evaluation.
