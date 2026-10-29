---
date: "2026-09-09T09:00:00+09:00"
title: "Foundations"
weight: 1
prev: "/docs/quantum-computing"
next: "/docs/quantum-computing/computing-models"
---

Quantum computing is a model of computation in which information is represented and transformed according to quantum mechanics. It does not make every calculation faster. Its value comes from arranging a computation so that superposition, entanglement, and interference change how the relevant solution space is explored.

This page introduces the minimum conceptual model needed to reason about quantum systems without treating them as mysterious or as faster versions of classical computers.

## Quantum Information

A classical bit records one of two values, 0 or 1. A **qubit** is a physical quantum system described by a state that can be expressed as a combination of basis states, commonly written as |0⟩ and |1⟩. The coefficients in that combination are amplitudes. Their squared magnitudes determine the probabilities of measurement outcomes.

This distinction is important: a qubit does not expose both values as ordinary data that can be read simultaneously. Measurement produces a classical result and generally changes the state. Quantum algorithms must therefore shape amplitudes before measurement so that useful outcomes become more likely.

## The Core Phenomena

### Superposition

Superposition allows a quantum state to contain amplitudes for multiple basis states. With several qubits, the state space grows exponentially with the number of qubits. This gives quantum algorithms a rich mathematical space in which to operate, but it does not provide a way to read every possible value at once.

### Entanglement

Entanglement describes correlations that cannot be represented as independent states for each qubit. It lets a quantum circuit manipulate relationships across a system as a whole. Entanglement is a computational resource in many algorithms, but more entanglement is not automatically better; it must support the structure of the problem.

### Interference

Quantum amplitudes can reinforce or cancel one another. Algorithms use **interference** to increase the probability of useful measurement outcomes and suppress unhelpful ones. This is the mechanism that turns a large state space into a computational advantage: the algorithm must guide the evolution of the state, not merely create superposition.

### Measurement

Measurement converts quantum information into a classical outcome. Because one execution normally yields only a sample, a circuit is often run many times to estimate a probability distribution or expectation value. The number of repetitions affects both precision and total execution cost.

## Gates, Circuits, and Execution

In the gate-based model, a program is expressed as a **quantum circuit**. The circuit prepares qubits, applies reversible quantum gates, and measures selected qubits. Single-qubit gates rotate individual states. Multi-qubit gates create conditional behavior and entanglement.

A simplified execution loop is:

1. Prepare an initial state.
2. Apply a sequence of quantum gates.
3. Measure the result.
4. Repeat the circuit to collect samples.
5. Process the samples with classical software.

Real workflows also include circuit compilation, mapping logical operations to available hardware, calibration-aware scheduling, and error mitigation or correction.

## What Quantum Parallelism Does Not Mean

The phrase _quantum parallelism_ can suggest that a quantum computer evaluates every input and returns every answer. That is misleading. A circuit can transform amplitudes associated with many basis states, but measurement exposes limited classical information. A useful quantum algorithm needs mathematical structure that allows interference to concentrate probability around an answer that can be extracted efficiently.

This is why quantum computing is specialized. Problems benefit only when they can be encoded into a quantum process with a favorable end-to-end cost, including state preparation, repeated execution, and classical post-processing.

## Quantum and Classical Systems

Quantum processors are accelerators, not replacements for conventional computers. Classical systems prepare inputs, compile and schedule circuits, control hardware, analyze measurements, and integrate results into applications. Even a fault-tolerant quantum computer will operate within a larger classical system.

The practical question is therefore not “quantum or classical?” It is which part of a workload, if any, has structure that a quantum method can exploit while the rest remains classical.

## Summary

Quantum computation works by preparing quantum states, transforming their amplitudes through gates and interference, and extracting limited classical information through measurement. Superposition provides the state space, entanglement represents nonclassical correlations, and interference shapes the probability of outcomes. Together they enable particular computational strategies, not universal acceleration.
