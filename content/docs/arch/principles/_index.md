---
date: "2026-08-30T00:00:00+09:00"
title: "Architecture Principles"
weight: 9
prev: "/docs/arch/decision-frameworks"
---

Architecture principles turn organizational priorities into durable guidance for design decisions. They make a preferred direction explicit before a team becomes attached to a particular technology or implementation.

## Definition

An architecture principle is a durable statement that guides a class of decisions. It translates business goals, engineering goals, and architectural priorities into a constraint or preference that teams can apply repeatedly.

A principle does not select an architecture by itself. It narrows the acceptable options, makes the burden of proof visible, and creates consistency across decisions made by different people at different times.

```text
Business and engineering goals
             ↓
Architecture principles
             ↓
Decision framework
             ↓
Architecture decision
             ↓
Views and implementation
```

For example, a company trying to reduce operational load might adopt the principle **Prefer managed services for undifferentiated infrastructure**. That statement does not mandate one provider or prohibit self-hosting. It establishes the default direction and requires a deliberate reason to depart from it.

## Why Principles Matter

Architecture decisions are rarely independent. A database choice, deployment model, integration pattern, and observability design may all be shaped by the same organizational goal. If that goal is rediscovered during every review, teams spend time repeating debates and may reach incompatible conclusions.

Useful principles provide continuity by:

- Preserving important priorities across projects and decision cycles
- Giving teams a shared starting point without prescribing every design
- Making expectations and the burden of justification explicit
- Helping reviewers distinguish intentional exceptions from accidental inconsistency
- Connecting strategy to concrete architecture choices

Principles are especially valuable when decision authority is distributed. They let teams exercise local judgment within a common direction rather than routing every choice through a central architecture group.

## Anatomy of a Useful Principle

A useful principle is more than a slogan. It should contain enough information for someone to apply it, challenge it, and recognize when it does not fit.

| Element          | Purpose                                                             | Example                                                                      |
| ---------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Statement**    | Expresses the durable preference or constraint                      | Prefer managed services for undifferentiated infrastructure                  |
| **Rationale**    | Connects the principle to an organizational or engineering priority | Reduce operational ownership and focus on differentiating work               |
| **Implications** | Explains how the principle changes evaluation or implementation     | A self-hosted technology requires explicit justification                     |
| **Exceptions**   | Defines legitimate reasons to depart from the default               | Regulatory, performance, or capability requirements may override the default |

The statement should be concise enough to remember and specific enough to create design pressure. **Build secure systems** is too broad because it does not help compare options. **Authenticate service-to-service requests at every trust boundary** is actionable, but may be closer to a standard if it admits little contextual judgment. The appropriate level lies between an aspiration and a detailed implementation rule.

A complete principle can be written as follows:

> **Principle:** Prefer managed services for undifferentiated infrastructure.  
> **Rationale:** Reduce operational ownership and focus engineering effort on capabilities that differentiate the organization.  
> **Implication:** A self-hosted technology needs an explicit justification covering capability gaps, total ownership cost, and operational responsibility.  
> **Exception:** Regulatory constraints, demonstrated performance requirements, or missing provider capabilities may justify self-hosting.

## Principles vs. Pillars

[Pillars](../pillars/) and principles both influence tradeoffs, but they work at different levels.

| Concept       | Question answered                         | Typical form                                          | Example                                                     |
| ------------- | ----------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| **Pillar**    | What matters in this architecture?        | A strategic quality or priority                       | Operability                                                 |
| **Principle** | What persistent guidance follows from it? | A directional constraint or preference with rationale | Prefer managed services for undifferentiated infrastructure |

A pillar is a lens used to judge alternatives. A principle converts one or more of those lenses into guidance that applies across decisions. Operability and cost efficiency may together motivate a managed-services principle. Security and auditability may motivate a principle that every privileged action must produce attributable evidence.

The relationship is not one-to-one. One pillar can produce several principles, and one principle can support several pillars. Keeping the distinction clear prevents pillars from becoming vague slogans and prevents principles from appearing as arbitrary rules.

## Principles in Decision-Making

Principles provide persistent guidance; a [decision framework](../decision-frameworks/) structures the reasoning for one specific choice. The two are complementary.

When a team evaluates whether to operate a database itself, the principle establishes managed service as the default. The decision framework still asks which stakeholders are affected, what constraints apply, what options exist, what evidence supports them, and what consequences each option creates. The principle changes the starting position and burden of proof, but it does not replace analysis.

A practical sequence is:

1. Identify the decision and the goals or concerns behind it.
2. Find the principles that apply and state how they shape the default.
3. Use a decision framework to compare viable options against evidence and constraints.
4. Record whether the result follows a principle or uses an explicit exception.
5. Express the chosen architecture through appropriate [views and viewpoints](../views-and-viewpoints/).

Multiple principles may point in different directions. A preference for managed services may conflict with data residency or latency guidance. The team should not hide that tension or count which option satisfies the most principles. It should identify which concern dominates in this context and preserve the reasoning in the decision record.

## Exceptions and Evolution

A principle is a default with authority, not an absolute rule. A principle that cannot admit legitimate exceptions will either force poor decisions or be ignored when reality differs from its assumptions.

Exceptions should be explicit and reviewable. Record:

- Which principle is being departed from
- Which constraint or evidence makes the default unsuitable
- Who accepts the additional risk or ownership
- Whether the exception is temporary or enduring
- What change would trigger another review

Repeated exceptions are feedback. They may reveal weak enforcement, but they may also show that the principle is too broad, its rationale is no longer valid, or the organization lacks the platform capability needed to follow it. Principles should therefore have an owner and a review trigger, such as a strategy change, recurring exceptions, new regulation, or a major shift in operating model.

Evolution should preserve intent. When a principle changes, document why, identify affected standards and decisions, and avoid silently treating older choices as mistakes. They were made under a different set of priorities and constraints.

## Common Mistakes

**Writing Aspirations Instead of Guidance.** Statements such as “be scalable” or “use simple designs” name desirable outcomes but do not create a usable preference or constraint.

**Encoding a Technology Choice as a Principle.** “Use product X” is usually a standard or decision. A principle should explain the durable direction that would remain meaningful if the available products changed.

**Omitting the Rationale.** Without a rationale, teams cannot judge whether the principle applies to an unfamiliar case or whether its assumptions have expired.

**Treating Principles as Universal Laws.** Context matters. Legitimate exceptions should be visible, justified, and reviewed rather than concealed.

**Creating Too Many Principles.** A large catalog makes conflicts common and priorities unclear. Keep the set small enough that teams can recall and apply it.

**Using Principles to Avoid Decisions.** Principles guide judgment; they do not eliminate evidence, tradeoffs, or accountable decision-making.

**Failing to Maintain Them.** A principle detached from current strategy, platform capability, or regulation becomes organizational folklore rather than useful guidance.

## Summary

Architecture principles are durable decision guidance. They translate goals and pillars into constraints or preferences, establish defaults across many decisions, and make exceptions explicit. Decision frameworks then apply that persistent guidance to a particular choice, while views communicate the resulting architecture. Together, these concepts form a reasoning system rather than a collection of isolated terms.
