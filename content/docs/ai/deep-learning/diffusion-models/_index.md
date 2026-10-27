---
date: "2026-10-20T09:00:00+09:00"
title: "Diffusion Models"
weight: 9
prev: "/docs/ai/deep-learning/graph-neural-networks"
next: "/docs/ai/deep-learning"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.


Diffusion models are generative models that learn to produce data by reversing a gradual corruption process. During training, noise is added to examples and a neural network learns to estimate or remove it. During generation, the model starts from noise and repeatedly denoises toward a sample from the learned data distribution.

## Forward and Reverse Processes

The forward process gradually perturbs training data, often by adding noise over a sequence of steps. The learned reverse process estimates how to move from a noisy state toward a cleaner one. Repeating the reverse steps produces a new sample; the model is not simply retrieving a stored training example.

Many image-generation systems use a compressed latent space rather than operating directly on pixels. Text or other conditioning signals can guide generation by influencing the denoising process.

## Capabilities and Tradeoffs

Diffusion models can generate detailed images and other structured outputs. Conditioning can guide content, while changes to the sampling procedure can trade off output quality, diversity, and speed.

Repeated denoising steps can make generation slower than methods that produce an output in one pass. Training and sampling require compute, and generated results can still contain errors, reflect training-data biases, or fail to follow a condition precisely. A plausible output is not evidence that its details are true.

## Relationship to Other Architectures

Diffusion is a generative modeling approach, not one fixed neural architecture. Its denoising network may use convolutional layers, transformer blocks, or combinations of components. It therefore complements architecture families such as CNNs and Transformers.

## Foundational Papers

An early diffusion-based generative approach was introduced in [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/abs/1503.03585) (2015). [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) (2020) demonstrated high-quality image synthesis and helped establish the modern diffusion-model approach.

## Summary

Diffusion models generate samples through a learned sequence of denoising steps. They have enabled flexible, high-quality generation, especially for images, while iterative sampling and resource requirements remain important tradeoffs.
