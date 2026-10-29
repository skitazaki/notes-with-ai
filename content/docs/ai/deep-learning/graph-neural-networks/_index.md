---
date: "2026-10-20T09:00:00+09:00"
title: "Graph Neural Networks"
weight: 8
prev: "/docs/ai/deep-learning/state-space-models"
next: "/docs/ai/deep-learning/diffusion-models"
---

Graph neural networks (GNNs) are neural models for data represented as entities and relationships. A graph can describe social connections, molecules, knowledge, infrastructure, or interactions among items. GNNs use both node features and graph structure to produce representations or predictions.

## Message Passing

Many GNNs update each node by combining its own representation with information aggregated from neighboring nodes. Repeating this process lets information travel across multiple edges, so a node representation can reflect a wider neighborhood. Graph convolutional networks are one influential family within this broader approach.

The graph's edges and node features encode assumptions about which entities should influence one another. Those assumptions matter: an incomplete or noisy graph can lead to unhelpful representations, and repeated aggregation can blur differences between nodes.

## Tasks and Tradeoffs

GNNs support node classification, link prediction, graph classification, and ranking or recommendation problems. They are useful when relationships are part of the signal rather than incidental metadata.

Large or highly connected graphs can make neighborhood aggregation expensive. Handling changes in the graph, sparse features, and relationships across distant nodes also requires deliberate design. A graph representation does not by itself establish causal relationships between connected entities.

## Foundational Paper

The paper [The Graph Neural Network Model](https://doi.org/10.1109/TNN.2008.2005605) (published in 2009) explicitly proposed a neural network model for data represented in graph domains.

## Summary

GNNs learn from both entity attributes and relationships by propagating information through graph neighborhoods. They are a natural fit for relational data, with effectiveness tied to the quality and meaning of the graph structure.
