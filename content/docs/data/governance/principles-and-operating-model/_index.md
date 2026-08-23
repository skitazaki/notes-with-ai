---
date: "2026-08-22T00:00:00+09:00"
title: "Governance Principles and Operating Model"
weight: 1
prev: "/docs/data/governance"
next: "/docs/data/governance/ownership-and-stewardship"
---

Data governance turns organizational intent into repeatable decisions about data. Its operating model defines scope, authority, forums, escalation paths, and the lifecycle through which rules are proposed, approved, applied, reviewed, and retired.

An operating model is the practical arrangement through which governance work gets done. It does not prescribe one organization chart. A small organization may rely on named owners and existing leadership meetings, while a larger organization may need dedicated governance roles and several decision forums. In either case, the model should make it possible to answer the same questions: what requires a decision, who may make it, who must be consulted, how the decision is recorded, and where unresolved issues go.

## Foundations

- **Accountability** identifies the person or body answerable for an outcome.
- **Decision rights** specify which decisions a role may make and within what limits.
- **Authority** is the recognized mandate to exercise those rights.
- **Scope** identifies the domains, assets, uses, and obligations covered.

Accountability should remain singular enough to be meaningful, while operational responsibility can be distributed. For example, a Data Owner may remain answerable for appropriate use of a customer dataset even though a steward maintains its definitions, a platform team implements access controls, and a privacy specialist advises on processing conditions. Naming many contributors without identifying who accepts the outcome leaves accountability unresolved.

## Decision Forums and Escalation

A **governance forum** is a recurring mechanism for making decisions that cannot be resolved by one role acting within its existing authority. It may be an agenda within an established leadership meeting rather than a new committee. The form matters less than having a defined mandate, participants, decision scope, and record of outcomes.

Different scopes can require different forums:

- A **domain forum** brings together the owner, stewards, producers, consumers, and relevant specialists for decisions that depend on local business context, such as the accepted meaning of a measure or the priority of a quality issue.
- A **cross-domain council** coordinates matters that affect several domains, such as a shared identifier, conflicting definitions, or an exchange standard. A council is a decision and coordination body; it should not become the nominal owner of every data asset.
- An **enterprise forum** establishes minimum organization-wide requirements and decides issues whose inconsistency would create unacceptable legal, security, financial, or interoperability risk.

These are functional descriptions, not mandatory names or organizational layers. One forum can cover several functions in a smaller organization. An issue should be escalated only when it exceeds the current role's authority, affects another accountable scope, or requires explicit risk acceptance. Escalation is therefore a transfer of decision scope, not a substitute for local problem solving.

## From Intent to Evidence

Strategy becomes principles; principles guide policies; policies are made concrete through standards and control objectives; controls operate in processes and platforms; evidence shows what happened. Review uses that evidence to change ineffective policy or controls.

The sequence is a feedback loop rather than a one-way publication process. Evidence may show that a control is not operating, but it may also reveal that a standard is impractical or that a policy no longer addresses the intended risk. Governance must therefore review both compliance with the rule and the continuing fitness of the rule itself.

Every policy needs an owner, scope, approval authority, effective date, review cycle, and retirement condition. Exceptions need a rationale, risk owner, compensating controls, expiry date, and escalation route. Otherwise an exception becomes an undocumented alternate policy.

## Central and Distributed Responsibility

Centralized, federated, and hybrid models are all valid. The appropriate placement of a decision depends on risk, required consistency, available context, and organizational capacity. Centralize decisions whose inconsistency would create unacceptable enterprise risk or break interoperability. Where authority is delegated, place contextual decisions with the domains that understand the data and its use. Shared platforms can provide reusable enforcement and evidence collection without taking ownership of the underlying business decision.

Governance enables when it publishes clear decision boundaries, provides safe defaults and paved paths, and resolves ambiguity quickly. It becomes gatekeeping when forums approve routine work without adding context, accountability, or risk reduction.

An operating model is working when routine decisions are made at the intended level, exceptions are visible, cross-boundary conflicts have a credible route to resolution, and evidence changes future policy or controls. The number of councils or policies is not, by itself, a measure of governance effectiveness.

Continue with [Ownership and Stewardship](../ownership-and-stewardship/) for role-level decision rights and [Policies, Standards, and Controls](../policies-standards-and-controls/) for the rule hierarchy.
