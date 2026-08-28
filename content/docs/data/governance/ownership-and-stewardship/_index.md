---
date: "2026-08-22T00:00:00+09:00"
title: "Data Ownership and Stewardship"
weight: 2
prev: "/docs/data/governance/principles-and-operating-model"
next: "/docs/data/governance/policies-standards-and-controls"
---

Data ownership assigns accountability for decisions and outcomes. It is not merely the team that stores a table or runs a pipeline.

![Overview of accountable ownership, stewardship, producers, consumers, and platform responsibilities across data scopes](data-ownership-stewardship.webp "Data Ownership and Stewardship")

Ownership is needed because data decisions often span business meaning, risk, and technical operation. A platform administrator may be able to grant access, but should not have to decide whether a proposed use is acceptable. A steward may recognize that two definitions conflict, but may not have authority to choose which definition becomes an enterprise standard. Ownership connects those decisions to a person or body with an explicit mandate.

## Roles and Boundaries

The roles below describe governance responsibilities, not necessarily job titles. One person may perform several roles in a small organization, while a large organization may divide one role across several people. What matters is that each responsibility and decision right is explicit.

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

The distinction also protects the people performing the work. A steward should not be treated as accountable for a risk they cannot accept, and a platform team should not silently become the policy owner because it implemented the control. When a decision exceeds a role's mandate, that role prepares the context and routes the decision to the accountable owner or designated forum.

## What Is Owned?

A **dataset owner** decides for a bounded asset. A **domain owner** coordinates meaning and policy across a durable business boundary. A **data-product owner** is accountable for a consumer-facing product's usability, reliability, and lifecycle. These scopes can overlap, so decision records should state which scope takes precedence.

Ownership should follow a boundary that can be recognized and sustained. Assigning one executive as owner of thousands of unrelated tables may produce a complete catalog field without creating real accountability. Conversely, assigning an owner to every physical copy can fragment decisions that should remain consistent. Organizations should identify the decision scope first—such as a customer domain, a published data product, or a regulated record set—and then assign ownership at that scope.

## Ownership Through the Lifecycle

Ownership is not completed when a name is entered in a catalog. The owner or delegated roles need to participate when an asset is proposed, classified, published, changed, shared, and retired. Producers should notify owners of changes that affect meaning or controls. Consumers should have a route to raise fitness, access, or interpretation issues. Stewards keep the context and issue history visible so that decisions do not depend on personal memory.

Ownership records should therefore include the governed scope, effective dates, delegated decision rights, escalation path, and a process for reassignment. Temporary vacancies and organizational changes are governance events: an unowned asset should have a defined fallback authority rather than remaining silently unmanaged.

This page covers governance participation only. See [Data Teams](/docs/data/teams/) for broader organization patterns and roles.
