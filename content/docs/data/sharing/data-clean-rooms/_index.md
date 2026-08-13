---
date: "2026-08-13T00:00:00+09:00"
title: "Data Clean Rooms"
weight: 3
prev: "/docs/data/sharing/data-marketplaces"
next: "/docs/data/sharing/data-spaces"
---

A data clean room is a controlled architecture and governance pattern for deriving permitted insights from sensitive data without giving every participant unrestricted access to the underlying records.

The term describes a collaboration boundary, not one product or privacy-enhancing technology. A credible clean room states its participants, purposes, threat model, allowed computations, output controls, evidence, and responsibility boundaries.

## Why Clean Rooms Exist

Organizations may need to answer a joint question while being unable or unwilling to pool raw data conventionally. Examples include audience overlap, campaign measurement, fraud analysis, healthcare research, supply-chain coordination, and model evaluation.

Ordinary sharing may expose more data than the result requires. A clean room changes the interface: participants contribute data or make it remotely available, approved computation occurs within a constrained environment, and only authorized results leave.

## Core Control Layers

| Layer         | Responsibility                                                                    |
| ------------- | --------------------------------------------------------------------------------- |
| Participation | Identifies organizations, users, workloads, and approved purposes                 |
| Input         | Limits datasets, fields, versions, and contribution conditions                    |
| Computation   | Allows approved queries, functions, joins, models, or templates                   |
| Privacy       | Applies minimization, thresholds, suppression, noise, or cryptographic protection |
| Output        | Reviews, filters, aggregates, delays, or limits exported results                  |
| Evidence      | Records lineage, queries, decisions, versions, and released outputs               |
| Lifecycle     | Defines retention, revocation, incident handling, and termination                 |

Controls must work together. Restricting direct table access does not help if arbitrary query sequences can reconstruct individual records. Protecting inputs cryptographically does not make an unsafe aggregate suitable for release.

## Identity Matching and Join Risk

Many clean-room use cases begin by matching records that refer to the same person, household, device, business, or event. Matching can use hashed identifiers, tokens, trusted identity services, or private set intersection.

Hashing an identifier is not anonymization when the input space can be guessed or linked. Matching also creates a new relationship between datasets and can increase identifiability. The design should minimize identifiers, document match quality and bias, restrict permitted joins, and test what repeated outputs can reveal.

## Privacy-Enhancing Technologies

A clean room may use several mechanisms, but no implementation needs all of them.

- **Differential privacy** bounds how much a released result can reveal about an individual's participation, subject to an explicit privacy model and budget.
- **Secure multi-party computation** allows parties to calculate over separate inputs without revealing those inputs to one another.
- **Private set intersection** identifies common members of sets while limiting disclosure of non-matching members.
- **Homomorphic encryption** supports computation over encrypted values for selected operations, with significant performance and design tradeoffs.
- **Confidential computing** protects data in use inside a hardware-based, attested trusted execution environment.

[NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final) provides guidance for evaluating differential privacy guarantees, and the [NIST Privacy-Enhancing Cryptography project](https://csrc.nist.gov/Projects/pec) describes cryptographic mechanisms. The [Confidential Computing Consortium](https://confidentialcomputing.io/about/) defines confidential computing around hardware-based, attested trusted execution environments.

These are mechanisms, not governance decisions. A trusted execution environment can protect code and data from the host but cannot determine whether the query is appropriate or the output is too revealing.

## Threat Model

The architecture should identify which parties may be honest, curious, negligent, compromised, or actively malicious. Relevant threats include:

- a participant attempting to infer another participant's raw records
- an operator or privileged administrator accessing data in use
- repeated queries that isolate small groups
- collusion between participants
- malicious or vulnerable analysis code
- exports being combined with outside data
- stale permissions, undeleted inputs, or leaked credentials

The threat model determines whether conventional isolation is sufficient or whether cryptographic, statistical, or hardware protections are justified.

## Output Governance

Output control is often the decisive boundary. Controls may require minimum aggregation sizes, suppress rare values, limit dimensions, add noise, cap query frequency, review model artifacts, or require human approval for exceptional exports.

Outputs need provenance. Reviewers should be able to identify input versions, approved purpose, executed code or query, privacy parameters, policy decision, and recipient. Logs themselves may contain sensitive query intent and require protection.

## Operating Model

Participants need agreed roles for data preparation, policy definition, platform operation, query approval, privacy review, incident response, and audit. The operator should not silently become the universal trusted party merely because it hosts the environment.

Entry and exit procedures matter. They should address validation of contributed data, changed purposes, participant removal, credential rotation, retained outputs, and closure of the collaboration.

## Common Failure Modes

- Treating the “clean room” label as a privacy guarantee
- Allowing arbitrary queries without composition or reconstruction analysis
- Assuming hashed identifiers are anonymous
- Protecting input data but not exported results
- Using a TEE without verifying attestation, code, and key-release policy
- Ignoring model artifacts and derived data during revocation
- Collecting extensive logs without governing their sensitivity

## Summary

A data clean room narrows a sharing relationship to approved computation and controlled output. Its value comes from the combined architecture of identity, policy, isolation, privacy mechanisms, output governance, and evidence.

The design should begin with the permitted result and threat model, then choose the least data and strongest proportionate controls needed to produce that result.
