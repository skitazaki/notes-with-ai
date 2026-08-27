---
date: "2026-08-22T00:00:00+09:00"
title: "Encryption and Key Management"
weight: 3
prev: "/docs/data/security/data-protection-techniques"
next: "/docs/data/security/data-loss-prevention"
---

Encryption makes data unintelligible without authorized keys. It protects data at rest and in transit and can narrow exposure while data is in use. Its effectiveness depends on where plaintext appears, who can use keys, and how the key lifecycle is controlled—not merely whether an encryption setting is enabled.

Encryption protects confidentiality. Cryptographic authentication can protect integrity and authenticity, but encryption alone does not prevent an authorized application from leaking plaintext, an overprivileged user from querying it, or ransomware from destroying accessible copies.

## Data States

- **At rest:** database files, objects, disks, snapshots, extracts, archives, and backups. Storage encryption does not necessarily isolate tenants or privileged platform identities.
- **In transit:** APIs, pipeline connectors, streams, replication, downloads, and partner links. Secure transport should authenticate endpoints as well as encrypt traffic.
- **In use:** memory and compute. Application isolation, minimal plaintext scope, secure execution environments, and confidential computing can reduce exposure. Confidential computing does not replace controls on code, identities, outputs, and keys.

## Cryptographic Roles and Key Hierarchy

**Symmetric encryption** uses one secret for encryption and decryption and is efficient for bulk data. **Asymmetric cryptography** uses a public/private pair for key establishment, signatures, and cases where parties should not share one secret. Systems commonly combine them.

Envelope encryption uses a data-encryption key (DEK) for data and a key-encryption key (KEK) to wrap the DEK. The encrypted DEK may be stored beside ciphertext while the KEK remains in a strongly controlled service.

```mermaid
flowchart LR
  KMS["KMS or HSM<br/>protects KEK"] -->|wraps / unwraps| DEK["Encrypted data key"]
  DEK -->|authorized context| Data["Encrypted data objects"]
  Policy["Identity, policy & audit"] --> KMS
```

A KMS manages keys, policies, operations, versions, and audit events. An HSM provides a hardened cryptographic boundary and may keep key material from leaving protected hardware. Separate keys from data and key administration from routine data administration where practical. Limit decrypt operations by workload, environment, purpose, and context.

## Key Lifecycle

Manage generation, activation, authorized use, storage, rotation, revocation, archival where required, and destruction. Rotation supports compromise response but does not erase plaintext or revoke previously exported data.

Provider-managed keys reduce operational burden. Customer-managed keys offer more policy, separation, audit, and revocation control but increase availability and recovery responsibility. Choose according to the threat model.

**Crypto-shredding** destroys the key needed to decrypt ciphertext. It works as deletion only when all usable key copies are controlled, no plaintext or alternative copy remains, and the cryptographic design is sound.

## Failure Modes

- Keys and data in the same trust boundary
- One key across unrelated tenants, environments, or sensitivity levels
- Broad decrypt permission or long-lived exported credentials
- Backups without tested key recovery—or recoverable by too many administrators
- Rotation without an inventory of dependent ciphertext
- Logs, caches, or temporary files containing plaintext

## Summary

Encryption is a system property, not a checkbox. Define the threat and data state, minimize plaintext, establish a deliberate key hierarchy, restrict and observe key use, and test rotation and recovery.
