---
date: "2026-10-20T09:00:00+09:00"
title: "Transformers"
weight: 4
prev: "/docs/ai/deep-learning/recurrent-neural-networks"
next: "/docs/ai/deep-learning/autoencoders"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.


Transformers are neural architectures that use attention to relate elements in a sequence. They became a general-purpose foundation for language, code, image, audio, and multimodal models because the same architecture can represent relationships across many kinds of tokens or patches.

## Attention and Context

Attention lets each position compute a weighted view of other positions. This gives a model a flexible way to use context, such as linking a pronoun to an earlier noun or relating distant parts of an image. Self-attention computes these relationships within one input sequence; cross-attention connects two sequences, such as text instructions and image features.

Transformers usually combine attention with feed-forward layers, residual connections, normalization, and positional information. Positional information matters because attention alone does not encode the order of sequence elements.

## Common Designs

- **Encoder-style models** build contextual representations of an input and are useful for classification and retrieval.
- **Decoder-style models** predict the next element and support text generation and other autoregressive tasks.
- **Encoder-decoder models** transform one sequence into another, as in translation or conditional generation.

These are common patterns rather than strict limits. Modern systems combine transformer blocks with other components, including retrieval, tools, or modality-specific encoders.

## Strengths and Tradeoffs

Transformers train efficiently in parallel across sequence positions and can model long-range relationships. Their flexible representation supports transfer across tasks and modalities.

The cost of attention and memory generally grows with sequence length, making long-context processing expensive. Transformers also depend on large, representative training data and can reproduce its gaps and biases. Architecture alone does not guarantee factuality, interpretability, or reliable behavior.

## Relationship to Other Topics

Transformers are one family of neural architecture, not a synonym for deep learning. Mixture of Experts (MoE) can be used inside transformer layers to activate only selected feed-forward experts for each token. Diffusion systems may also use transformer blocks to process image patches or other structured inputs.

## Foundational Paper

The Transformer architecture was introduced in [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017).

## Summary

Transformers use attention to build context-dependent representations and have become a flexible backbone for sequence and multimodal learning. Their capabilities come with compute, memory, and data requirements that shape how they are trained and used.
