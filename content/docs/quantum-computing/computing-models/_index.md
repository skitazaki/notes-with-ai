---
date: "2026-09-09T09:00:00+09:00"
title: "Computing Models and Hardware"
weight: 2
prev: "/docs/quantum-computing/foundations"
next: "/docs/quantum-computing/algorithms-and-advantage"
---

Quantum computers are built through several computing models and physical architectures. These choices are related but distinct: a computing model defines how a problem is expressed, while a hardware modality defines how quantum information is physically stored, controlled, and measured.

Keeping the two levels separate makes comparisons more useful. A platform should not be judged by qubit count alone, and a computing model should not be confused with one vendor or device type.

## Gate-Based Quantum Computing

The gate-based model expresses computation as a sequence of operations on qubits. It is the closest quantum counterpart to a general programmable computer. Quantum circuits can represent a wide range of algorithms, and sufficiently controlled gates can approximate any unitary transformation relevant to computation.

Gate-based machines appear in two broad regimes. **Noisy intermediate-scale quantum** systems execute relatively shallow circuits without full error correction. **Fault-tolerant** systems use encoded logical qubits and error-correction procedures to support much deeper, more reliable computations. The latter requires substantial physical resources for each logical qubit.

## Quantum Annealing

Quantum annealing frames a problem as the search for a low-energy configuration of a physical system. It is specialized for optimization and sampling rather than universal circuit execution. A problem must be mapped to an objective function and connectivity that the machine can implement.

Annealing can be useful as an experimental optimization method, but comparisons with classical solvers must include encoding overhead, solution quality, runtime, and the strength of the classical baseline. Its specialized character is a design choice, not a lesser form of gate-based computing.

## Analog Quantum Simulation

Analog quantum simulators engineer one controllable quantum system to reproduce the behavior of another. They are especially relevant to quantum many-body physics, materials, and dynamics that are difficult to model classically. Instead of compiling a general circuit, researchers tune interactions and observe the resulting evolution.

Their strength is direct access to particular physical models at useful scales. Their limitation is programmability: a device may be excellent for one family of simulations and unsuitable for unrelated workloads.

## Major Hardware Modalities

| Modality                 | Qubit or carrier                         | Typical strengths                                             | Central engineering challenges                         |
| ------------------------ | ---------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| Superconducting circuits | Electrical states in fabricated circuits | Fast gates and mature fabrication techniques                  | Cryogenic control, coherence, and wiring at scale      |
| Trapped ions             | Internal states of confined ions         | High-fidelity operations and flexible connectivity            | Gate speed, optical control, and scaling traps         |
| Neutral atoms            | Atoms arranged with optical tweezers     | Large configurable arrays and natural interactions            | Uniform control, loss, and operation fidelity          |
| Photonics                | States of individual photons             | Communication compatibility and room-temperature transmission | Deterministic sources, loss, and feed-forward control  |
| Spin qubits              | Electron or nuclear spins                | Small physical footprint and semiconductor compatibility      | Uniform fabrication and precise control                |
| Topological approaches   | States protected by nonlocal properties  | Potentially lower error sensitivity                           | Demonstrating and controlling suitable physical states |

No modality dominates every dimension. Gate fidelity, connectivity, coherence time, operation speed, fabrication yield, control complexity, and measurement quality all interact.

## Physical and Logical Qubits

A **physical qubit** is an implemented quantum degree of freedom. A **logical qubit** is encoded across multiple physical qubits so that errors can be detected and corrected. This distinction makes raw qubit counts insufficient for comparing progress toward useful fault-tolerant computation.

Relevant system measures include the quality and speed of operations, the error-correction threshold, the overhead required per logical qubit, and the number of reliable logical operations a machine can perform. Application performance ultimately depends on the complete system, including compilation and classical control.

## Choosing the Right Comparison

Hardware evaluation should start with a workload and execution model. A chemistry simulation, a constrained optimization problem, and a distributed quantum communication experiment may require different capabilities. Useful questions include:

- Can the problem be represented naturally on the machine?
- How much routing or encoding overhead is required?
- How deep can the computation run at acceptable accuracy?
- What classical resources are needed around the processor?
- Which metric predicts application-level quality rather than laboratory scale alone?

## Summary

Quantum computing includes universal gate-based systems, specialized annealers, and analog simulators. Each can be realized through different physical modalities with distinct tradeoffs. Meaningful evaluation connects computing model, hardware quality, error-management strategy, and target workload instead of relying on a single headline metric.
