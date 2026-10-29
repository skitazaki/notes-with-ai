---
date: "2026-10-20T09:00:00+09:00"
title: "State Space Models"
weight: 7
prev: "/docs/ai/deep-learning/mixture-of-experts"
next: "/docs/ai/deep-learning/graph-neural-networks"
---

State space models (SSMs) represent a sequence through a hidden state that evolves as new inputs arrive. In deep learning, structured state space models use parameterized state transitions to capture long-range sequence relationships while aiming to keep computation manageable for long inputs.

## State and Sequence Processing

At a high level, an SSM maps an input sequence into a sequence of latent states and outputs. The state summarizes information from earlier positions. Structured variants constrain the transition dynamics so they can be computed efficiently, including through parallel or convolution-like formulations during training.

The term covers a range of methods. Their internal parameterizations, training algorithms, and practical behavior differ, so “state space model” does not identify one interchangeable architecture.

## Strengths and Tradeoffs

SSMs can offer efficient handling of long sequences and can maintain a compact state as inputs arrive. This makes them a useful point of comparison with recurrent networks and attention-based Transformers.

Efficiency depends on the model and workload. Some tasks benefit from direct content-based interactions between distant positions, while other sequence patterns can be represented effectively through state evolution. SSMs and Transformers therefore involve different inductive biases and engineering tradeoffs rather than a universal winner.

## Foundational Paper

An influential modern deep-learning sequence model based on structured state spaces is S4, introduced in [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396) (2021). State space models themselves predate this work and are not attributed to a single deep-learning paper.

## Summary

Deep-learning SSMs use structured latent-state dynamics to model sequences. They provide an alternative family for long-sequence processing, with behavior and efficiency determined by the specific model design and task.
