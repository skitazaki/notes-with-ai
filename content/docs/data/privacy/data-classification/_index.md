---
date: "2026-09-03T00:00:00+09:00"
title: "Data Classification for Privacy"
prev: "/docs/data/privacy/privacy-harms"
next: "/docs/data/privacy/de-identification"
---

Privacy classification describes data properties that affect how information about people should be handled. It turns abstract obligations into metadata that systems and teams can use when granting access, approving reuse, sharing data, or applying retention.

## Useful Classification Dimensions

A single label such as confidential is rarely enough. Classify whether data is personal, how directly it identifies someone, its sensitivity, the population represented, approved purposes, sharing constraints, retention category, and any jurisdictional or contractual conditions. Record provenance and confidence when a classification is inferred rather than confirmed.

Classification schemes should be small enough to apply consistently. Each value needs a definition, examples, an owner, and mapped handling rules. Separate privacy properties from business criticality and security impact while allowing those dimensions to inform one another.

## Classification Changes

Data can become more identifying or sensitive after joining, enrichment, modeling, or export. Derived attributes and embeddings may preserve information from their sources. Classification must therefore propagate through lineage and be reassessed at transformation and sharing boundaries.

Automation can detect obvious identifiers and suggest labels, but context determines meaning. Sampling, schema names, source metadata, and human review remain necessary, especially for free text, images, and inferred attributes.

## Making Labels Operational

Connect classifications to default access, approved environments, masking, encryption, monitoring, sharing review, retention, and deletion. Record exceptions with owners and expiration dates. Measure coverage, stale labels, unresolved conflicts, and whether controls actually consume the metadata.

## Summary

Privacy classification is valuable only when it changes a decision. Multidimensional, lineage-aware labels help apply proportionate controls without confusing personal-data status, sensitivity, confidentiality, and business importance.
