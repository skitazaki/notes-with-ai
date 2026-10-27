---
date: "2026-10-22T09:00:00+09:00"
title: "Generative Models and Deep Learning"
weight: 2
prev: "/docs/ai/generative-ai/system-patterns"
next: "/docs/ai/generative-ai"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.


Generative models and deep learning describe different aspects of machine learning. Generative modeling is concerned with learning patterns in data so a model can produce new samples. Deep learning uses neural networks with multiple layers to learn representations and relationships in data. Many generative models use deep learning, but the terms describe different things: one refers to a model's purpose, the other to a family of methods.

Generative adversarial networks (GANs) combine both. They are generative models trained using two neural networks in competition, and those networks are commonly deep neural networks.

## Two Different Ways to Classify a Model

Generative modeling classifies a model by its objective. A generative model learns a data distribution or a process for producing samples that resemble data from that distribution. It can generate images, text, audio, or other data, depending on its design.

Deep learning classifies methods by how they represent and learn patterns. A deep neural network uses multiple layers of learned transformations. Such networks can support prediction, classification, representation learning, or generation; generation is only one possible use.

| Question                         | Generative modeling                                                  | Deep learning                                                   |
| -------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------- |
| What does the category describe? | The goal of learning to produce new samples                          | Methods based on neural networks with multiple layers           |
| Does it always imply the other?  | No. Generative models can use other approaches                       | No. Deep networks can also classify, predict, or learn features |
| Examples                         | GANs, variational autoencoders, autoregressive, and diffusion models | CNNs, Transformers, and recurrent neural networks               |

The categories overlap when a deep neural network is trained to generate data. In that case, "generative" describes what the model is for, and "deep learning" describes how it is built or trained.

## Generative Adversarial Networks

A GAN consists of two neural networks trained in opposition. The generator maps a latent input, often sampled from a simple distribution, to a synthetic example. The discriminator receives real and generated examples and learns to distinguish them. Training updates both networks: the discriminator improves its judgments, while the generator learns to produce examples that the discriminator is more likely to mistake for real data.

The competition between the generator and discriminator gives GANs their name and training objective. Because the networks learn from data through multiple layers, GANs are also a deep-learning approach. This illustrates the distinction: "generative" describes the kind of model, while "deep learning" describes how its networks learn.

GANs are not the only way to generate data with deep learning. Variational autoencoders learn a latent-variable model and decode samples from it. Autoregressive models predict data elements sequentially. Diffusion models learn to reverse a gradual corruption process. These families differ in their learning objectives, sampling processes, and characteristic tradeoffs.

## Generative Models and Generative AI Systems

A generative model produces samples based on patterns learned from data. A generative AI system is a broader application that uses a model together with instructions, input context, user interaction, tools, and controls. A GAN can provide the generation capability within such a system; the application also includes the components that make the model useful in a particular setting.

Modern generative AI often uses foundation models, including large language and multimodal models. These models commonly use deep neural architectures and generate outputs. However, not every generative model is a foundation model, and not every deep-learning model is generative. The terms refer to different levels: the application, the model's purpose, and the methods used to build and train it.

## Summary

Generative modeling describes the task of learning to produce data, while deep learning describes methods based on multilayer neural networks. GANs bring the two together: they learn to generate samples by training a generator and discriminator in competition. Generative AI systems can use such models alongside the context and controls needed for an application.
