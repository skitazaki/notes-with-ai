+++
date = '2026-05-10T14:10:00+09:00'
title = 'Concept Dictionary'
weight = 13
prev = '/docs/acc/reference-architectures'
+++

Shared terminology is essential in access-control architecture because small differences in language often hide large differences in trust assumptions.

## Executive Summary

This dictionary defines core terms used across the library so policy, engineering, platform, and governance teams can discuss the same concepts without ambiguity.

## Core Concepts

### Principal

The active entity requesting or performing an action. A principal may be a human user, service, workload, device, or AI agent.

### Identity

The asserted and validated representation of a principal within a trust domain. One principal may hold multiple identities across systems.

### Subject

The entity about which a policy decision is evaluated. In many systems subject and principal are effectively the same, but the distinction matters when delegated action is involved.

### Resource

The object, service, dataset, endpoint, or capability being accessed.

### Entitlement

A granted permission, role, or capability that allows some class of action.

### Capability

A bounded authority to perform a specific operation, often designed to be delegated, scoped, or time-limited.

### Delegation

The act of granting a principal limited authority to act on behalf of another principal or policy domain.

### Policy

The formal rule set used to decide whether access should be allowed, denied, constrained, or escalated.

### Scope

The bounded range within which a credential, permission, or delegated authority is valid.

### Trust boundary

The point across which assumptions about identity, control, or data handling must be re-evaluated.

### Workload identity

The machine-verifiable identity of a running service, job, container, function, or device.

### Agent

A software system that can plan and execute actions with some degree of autonomy, often using tools, memory, and delegated permissions.

## Implementation and Operations

Terminology should be standardized in policy code, audit records, architecture diagrams, and review processes. If teams use the same word to mean different things, control failures usually follow.
