---
date: "2026-08-30T00:00:00+09:00"
title: "Responsible Data Collection"
weight: 5
prev: "/docs/data/collection/external-and-third-party-data"
next: "/docs/data/engineering"
---

Responsible Data Collection applies governance, privacy, security, and accountability when deciding whether and how data should be collected. Its purpose is not to reproduce those disciplines, but to bring their questions to the earliest point—before collection creates risk, obligations, expectations, and copies that may be difficult to reverse.

## A Collection Decision

Before approving collection, establish:

1. **Purpose:** What specific outcome or decision requires the data, and which uses are outside scope?
2. **Necessity and proportionality:** Is the data needed, and is the detail, population, frequency, and duration proportionate to the purpose and impact?
3. **Authority:** Who is permitted to authorize collection, and what legal, contractual, policy, consent, or other basis applies?
4. **Transparency:** What should affected people, source owners, providers, and users understand about the collection and its consequences?
5. **Protection and lifecycle:** How will sensitivity, access, retention, correction, withdrawal, deletion, and incident response be handled?
6. **Accountability:** Who owns the source relationship, collection design, dataset, review, and evidence?

A technically accessible field is not automatically appropriate to collect. Conversely, authorization to collect does not remove the need to secure the data, limit use, or maintain its quality and context.

## Minimize at the Source

Data minimization is most effective before capture. It can limit fields, precision, frequency, observation windows, population, identifiability, or retention. Collecting broad data and filtering it later still creates exposure during capture, transfer, landing, backup, and incident response.

Minimization is purpose-dependent. Exact location may be necessary for dispatch at a particular moment while a coarse region is sufficient for planning. Document why the chosen scope is necessary and review that reasoning when the purpose, method, or source changes.

## Sensitive Data and Collection Restrictions

Collection design should identify personal, confidential, regulated, safety-critical, commercially restricted, or otherwise sensitive information early enough to change the method. Options may include avoiding collection, using a less precise measure, separating identifiers, limiting participants, applying stronger authentication, or producing an aggregate at the source.

[Data Privacy](/docs/data/privacy/) owns the principles for responsible processing of information about people, including purpose limitation, minimization, transparency, participation, and retention. [Data Security](/docs/data/security/) owns protection against unauthorized disclosure, alteration, loss, and misuse. The collection decision uses both perspectives; it does not collapse one into the other.

## Ownership, Provenance, and Evidence

Preserve why collection was approved, which method and source were used, who owned the decision, which restrictions apply, and when it must be reviewed. Useful context includes source and owner, observation time, instrument or form version, notices or consent state where applicable, permitted purposes, classifications, retention expectations, and known limitations.

[Metadata](/docs/data/metadata/) provides the broader mechanisms for representing provenance, lineage, semantics, classifications, and automated controls. [Data Governance](/docs/data/governance/) establishes decision rights, policies, ownership, standards, exceptions, and evidence. Collection should produce the context those mechanisms need rather than invent a separate control framework.

## Review Triggers

Reassess collection when the purpose expands, a new population is included, precision or frequency increases, an instrument changes, a new provider is introduced, data is linked with another source, restrictions change, or evidence shows unexpected harm or poor fitness. Continuing collection should be an explicit lifecycle decision, not an indefinite consequence of an old implementation.

## Summary

Responsible collection asks whether the data should exist in the organization's landscape and, if so, under which boundaries. Specify purpose, minimize at the source, apply appropriate authority and transparency, plan protection and retention, and preserve evidence for governance and review.
