---
date: "2026-08-22T00:00:00+09:00"
title: "Data Protection Techniques"
weight: 2
prev: "/docs/data/security/classification-and-handling"
next: "/docs/data/security/encryption-and-key-management"
---

Data protection techniques reduce exposure by changing how values are represented or what detail consumers receive. Masking, tokenization, redaction, hashing, pseudonymization, and aggregation solve different problems and are not interchangeable.

| Technique        | Reversible?                                  | Referential consistency                | Typical use                                                   |
| ---------------- | -------------------------------------------- | -------------------------------------- | ------------------------------------------------------------- |
| Masking          | Depends                                      | Optional                               | Hide values in non-production, support, or analytical views   |
| Tokenization     | Through a protected mapping or service       | Often required                         | Replace stable identifiers while preserving joins             |
| Redaction        | No in the released output                    | Usually not                            | Remove fields or passages from documents, logs, and responses |
| Hashing          | One-way by design                            | Deterministic hashes preserve equality | Integrity checks, credential verification, limited matching   |
| Pseudonymization | Usually linkable with additional information | Often required                         | Separate direct identity from working datasets                |
| Aggregation      | Not directly; inference may remain possible  | Group level                            | Release summaries instead of row-level values                 |

## Properties and Limitations

**Masking** substitutes, perturbs, generalizes, or partially hides values. Static masking creates a transformed copy; dynamic masking changes the presented view. **Redaction** removes content from a released artifact. Visual overlays are not secure redaction if underlying text or metadata remains.

**Tokenization** replaces a value with a surrogate and relies on a secured vault or service for recovery. Stable tokens support joins but also linkage. The mapping service becomes a high-value asset.

**Pseudonymization** separates identifying attributes so records cannot be attributed without additional information. It remains sensitive when external data, repeated observations, or rare attributes enable re-identification. Privacy implications belong in [Data Privacy](/docs/data/privacy/).

**Hashing** maps input to a fixed digest and is not designed for recovery. It supports integrity checks and specialized password verification, but does not conceal low-entropy identifiers because attackers can hash likely inputs. **Aggregation** reduces row-level exposure, but small groups, repeated queries, differencing, and external knowledge can reveal contributors.

## Selection Questions

Ask whether original recovery and stable joins are required, what auxiliary information an attacker can obtain, whether rare values and relationships remain, where source data, mappings and keys are stored, and how consumers can copy or combine the result.

## Summary

Select protection techniques by reversibility, linkage needs, auxiliary-information risk, and the controls around source data, keys, mappings, and outputs.
