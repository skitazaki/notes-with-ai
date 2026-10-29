---
date: "2026-09-03T00:00:00+09:00"
title: "Personal Data and PII"
prev: "/docs/data/privacy/privacy-fundamentals"
next: "/docs/data/privacy/privacy-harms"
---

Personal data is information that relates to an identified or identifiable person. Personally identifiable information (PII) is a common, but context-dependent, label for information that can distinguish or trace an identity. The terms overlap, yet legal and organizational definitions vary; teams should record the definition and obligations they actually apply.

## Identifiability Is Contextual

Direct identifiers include names, account numbers, email addresses, and government identifiers. Indirect identifiers—location, device data, dates, rare characteristics, or behavioral patterns—may identify someone when combined with other information. A stable pseudonym can also single out a person even when their name is absent.

Identifiability depends on realistic means available to recipients and likely attackers, not only the contents of one table. Linkability, inference, external datasets, and access to mapping keys all matter.

## Sensitivity and Consequence

Some personal data warrants stronger handling because misuse may cause greater harm. Health, biometric, financial, precise location, communications, employment, and children's data are frequent examples. Sensitivity is not fixed: an apparently ordinary fact can become sensitive through context, combination, or use.

Classification should distinguish identifiability from sensitivity. One describes connection to a person; the other helps express likely consequence and handling need. Both should inform collection, access, sharing, retention, monitoring, and deletion.

## Managing Personal Data

Maintain an inventory that records source, purpose, owner, recipients, location, retention, classification, and transformations. Propagate relevant metadata into derived datasets and exports. Review new joins and inferences, because a dataset's privacy properties can change without any new fields being collected.

## Summary

Personal data is defined by relationship and context, not by a short list of columns. Treat identifiability as a spectrum, assess combination and inference risk, and connect classifications to concrete lifecycle controls.
