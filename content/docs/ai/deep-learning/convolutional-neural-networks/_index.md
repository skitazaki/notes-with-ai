---
date: "2026-10-20T09:00:00+09:00"
title: "Convolutional Neural Networks"
weight: 2
prev: "/docs/ai/deep-learning/neural-architectures"
next: "/docs/ai/deep-learning/recurrent-neural-networks"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.

Convolutional neural networks (CNNs) are neural architectures designed to use local structure in data. They became especially influential in computer vision, where nearby pixels are more closely related than distant ones and the same visual pattern can appear in different parts of an image.

## Convolution and Shared Weights

A convolutional layer applies learned filters across local regions. Because the same filter is reused at different positions, the model can detect a pattern wherever it appears while using fewer parameters than a fully connected layer over the entire input. Stacking convolutional layers lets the network combine simple local features into more complex patterns.

Pooling or strided operations may reduce spatial resolution and aggregate information across larger regions. Modern vision networks vary in how they use these operations, and many combine convolution with attention or other components.

## Strengths and Limits

CNNs provide an effective inductive bias for images and other grid-like signals: local patterns matter, and nearby regions have meaningful relationships. They can be computationally efficient and useful in settings that benefit from spatial locality.

The same design can make global relationships less direct to represent than local ones. CNNs are not limited to images, but applying them to data without meaningful neighborhood structure may offer little benefit. Their performance also depends on training data, objective, and architecture choices.

## Foundational Paper

[Gradient-Based Learning Applied to Document Recognition](https://doi.org/10.1109/5.726791) (1998) is a classic account of convolutional networks and their application to handwritten document recognition.

## Summary

CNNs use local filters and shared weights to learn spatial features at multiple levels. They remain useful when the structure of the input is local and grid-like, and can be combined with other neural components when broader context is needed.
