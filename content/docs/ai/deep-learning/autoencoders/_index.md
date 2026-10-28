---
date: "2026-10-20T09:00:00+09:00"
title: "Autoencoders"
weight: 5
prev: "/docs/ai/deep-learning/transformers"
next: "/docs/ai/deep-learning/mixture-of-experts"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.

Autoencoders are neural networks trained to reconstruct their inputs. An encoder maps an input into a representation, often called a latent code, and a decoder uses that representation to produce a reconstruction. By constraining the representation or the model, training can encourage the network to capture useful structure rather than simply copy the input.

## Compression and Reconstruction

The encoder and decoder are trained together so the reconstruction remains similar to the original input. A narrow latent representation is one way to create a bottleneck, but denoising objectives, sparsity constraints, or probabilistic latent variables can shape what the model learns in other ways.

The learned representation depends on the data, architecture, objective, and constraints. A compact code is not automatically meaningful or useful for every downstream task.

## Variants and Uses

Autoencoders have been used for dimensionality reduction, representation learning, denoising, and anomaly detection. Variational autoencoders use a probabilistic latent representation and can support generation. Sparse autoencoders constrain activations and are also studied as a way to analyze features in neural networks, including language models.

Reconstruction quality alone does not guarantee that the latent representation captures the properties a user cares about. Anomaly detection based on reconstruction error, for example, can miss unusual cases that the model reconstructs well.

## Foundational Paper

An influential demonstration of deep autoencoders for dimensionality reduction is [Reducing the Dimensionality of Data with Neural Networks](https://doi.org/10.1126/science.1127647) (2006).

## Summary

Autoencoders learn representations through an encoder-decoder reconstruction task. Their usefulness depends on how the objective and constraints shape those representations for the intended analysis or downstream use.
