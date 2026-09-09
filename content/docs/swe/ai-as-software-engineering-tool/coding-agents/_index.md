---
date: "2026-09-09T00:00:00+09:00"
title: "Coding Agents"
weight: 10
prev: "/docs/swe/ai-as-software-engineering-tool"
next: "/docs/swe/ai-as-software-engineering-tool/harness-engineering"
---

Coding agents use models and tools to perform multi-step software-engineering work: exploring a repository, editing files, running checks, and presenting evidence. Their ability to act makes workflow design and authority as important as model capability.

## Roles and task boundaries

Agents can support understanding, implementation, testing, review, migration, and operational investigation. A good task states the desired outcome, scope, invariants, and completion evidence. It distinguishes read-only exploration from modification and identifies effects—such as deployments, messages, or data changes—that require separate authority.

Repository instructions, issue context, source code, and tool output may conflict or contain untrusted text. Agents need a clear instruction hierarchy and the smallest relevant context. More context can add noise, expose information, and make critical constraints harder to find.

## A collaborative workflow

Before editing, an agent should inspect local conventions and current state. During implementation it should make bounded changes and obtain feedback from tests, linters, builds, or rendered behavior. The final handoff should describe the outcome, residual risks, and validation—not merely claim success.

Autonomy is multidimensional. Permission to read a repository does not imply permission to execute arbitrary code, access a network, use credentials, modify production, or communicate externally. Reversibility, impact, and observability should determine which steps can proceed automatically and where human review belongs.

Agents can parallelize independent work, but coordination overhead and merge risk remain. Shared files, runtime state, and unclear ownership can erase the benefit. Decomposition should create truly separate scopes with explicit integration responsibility.

## Summary

Coding agents are participants in an engineering workflow, not autonomous sources of truth. Clear tasks, bounded authority, repository-aware execution, and evidence-based handoff make their work useful and reviewable.
