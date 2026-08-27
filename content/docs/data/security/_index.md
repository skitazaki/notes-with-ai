---
date: "2026-08-22T00:00:00+09:00"
title: "Data Security"
weight: 7
prev: "/docs/data"
---

Data security protects data against unauthorized disclosure, alteration, destruction, leakage, and misuse wherever it resides or moves. Its central question is: **How do we maintain appropriate protection as data crosses systems, teams, clouds, regions, partners, analytics environments, and AI workloads?**

Confidentiality limits disclosure, integrity protects against unauthorized or undetected change, availability keeps data and recovery capabilities usable, and authenticity establishes confidence in sources and actions. These objectives are foundations, but effective security follows the data lifecycle and realistic threats rather than organizing everything mechanically around the CIA triad.

## A Data-Centric Boundary

Modern data is copied into warehouses, lakehouses, object stores, notebooks, caches, temporary files, extracts, analytics tools, backups, SaaS platforms, partner environments, and AI systems. Protecting one database or network perimeter therefore leaves other copies and transfer paths exposed.

Data-centric security follows the asset across boundaries. It combines defense in depth, least privilege, blast-radius reduction, and assume-breach thinking: prevent compromise, limit what a compromised identity or component can reach, detect misuse, and preserve recovery.

![Data-centric defense-in-depth model with data protected by four layers of controls and monitoring and detection spanning every layer](data-centric-defense-in-depth.webp "Data-Centric Defense in Depth")

The principle is to protect data across systems and boundaries, not merely the perimeter around one system.

## From Understanding to Recovery

```mermaid
flowchart LR
  U["Understand<br/>inventory, location, lineage"] --> C["Classify & Assess<br/>sensitivity, exposure, threats"]
  C --> P["Protect<br/>encryption, masking, secure handling"]
  P --> O["Control<br/>least privilege, isolation, egress"]
  O --> D["Detect<br/>audit, anomalies, extraction"]
  D --> R["Respond & Recover<br/>contain, investigate, restore, verify"]
  R -. lessons .-> U
```

- **Understand** important data, copies, flows, locations, and dependencies.
- **Classify and assess** sensitivity, criticality, exposure, trust boundaries, and threats.
- **Protect** data and credentials through encryption, representation-changing techniques, and secure storage and transport.
- **Control** permitted paths using least privilege, isolation, policy enforcement, controlled sharing, and egress restrictions. Identity and authorization models belong in [Access Control](/docs/acc/).
- **Detect** security-relevant access, permission changes, abnormal queries, bulk extraction, and exfiltration signals.
- **Respond and recover** by containing access, rotating credentials and keys, investigating affected data, restoring trusted copies, and validating integrity.

## Security Across the Lifecycle

| Lifecycle or state | Representative concerns                                                      |
| ------------------ | ---------------------------------------------------------------------------- |
| Collection         | Source authenticity, secure ingestion, malicious input, early classification |
| Storage            | Encryption, access boundaries, isolation, exposed object stores              |
| Processing         | Memory exposure, temporary copies, workload credentials, untrusted code      |
| Analytics and AI   | Excessive access, notebooks, extracts, model inputs and outputs              |
| Sharing            | Recipient controls, egress paths, partner boundaries                         |
| Backup and archive | Encryption, privileged access, immutability, recoverability                  |
| Deletion           | Replicas, caches, backups, residual keys and media                           |

Cloud storage, streams, warehouses, lakehouses, SaaS analytics, clean rooms, data products, cross-cloud transfers, and AI consumption are contexts in which controls operate—not separate security taxonomies.

## Lightweight Data Threat Modeling

Start with the data. Identify sensitive or business-critical assets, enumerate copies and flows, mark trust boundaries, and ask how confidentiality, integrity, availability, or authenticity could fail. Relevant threats include unauthorized reading or modification, accidental disclosure, public exposure, credential compromise, privilege escalation, insiders, exfiltration, ransomware, backup compromise, cross-tenant exposure, third-party compromise, and inference from protected data. Prioritize credible paths by impact and ease, then map preventive, detective, and recovery controls.

## Boundaries with Neighboring Disciplines

| Discipline                                                                                         | Primary question                                                                  | Relationship to data security                                                                                                    |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Data Governance                                                                                    | Who owns decisions, sets policy, manages exceptions, and demonstrates compliance? | Establishes requirements and accountability; security operates safeguards.                                                       |
| [Data Privacy](/docs/data/privacy/)                                                                | Is processing information about people appropriate and necessary?                 | Depends on safeguards, but appropriate use cannot be decided by security alone.                                                  |
| [Access Control](/docs/acc/)                                                                       | Who or what may perform which action?                                             | Provides one protection mechanism; security also covers encryption, exposure, monitoring, exfiltration, integrity, and recovery. |
| [Data Management](/docs/data/management/)                                                          | How does data remain trustworthy, usable, and sustainable?                        | Operates lifecycle and quality practices on which security imposes safeguards.                                                   |
| [Data Architecture](/docs/data/data-architecture/) and [Data Engineering](/docs/data/engineering/) | How are data systems structured, built, and operated?                             | Provide systems and flows whose security properties are defined and verified here.                                               |

## Topic Pages

{{< cards >}}
{{< card link="classification-and-handling/" title="Data Classification and Handling" icon="tag" subtitle="Turning sensitivity and criticality into enforceable handling requirements" >}}
{{< card link="data-protection-techniques/" title="Data Protection Techniques" icon="eye-off" subtitle="Comparing masking, tokenization, redaction, hashing, pseudonymization, and aggregation" >}}
{{< card link="encryption-and-key-management/" title="Encryption and Key Management" icon="key" subtitle="Protecting data at rest, in transit, and conceptually in use" >}}
{{< card link="data-loss-prevention/" title="Data Loss Prevention and Exfiltration" icon="shield-exclamation" subtitle="Reducing accidental leakage and malicious extraction across egress paths" >}}
{{< card link="monitoring-and-incident-response/" title="Data Security Monitoring and Incident Response" icon="eye" subtitle="Detecting, investigating, containing, and recovering from data-focused incidents" >}}
{{< /cards >}}

## Summary

Data security protects the asset across its lifecycle. It starts by understanding and classifying data, applies layered protections and controlled paths, observes access and movement, and preserves the ability to contain and recover.
