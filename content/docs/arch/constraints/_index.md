---
date: "2026-09-10T00:00:00+09:00"
title: "Architecture Constraints"
weight: 10
prev: "/docs/arch/principles"
next: "/docs/arch"
---

Architecture constraints define the limits of the solution space before a team makes a design decision. They state what a solution must do, must not do, or cannot rely on, so teams do not spend time defending options that were never viable.

## Definition

A constraint is a condition that bounds an architecture decision. It may rule out technologies, deployment locations, integration patterns, operating models, or timelines. It is not simply an important preference: an option that violates a genuine constraint is not acceptable unless the authority that owns it changes the condition.

Consider a team designing a customer-data platform. **Customer data must remain in Japan** is a constraint. An option that replicates identifiable customer data to another region cannot be selected without changing the legal, contractual, or policy condition behind that requirement. By contrast, **prefer managed services** is a direction for choosing among viable options; a self-hosted design can still be justified when its advantages outweigh its additional operational cost.

```text
Constraint → What must / cannot be done?
Principle  → What direction do we normally prefer?
Decision   → What do we choose in this situation?
```

## Sources of Constraints

Constraints arise from the environment in which a system operates, not only from its codebase. Common sources include:

- Laws, regulation, contracts, and data-residency commitments
- Security requirements, trust boundaries, and risk acceptance decisions
- Existing platforms, interfaces, data formats, and migration commitments
- Budget, delivery date, staffing, and operational capability
- Physical location, network latency, hardware, or vendor availability
- Business policy, customer commitments, and organizational ownership

The source tells the team who can interpret, verify, or change the constraint. “Data must remain in Japan” should identify whether it follows from legislation, a customer contract, an internal policy, or a risk decision.

## Hard vs. Soft Constraints

Hard constraints are conditions an option must satisfy. They are commonly enforced by law, contract, security policy, a fixed interface, or a non-negotiable delivery boundary. They should be tested early, before detailed comparison of alternatives.

Soft constraints are strong limits that can be relaxed with explicit approval and understood consequences. A fixed launch date, preferred cloud region, or spending ceiling may be soft when a sponsor can authorize a change. This makes the owner, escalation path, and cost of exception visible.

Avoid using _hard_ and _soft_ as substitutes for “important” and “unimportant.” The relevant question is whether a team can legitimately select an option that violates the condition, and who has the authority to approve that exception.

## Constraints vs. Principles

[Architecture Principles](../principles/) provide durable guidance across decisions. They establish defaults and a burden of proof, but normally leave several options open. Constraints determine the boundary of what can be considered at all.

| Concept        | Question                     | Effect on options                          | Running example                     |
| -------------- | ---------------------------- | ------------------------------------------ | ----------------------------------- |
| **Constraint** | What must or cannot be done? | Removes non-compliant options              | Customer data must remain in Japan  |
| **Principle**  | What do we normally prefer?  | Establishes a default among viable options | Prefer managed services             |
| **Decision**   | What do we choose here?      | Commits to an option in context            | Use a Japan-region managed database |

The distinction prevents two common errors. Calling a preference a constraint makes normal tradeoffs appear impossible. Calling a genuine boundary a principle lets teams treat compliance as optional. A principle may be motivated by constraints, and a constraint may justify an exception to a principle, but they should remain separately stated.

## Constraints in Decision-Making

A [decision framework](../decision-frameworks/) should surface constraints before it ranks alternatives. Start by naming the decision, then record the constraints, their source, owner, and evidence. Eliminate options that fail hard constraints. Only then compare the remaining options against principles, pillars, costs, risks, reversibility, and evidence.

For the customer-data platform, the team first confirms what “remain in Japan” covers: storage, processing, backups, support access, telemetry, and disaster recovery may have different implications. It then removes designs that cannot meet that scope. Within the remaining set, the managed-services principle favors a Japan-region managed database. If none satisfies the requirement, the team may choose a self-hosted database and record residency as the reason for departing from the default.

This order keeps discussion honest. A managed service is not “better” if it violates a hard residency constraint; it is simply not viable. Conversely, an approved self-hosted option is not necessarily a failure of the principle when the constraint changes what is possible.

## Validating and Revisiting Constraints

Constraints deserve evidence and maintenance. For each material one, record the statement, source, scope, owner, verification, and review trigger. Test ambiguous wording with the people responsible for legal, security, operations, product, or customer commitments.

Revisit a constraint when its source changes: a contract expires, a regulation is clarified, a platform gains a capability, a migration completes, or a deadline and budget are renegotiated. It may be retired or narrowed, but should never disappear silently.

## Common Mistakes

**Treating assumptions as constraints.** An untested belief about cost, latency, or product capability should be evidence to validate, not a boundary that eliminates options.

**Leaving the source or owner unstated.** Without them, teams cannot resolve ambiguity or know who may approve an exception.

**Discovering constraints after choosing a design.** Late discovery turns a decision into rework and encourages teams to rationalize a non-compliant option.

**Using a preference to hide a tradeoff.** “We always use managed services” is a principle unless an accountable authority has made it a mandatory rule.

**Never reviewing temporary limits.** Migration restrictions, deadlines, and vendor capabilities change. Retaining them as permanent folklore unnecessarily shrinks future choices.

## Summary

Architecture constraints bound the solution space before a decision is made. Principles then guide the preferred direction among the viable options, and decision frameworks make the contextual choice and its consequences explicit. Keeping those roles separate makes architecture reasoning faster, clearer, and easier to revisit.
