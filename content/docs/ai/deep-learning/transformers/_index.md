---
date: "2026-11-26T10:39:00+09:00"
title: "Transformers"
weight: 4
prev: "/docs/ai/deep-learning/recurrent-neural-networks"
next: "/docs/ai/deep-learning/autoencoders"
---

Transformers are neural architectures that use attention to relate elements in a sequence. They became a general-purpose foundation for language, code, image, audio, and multimodal models because the same architecture can represent relationships across many kinds of tokens or patches.

## Attention and Context

Attention lets each position compute a weighted view of other positions. This gives a model a flexible way to use context, such as linking a pronoun to an earlier noun or relating distant parts of an image. Self-attention computes these relationships within one input sequence; cross-attention connects two sequences, such as text instructions and image features.

Transformers usually combine attention with feed-forward layers, residual connections, normalization, and positional information. Positional information matters because attention alone does not encode the order of sequence elements.

## Query, Key, and Value

Self-attention starts with a representation for each input token. Learned linear projections transform each representation into a **query (Q)**, **key (K)**, and **value (V)**:

`Q = XW_Q,quad K = XW_K,quad V = XW_V`

A query represents what a position is looking for, a key represents what it can be matched on, and a value carries the information that can be mixed into the output. These are useful intuitions rather than literal roles assigned by the model.

Scaled dot-product attention compares queries with keys, normalizes the scores, and uses the resulting weights to combine values:

`Attention(Q,K,V)=softmax(QK^T/\sqrt{d_k}+M)V`

Here, `d_k` is the key dimension and `M` is an optional mask. In causal self-attention, the mask prevents a token from attending to future positions. Multi-head attention performs this operation in multiple learned subspaces and combines the head outputs.

## KV Cache During Generation

Autoregressive models generate one token at a time. At each decoding step, the model needs the keys and values of earlier tokens so the new query can attend to the preceding context. Without a cache, those earlier key and value projections would be recomputed repeatedly.

A **KV cache** stores the keys and values produced by previous tokens in each attention layer. When a new token is generated, the model computes its new query, key, and value, appends the new key and value to the cache, and attends to the cached entries allowed by the attention mask. The cache stores K and V, not the attention weights or the final attention outputs.

Caching avoids repeated projection and attention computation for past tokens, making incremental decoding much more practical. It does not make the cache free: memory grows with the number of cached tokens, layers, KV heads, and head dimension. A simplified estimate for an uncompressed cache is:

`2 × layers × tokens × KV-heads × head-dimension × bytes-per-element`

The factor of two accounts for keys and values. Actual memory also depends on allocation, padding, quantization, and cache implementation. Grouped-query attention (GQA) and multi-query attention (MQA) reduce the number of KV heads shared by query heads, lowering cache size and memory bandwidth. Multi-head Latent Attention (MLA) compresses the KV representation into a latent vector and is another approach to reducing cache storage.

KV caching is an inference technique, not a change to which token positions attention can access. Sparse attention changes that interaction pattern; it can reduce cache reads, while a KV cache avoids recomputing past K and V. They can be used together.

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

For methods that reduce the token interactions computed by attention, see [Sparse Attention](sparse-attention/). Sparse attention is distinct from KV caching: one restricts attention connections, while the other reuses past key and value projections during decoding.

## Foundational Paper

The Transformer architecture was introduced in [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017).

## Summary

Transformers use attention to build context-dependent representations and have become a flexible backbone for sequence and multimodal learning. Query, key, and value projections explain how attention compares and combines token information; the KV cache makes autoregressive generation practical by retaining past keys and values. Their capabilities come with compute, memory, and data requirements that shape how they are trained and used.
