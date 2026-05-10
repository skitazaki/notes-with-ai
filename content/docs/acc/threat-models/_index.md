+++
date = '2026-05-10T13:40:00+09:00'
title = 'Threat Model Catalog'
weight = 10
prev = '/docs/acc/patterns'
next = '/docs/acc/decision-frameworks'
+++

Threat models help teams move from generic security concern to explicit attack paths, trust-boundary analysis, and mitigation choices.

## Executive Summary

Access-control failures rarely appear as a single bug. They emerge as chains: stale permissions plus weak review, token theft plus absent segmentation, prompt injection plus broad tool access, or service-account sprawl plus missing attribution. A threat catalog provides a shared language for reasoning about those chains before incidents happen.

## Core Concepts

### Common threat categories

- **Privilege escalation** through misconfiguration, role inheritance, or flawed policy evaluation
- **Token or credential theft** from endpoints, workloads, CI/CD systems, or logs
- **Lateral movement** using over-broad service trust or shared credentials
- **Orphaned accounts** that remain active after ownership disappears
- **Shadow administration** through indirect permissions or ungoverned support tooling
- **Confused deputy** where a trusted service is tricked into misusing its authority
- **Prompt injection** that influences agent tools or data interpretation
- **Policy bypass** through undocumented exception paths or inconsistent enforcement layers

### Threat-model structure

For each threat, teams should capture:

1. attacker preconditions
2. trust boundaries crossed
3. assets at risk
4. detection opportunities
5. preventive and compensating controls

## Implementation and Operations

### Example mitigation mapping

- stale permissions -> lifecycle automation, access review, ownership mapping
- token theft -> short-lived credentials, device binding, vault hygiene, anomaly detection
- lateral movement -> segmentation, least privilege, service identity separation
- prompt injection -> tool allowlists, content isolation, approval gates, output filtering
- policy bypass -> unified policy semantics, negative testing, consistent logging

Threat models are most useful when they are attached to architecture reviews, control testing, and post-incident learning rather than maintained as static compliance documents.
