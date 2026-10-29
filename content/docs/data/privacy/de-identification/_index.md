---
date: "2026-09-03T00:00:00+09:00"
title: "De-identification"
prev: "/docs/data/privacy/data-classification"
next: "/docs/data/privacy/privacy-engineering"
---

De-identification reduces the likelihood that data can be connected to a person. It can enable lower-risk analytics, testing, research, and sharing, but it is not a binary property or a permanent guarantee. Risk depends on the released data, recipients, external information, and permitted uses.

## Techniques and Trade-offs

Pseudonymization replaces identifiers with tokens while retaining a controlled way to reconnect records. It supports operations such as longitudinal analysis but remains identifiable when keys or other linking information exist. Generalization reduces precision; suppression removes risky values; aggregation reports groups; perturbation adds controlled uncertainty. Synthetic data models patterns without distributing source records, although memorization and rare combinations still require testing.

Anonymization aims to make identification no longer reasonably likely in the relevant context. Removing names alone is insufficient because quasi-identifiers such as age, location, and timestamps can become unique when combined.

## Evaluate the Release Context

Define the intended recipients, environment, purpose, auxiliary data, and consequences of re-identification. Test singling out, linkability, inference, rare records, and model leakage. Balance privacy risk against utility; a transformed dataset that cannot support its stated purpose encourages unsafe workarounds.

## Layered Controls

Combine transformation with contracts, purpose limits, access restrictions, query controls, output review, monitoring, and retention. Protect tokenization keys separately. Reassess releases when external datasets, recipients, algorithms, or intended uses change.

## Summary

De-identification is a risk-reduction process, not a label applied once. Choose techniques for a defined threat and use context, validate their limits, and support them with governance and security controls.
