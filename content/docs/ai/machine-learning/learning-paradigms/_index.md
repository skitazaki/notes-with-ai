---
date: "2026-09-09T09:00:00+09:00"
title: "Machine Learning Paradigms"
weight: 1
prev: "/docs/ai/machine-learning"
next: "/docs/ai/machine-learning"
---

Machine Learning Paradigms provides a conceptual framework for supervised, unsupervised, self-supervised, and reinforcement learning. It focuses on durable ideas for design and decision-making rather than particular products or implementation steps.

## Main Learning Paradigms

### Supervised Learning

Supervised learning uses labeled examples. The system sees inputs together with desired outputs and learns a function that maps one to the other. Classification, regression, ranking, and many prediction tasks follow this pattern.

It works well when labels are meaningful and representative, but quality depends heavily on the data definition and the target being learned.

### Unsupervised Learning

Unsupervised learning looks for structure without explicit target labels. Clustering, segmentation, dimensionality reduction, and anomaly discovery are common examples. The system is not told the answer directly. It is asked to uncover useful organization in the data.

This is powerful for exploration, but usefulness depends on how the discovered structure connects to actual business or product decisions.

### Self-Supervised Learning

Self-supervised learning creates training signals from the data itself. Predicting masked words, next tokens, missing patches, or other internal structure allows models to learn broad representations without fully human-labeled datasets. This pattern became especially important in large language and multimodal models.

Its significance is architectural as much as statistical. It makes large-scale pretraining economically and operationally viable.

### Reinforcement Learning

Reinforcement learning focuses on action and feedback over time. The system interacts with an environment, receives rewards or penalties, and learns policies that improve cumulative outcomes. It is useful when decisions affect future states, such as control systems, game play, scheduling, or sequential optimization.

The core challenge is that feedback is delayed and exploration can be costly or risky.

## Comparing Learning Paradigms

The following comparison highlights the different signals, uses, and limits of the main learning paradigms.

| Paradigm        | Main signal                          | Typical use                                 | Strength                                  | Common limit                                |
| --------------- | ------------------------------------ | ------------------------------------------- | ----------------------------------------- | ------------------------------------------- |
| Supervised      | Human-provided labels                | Classification, regression, ranking         | Clear objective alignment                 | Label cost and label bias                   |
| Unsupervised    | Structure within the data            | Clustering, anomaly discovery, segmentation | Useful for exploration and representation | Harder to tie directly to business outcomes |
| Self-supervised | Signals derived from the data itself | Pretraining and representation learning     | Scales to large unlabelled corpora        | Needs downstream adaptation and evaluation  |
| Reinforcement   | Reward from sequential interaction   | Control, planning, optimization             | Learns behavior over time                 | Sample efficiency and stability challenges  |

## Summary

Understanding machine learning paradigms makes it possible to place individual methods and technologies in context according to their role, assumptions, and tradeoffs.
