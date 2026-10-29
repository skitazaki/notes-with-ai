---
date: "2026-10-20T09:00:00+09:00"
title: "Mixture of Experts (MoE)"
weight: 6
prev: "/docs/ai/deep-learning/autoencoders"
next: "/docs/ai/deep-learning/state-space-models"
---

Mixture of Experts (MoE) is a model design that combines multiple expert networks with a routing mechanism. For each input, the router selects a subset of experts to process it. This conditional computation can increase a model's total parameter capacity without requiring every parameter to be active for every input.

## Experts and Routing

An expert is typically a feed-forward neural network. A router scores the input, often at the token level, and sends it to one or more experts. The selected experts process the input, and their outputs are combined, sometimes using the router's scores as weights.

Experts are learned components rather than manually assigned subject specialists. Training may lead them to respond differently to patterns in the data, but their roles are not necessarily clean or human-interpretable.

## Why Use MoE

In a dense model, most model layers are activated for each token. In a sparse MoE layer, only a small number of experts are selected. This can provide a larger parameter pool while limiting the computation performed per token. MoE therefore offers a way to scale model capacity when computation per example is a constraint.

## Costs and Design Challenges

MoE shifts some costs rather than removing them. All expert parameters still need to be stored or made available, so memory, checkpoint, and serving requirements can remain high. Routing also adds communication between devices when experts are distributed across accelerators.

Training must keep the workload reasonably balanced across experts. If routing sends too many tokens to a few experts, those experts become bottlenecks while others are underused. Capacity limits, auxiliary balancing objectives, and routing choices can help, but they add design and operational complexity. Results depend on the model, training setup, and serving environment; sparse activation does not guarantee lower end-to-end cost.

## Relationship to Transformers

MoE is a design pattern that can be applied to parts of a neural network, rather than a standalone architecture family with one fixed structure. A common approach replaces the feed-forward sublayer in selected transformer blocks with a set of experts and a router. Attention may remain dense while expert computation is sparse.

## Foundational Papers

The original mixture-of-experts formulation was presented in [Adaptive Mixtures of Local Experts](https://doi.org/10.1162/NECO.1991.3.1.79) (1991). The sparsely gated layer used to scale neural networks through conditional computation was introduced in [Outrageously Large Neural Networks](https://arxiv.org/abs/1701.06538) (2017).

## Summary

MoE uses input-dependent routing to activate a subset of expert networks. It can expand model capacity without proportionally increasing per-token computation, while introducing memory, communication, load-balancing, and serving tradeoffs.
