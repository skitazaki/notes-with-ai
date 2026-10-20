---
date: "2026-10-20T09:00:00+09:00"
title: "Recurrent Neural Networks, LSTMs, and GRUs"
weight: 3
prev: "/docs/ai/deep-learning/convolutional-neural-networks"
next: "/docs/ai/deep-learning/transformers"
---

Recurrent neural networks (RNNs) process a sequence one step at a time while carrying a hidden state forward. The state provides a compact summary of earlier inputs, allowing the model's output at each step to depend on sequence history.

## Recurrent State

At each time step, an RNN combines the current input with its previous hidden state to produce an updated state and, optionally, an output. The same parameters are reused across steps, which makes the architecture naturally suited to variable-length sequences.

Vanilla RNNs can struggle to learn dependencies over long intervals because training signals may weaken or grow across many steps. Long Short-Term Memory (LSTM) networks and Gated Recurrent Units (GRUs) add gates that regulate how information is retained, updated, or exposed. These mechanisms improve the handling of longer dependencies but do not remove every limitation.

## Uses and Tradeoffs

RNNs and their gated variants have been used for language, speech, time series, and streaming tasks. Processing inputs sequentially can be useful when the input arrives over time or when maintaining a running state is important.

Sequential computation limits parallelism across positions during training and inference. This can make long sequences slower to process than with architectures that handle positions more independently. Transformers and state space models offer different tradeoffs for sequence modeling.

## Summary

RNNs represent sequence history through a recurrent hidden state. LSTMs and GRUs use gates to manage that state and improve learning over longer intervals, while retaining the sequential nature of recurrent computation.
