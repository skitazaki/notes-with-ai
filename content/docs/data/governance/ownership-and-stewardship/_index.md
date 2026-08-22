---
date: "2026-08-22T00:00:00+09:00"
title: "Data Ownership and Stewardship"
weight: 2
prev: "/docs/data/governance/principles-and-operating-model"
next: "/docs/data/governance/policies-standards-and-controls"
---

Data ownership assigns accountability for decisions and outcomes. It is not merely the team that stores a table or runs a pipeline.

## Roles and Boundaries

- A **Data Owner** is accountable for a domain, dataset, or data product and accepts decisions about permitted use, quality expectations, access, and lifecycle.
- A **Data Steward** maintains definitions, classifications, issues, and policy application, and prepares decisions that require owner authority.
- **Technical and platform teams** operate storage, pipelines, access mechanisms, metadata services, and automated controls.
- **Producers** make source meaning, change, and quality signals explicit; **consumers** use data within declared terms and report unsuitable behavior.
- Governance, privacy, security, risk, and compliance specialists define or advise on cross-cutting obligations.

| Decision                                        | Accountable                     | Responsible or consulted                   |
| ----------------------------------------------- | ------------------------------- | ------------------------------------------ |
| Define acceptable uses and service expectations | Data Owner                      | Steward, producers, consumers, specialists |
| Maintain definitions and classification records | Data Owner                      | Data Steward                               |
| Implement access and quality controls           | Data Owner                      | Platform and delivery teams                |
| Approve a material exception                    | Designated risk or policy owner | Data Owner, specialists                    |
| Report use and control evidence                 | Data Owner                      | Steward and platform teams                 |

Accountability and operational responsibility must remain distinct: assigning a steward to update a catalog does not transfer the owner's accountability.

## What Is Owned?

A **dataset owner** decides for a bounded asset. A **domain owner** coordinates meaning and policy across a durable business boundary. A **data-product owner** is accountable for a consumer-facing product's usability, reliability, and lifecycle. These scopes can overlap, so decision records should state which scope takes precedence.

This page covers governance participation only. See [Data Teams](/docs/data/teams/) for broader organization patterns and roles.
