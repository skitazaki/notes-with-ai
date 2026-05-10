+++
date = '2026-05-10T13:00:00+09:00'
title = 'AI Agents & Autonomous Authorization'
weight = 6
prev = '/docs/acc/workload-identity'
next = '/docs/acc/defense-in-depth'
+++

AI agents should be treated as constrained operating identities rather than as a user-interface feature layered on top of existing permissions.

## Executive Summary

An AI agent can read context, select tools, generate actions, and operate across multiple systems with speed and scale that humans cannot match. That capability changes the authorization problem. The key issue is not merely whether an agent is authenticated. It is how delegated authority is bounded, explained, monitored, and revoked.

Agent security therefore requires explicit control of tool scopes, memory access, approval boundaries, and execution environments. Without those controls, the combination of broad permissions and probabilistic behavior creates a new class of confused-deputy and prompt-injection risk.

## Core Concepts

### Agents as principals

An agent may act:

- on behalf of a human principal
- under its own service identity
- through delegated capabilities issued for a specific task

These modes should not be conflated. "Acting for a user" is not enough as a trust model. Systems must record who delegated what, for how long, to which tools, and under which policy constraints.

### Key risk areas

- **Prompt injection** can alter tool use or data interpretation.
- **Over-permissioned tools** can turn small context exposure into broad compromise.
- **Memory leakage** can reveal sensitive cross-task data.
- **Multi-agent chains** can blur accountability across planning and execution.
- **Agent impersonation** can occur when tool credentials are shared or ambient.

### Better control models

Promising patterns include capability-based delegation, ephemeral execution identities, human-in-the-loop approval for sensitive actions, sandboxed tool runtimes, and cryptographically bound delegation records.

## Implementation and Operations

### Design guidance

- Issue task-scoped credentials instead of reusing broad user tokens.
- Separate read, write, and approval permissions.
- Isolate agent memory by tenant, workflow, and retention class.
- Treat tool invocation as a policy enforcement point.
- Log intent, prompt context class, selected tools, approvals, and outcomes.

### A practical approval model

Low-risk actions may be pre-authorized within a bounded policy. Medium-risk actions may require secondary checks such as data-classification validation or anomaly detection. High-risk actions such as privilege changes, production writes, or regulated data export should require explicit approval or cryptographic delegation.

The objective is not to block autonomy entirely. It is to make autonomous behavior bounded, observable, and governable.
