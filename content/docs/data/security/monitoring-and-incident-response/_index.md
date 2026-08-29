---
date: "2026-08-22T00:00:00+09:00"
title: "Data Security Monitoring and Incident Response"
weight: 5
prev: "/docs/data/security/data-loss-prevention"
---

Data security monitoring observes how sensitive and business-critical data is accessed, changed, exported, and administered. Incident response uses that evidence to determine what happened, contain harm, recover trusted assets, and improve controls.

[Data Observability](/docs/data/engineering/observability/) asks whether flows are healthy, timely, and behaving as expected. Data security monitoring asks whether activity represents unauthorized disclosure, alteration, destruction, or misuse. Telemetry may overlap, but detection and response differ.

## Security-Relevant Telemetry

- **Data access:** principal, workload, dataset or field, action, query, result volume, time, source, destination, and decision.
- **Administrative changes:** grants, roles, policies, sharing, public exposure, disabled logging, retention, and backup settings.
- **Movement:** exports, downloads, copies, replication, cross-account transfers, connectors, and external shares.
- **Protection services:** decrypt operations, key-policy changes, token-vault use, masking bypass, and discovery results.
- **Integrity and recovery:** writes, deletes, schema changes, checksums, immutable snapshots, backup access, restore tests, and recovery results.

Identify human and workload principals consistently, preserve time and request correlation, and protect logs from alteration or deletion. Avoid recording raw sensitive values when identifiers, classifications, fingerprints, or references provide enough evidence.

## Detection Patterns

| Signal                              | Security question                                               |
| ----------------------------------- | --------------------------------------------------------------- |
| Unusual sensitive-data access       | Is the principal accessing a new class, domain, or time window? |
| Abnormal query or result volume     | Is ordinary access being used for bulk extraction?              |
| Repeated narrow queries             | Can permitted results reconstruct a protected population?       |
| Mass export or new destination      | Is data crossing an unapproved boundary?                        |
| Permission or sharing change        | Did a control change before unusual access?                     |
| Unexpected modification or deletion | Is integrity or availability under attack?                      |
| Backup or key access                | Is an actor targeting recovery or decryption?                   |

Use high-confidence rules alongside contextual anomaly detection. Static thresholds may miss slow activity; baselines require tuning and explainable evidence.

## Investigation, Containment, and Recovery

Reconstruct the data path, not only the login. Determine affected datasets, fields, partitions, records, backups, and derived outputs; the human, workload, credential, session, query, and tool involved; actions and volume; destinations and recipients; and which control allowed the path.

[Metadata](/docs/data/metadata/) and lineage identify derived assets and consumers. Evidence from [Access Control](/docs/acc/) explains how permission was obtained. Preserve evidence with controlled access and integrity.

Containment may revoke sessions, disable workloads or connectors, narrow permissions, isolate storage, block egress, rotate credentials or keys, suspend sharing, or preserve backups. Stop harm without unnecessarily destroying evidence or recovery paths.

Recovery means restoring from a known-good point, verifying integrity, re-establishing secure configuration, validating dependent datasets and models, and monitoring for recurrence. Restoration does not undo a confidentiality loss; downstream copies, recipients, and continued access also require response.

Prioritize high-value data and high-impact paths. Define and test playbooks for mass export, public exposure, destructive change, key compromise, and backup compromise. Measure coverage, evidence quality, investigation time, containment time, and recurrence—not only alert volume.

## Summary

Monitoring turns access, administration, movement, protection, and recovery events into security evidence. Response follows affected data across copies and boundaries, contains the path, restores trusted state, validates integrity, and improves controls.
