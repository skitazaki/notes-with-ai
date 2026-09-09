---
date: "2026-09-09T09:00:00+09:00"
title: "Errors, Error Correction, and Fault Tolerance"
weight: 4
prev: "/docs/quantum-computing/algorithms-and-advantage"
next: "/docs/quantum-computing/hybrid-systems"
---

Quantum information is fragile. Unwanted interaction with the environment, imperfect control, state preparation errors, and measurement errors all reduce the reliability of a computation. Because unknown quantum states cannot simply be copied and inspected, error management differs fundamentally from classical redundancy.

The path from noisy experiments to dependable quantum computation involves three related but distinct ideas: characterization, error mitigation, and quantum error correction.

## Sources of Error

**Decoherence** is the loss of useful quantum behavior through interaction with the environment. **Control errors** occur when a pulse or gate differs from its intended operation. **Readout errors** distort measurement results. Leakage can move a physical system outside the states used as the computational basis, while crosstalk causes operations on one part of a device to affect another.

Errors can also be correlated across qubits or over time. Such correlations matter because many error-correction analyses assume noise with particular statistical properties. A low average error rate does not fully describe a system if rare correlated events dominate failures.

## Characterization and Calibration

Before errors can be managed, a platform must estimate how the device behaves. Calibration tunes controls and measurements. Characterization protocols estimate quantities such as gate fidelity, coherence, crosstalk, and readout quality. Continuous monitoring is needed because device behavior drifts.

These measurements are not interchangeable. A benchmark that summarizes one aspect of a processor may not predict performance for every circuit. Application-relevant tests should therefore complement component-level metrics.

## Error Mitigation

**Quantum error mitigation** reduces bias in results without creating fully protected logical qubits. Techniques may estimate the zero-noise result from several noisy executions, learn and invert readout errors, discard results that violate known symmetries, or use randomized transformations to make noise easier to model.

Mitigation can improve estimates for limited workloads, but it has costs. It often requires more circuit executions, relies on assumptions about noise, and may scale poorly as circuits deepen. It does not make an arbitrary noisy computation reliable.

## Quantum Error Correction

Quantum error correction encodes logical information across multiple physical qubits. Carefully designed measurements reveal information about errors without directly revealing the protected logical state. A decoder interprets these **syndrome** measurements and determines which corrective action or tracked update is required.

A code has a **distance** related to the number of physical errors it can detect or correct. If physical operations are below a suitable threshold and the code is scaled appropriately, increasing the code distance can suppress logical error rates. This is the central mechanism behind scalable fault tolerance.

## Fault-Tolerant Computation

Error correction protects stored information; **fault tolerance** extends that protection to the entire computation. State preparation, logical gates, measurement, decoding, and control must be designed so that a limited physical fault does not spread into an uncorrectable logical failure.

The resource cost can be large. One logical qubit may require many physical qubits, and some logical operations require additional prepared states, verification, and classical decoding. Resource estimates should therefore state the target logical error rate, algorithm size, code assumptions, and physical error model.

## What Progress Should Be Measured

Useful progress indicators connect physical improvements to logical behavior:

- physical operation and measurement error rates;
- stability and correlation of noise over time;
- logical error rate as code size increases;
- speed and accuracy of syndrome extraction and decoding;
- number and quality of logical operations completed;
- total physical, control, cooling, and runtime overhead.

A demonstration of an encoded qubit is important, but a useful fault-tolerant system also needs scalable logical operations and an architecture that can sustain them.

## Summary

Noise is not one problem with one remedy. Characterization identifies device behavior, mitigation improves selected noisy estimates, and error correction protects logical information. Fault tolerance integrates these ideas into a complete computational architecture. The decisive milestone is not merely more physical qubits, but increasingly reliable logical computation at manageable system cost.
