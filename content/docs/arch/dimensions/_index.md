---
date: "2026-06-28T00:00:00+09:00"
title: "Architecture Dimensions"
weight: 1
prev: "/docs/arch"
next: "/docs/arch/layers"
---

Architecture becomes confusing when teams try to force every concern into one diagram or one vocabulary. Dependency direction, runtime control, design priorities, team accountability, and stakeholder communication are all architectural concerns, but they are not the same kind of concern. An architecture dimension is the lens that makes one of those concerns legible.

## Definition

An architecture dimension is a reasoning lens for understanding one system from a specific perspective. It helps a team ask a focused question, ignore details that are not relevant to that question, and compare design options using the right criteria.

Dimensions are not the same thing as diagrams. A diagram is a representation. A dimension is the framing logic that determines what that representation should emphasize.

## Why Dimensions Matter

Teams lose clarity when they mix several kinds of reasoning in one model. A single picture may try to show service dependencies, runtime request paths, ownership by team, security controls, and executive outcomes at the same time. The result is usually overloaded and ambiguous.

Dimensions matter because they separate concerns that otherwise get conflated:

- Structural questions are about what is built and what depends on what.
- Operational questions are about how work moves and how the system behaves at runtime.
- Strategic questions are about which qualities should shape tradeoffs.
- Ownership questions are about who changes and operates the system.
- Communication questions are about what a specific audience needs to understand.

That separation does not fragment architecture. It makes reasoning explicit. One system still exists, but engineers need different lenses to understand it well.

## The Core Dimensions

### Structural

The structural dimension focuses on form and dependency. It helps answer questions such as which modules depend on which platforms, where abstractions sit, and how changes should propagate through the system. Layers, components, services, interfaces, and modules are common structural concepts.

### Operational

The operational dimension focuses on runtime behavior. It explains how requests, jobs, events, telemetry, and policy decisions move through the system. Control planes, data planes, pipelines, workflows, and handoff points are common operational concepts.

### Strategic

The strategic dimension focuses on priorities and tradeoffs. It captures what the architecture must optimize for, such as reliability, security, cost efficiency, or developer velocity. Pillars, principles, quality attributes, and constraints belong here.

### Ownership

The ownership dimension focuses on responsibility. It helps teams reason about who can change a service safely, who operates it, who owns the data contract, and where cross-team dependencies introduce friction or risk. Domains, bounded contexts, platform responsibilities, and service ownership boundaries are common concepts.

### Communication

The communication dimension focuses on explanation. It helps teams decide which concerns should be selected, framed, and presented for a particular audience. Views, viewpoints, review artifacts, and audience-specific summaries belong here because they turn architecture reasoning into communication.

## Comparison Table

| Dimension     | Primary question                            | Common concepts                                   | Useful for                                           | Common mistake                                                           |
| ------------- | ------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| Structural    | What is built, and what depends on what?    | Layers, modules, services, components             | Dependency management, abstraction, change isolation | Treating runtime traffic as if it were structural dependency             |
| Operational   | How does work execute and move?             | Planes, flows, pipelines, orchestration           | Failure analysis, latency reasoning, runtime control | Ignoring static boundaries and assuming execution paths define structure |
| Strategic     | What are we optimizing for?                 | Pillars, principles, quality attributes, policies | Tradeoff analysis, reviews, investment choices       | Listing values without turning them into decision criteria               |
| Ownership     | Who changes and operates what?              | Domains, teams, platforms, contracts, cells       | Accountability, scaling delivery, incident response  | Assuming technical boundaries automatically map to teams                 |
| Communication | What does this audience need to understand? | Views, viewpoints, summaries, review documents    | Alignment, onboarding, decision support              | Trying to satisfy every audience with one diagram                        |

## Example: One Platform, Many Dimensions

Consider a cloud-native AI platform that supports retrieval, model inference, policy enforcement, audit logging, and developer self-service.

From a structural perspective, the platform may be described as gateways, orchestration services, retrieval services, model adapters, policy engines, and observability components. The key concern is how those parts depend on one another.

From an operational perspective, the same platform may be described as a control plane that manages configuration, a data plane that handles requests and embeddings, and an observability plane that captures traces and audit signals. The key concern is how work flows and where failures or delays can occur.

From a strategic perspective, the platform may prioritize reliability, security, and cost efficiency over raw feature flexibility. That changes design choices such as isolation levels, caching policy, and deployment patterns.

From an ownership perspective, the platform team may own the shared runtime, product teams may own domain-specific prompts and integrations, and security may own policy guardrails. That distribution affects how quickly the system can evolve.

From a communication perspective, the same reasoning may be packaged differently: executives may need a business capability view, operators may need a runtime dependency view, and security reviewers may need a trust-boundary view.

An image should appear here showing one system projected into multiple architecture dimensions.

## Relationship to Views

Dimensions support reasoning. Views are the communication artifacts produced from that reasoning. The distinction matters because a team often reasons through one or more dimensions before deciding how to package the result for a specific audience and purpose.

One useful chain is:

1. Start with the concern.
2. Choose the dimension that best fits that concern.
3. Reason about options, dependencies, risks, and tradeoffs.
4. Produce a view that communicates the result to the intended audience.

For example, if the concern is dependency control, the structural dimension is usually the right starting point. If the concern is runtime policy enforcement, the operational dimension may be more useful. The resulting view should then be shaped for the people who need to act on it.

## Summary

Architecture dimensions are complementary lenses, not competing definitions of architecture. They help teams choose the right reasoning model for the question in front of them and avoid collapsing structure, runtime behavior, priorities, ownership, and communication into one overloaded artifact.
