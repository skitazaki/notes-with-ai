---
date: "2026-09-09T00:00:00+09:00"
title: "Coding Agents"
weight: 10
prev: "/docs/swe/ai-as-software-engineering-tool"
next: "/docs/swe/ai-as-software-engineering-tool/harness-engineering"
---

Coding agents are not just code-generation utilities; they execute concrete software-engineering tasks such as repository understanding, implementation, validation, and review handoff. Because they chain these tasks, design decisions must cover not only model quality but also endpoint selection, runtime environment, and authority boundaries.
Coding agents use models and tools to perform multi-step software-engineering work: exploring a repository, editing files, running checks, and presenting evidence. Their ability to act makes workflow design and authority as important as model capability.

## Interaction surfaces

The same coding agent can appear through different interaction surfaces: terminal interfaces, dedicated desktop applications, and editor or plugin integrations. Each surface changes how users issue instructions, review actions, and approve side effects.

Surface choice also determines practical constraints such as available tools, context visibility, execution permissions, and collaboration flow. In practice, it is useful to design the operating surface first, then choose model and endpoint combinations that fit that surface.
How those constraints are enforced in execution depends on harness design; for details, see [Harness Engineering](/docs/swe/ai-as-software-engineering-tool/harness-engineering/).

## Models, endpoints, and access patterns

At the core of a coding-agent stack is a combination choice: which model family, through which endpoint, running in which environment. Major model providers include OpenAI, Anthropic, Google, and Microsoft, and each access pattern changes available resources and constraints such as permission scope, latency profile, data-boundary options, and cost controls.

- Cloud-managed access: examples include GitHub Copilot, OpenAI API, Anthropic API, Google Gemini API, and Azure OpenAI. This usually improves elasticity, but introduces policy, region, network-path, and quota constraints.
- Self-managed cloud execution: teams run their own inference stack on AWS, Azure, or Google Cloud. This increases control, while shifting operations, observability, security hardening, and cost optimization to the team.
- Local execution: models run on developer workstations or internal infrastructure. This can fit privacy or offline requirements, but is constrained by local GPU/CPU/memory and model size.

Hosting services and models are not one-to-one. For example, OpenAI-family models can be consumed directly through OpenAI endpoints, through Azure OpenAI, or through GitHub Copilot. Anthropic models can be reached through Anthropic APIs and cloud-provider-hosted offerings, including Claude on Amazon Bedrock and Claude Platform on AWS. Google models can be used through Gemini API or Gemini Enterprise Agent Platform, while Microsoft model families can be accessed through Microsoft Foundry.

The platform layer can also include patterns where teams use models through platforms such as [Databricks Unity Gateway](https://www.databricks.com/product/artificial-intelligence/unity-gateway) and [Snowflake Cortex AI](https://www.snowflake.com/en/product/features/cortex/). In these patterns, coding-agent requests are accepted through the platform gateway and routed to underlying model providers, including Claude-family models depending on provider availability and region. In hybrid setups, services such as [ngrok](https://ngrok.com/) can be used as a model-routing layer that routes and secures traffic across cloud and local model endpoints.

For open-source or open-weight options, common candidates include Llama, Mistral, and Qwen. They can run in cloud or local environments, but teams must own evaluation quality, guardrails, and update cadence.

## Roles and task boundaries

Agents can support understanding, implementation, testing, review, migration, and operational investigation. A good task states the desired outcome, scope, invariants, and completion evidence. It distinguishes read-only exploration from modification and identifies effects—such as deployments, messages, or data changes—that require separate authority.

Repository instructions, issue context, source code, and tool output may conflict or contain untrusted text. Agents need a clear instruction hierarchy (for example: platform/system constraints, then repository policies, then task-specific requests) and the smallest relevant context. More context can add noise, expose information, and make critical constraints harder to find.

## A collaborative workflow

Before editing, an agent should inspect local conventions and current state. During implementation it should make bounded changes and obtain feedback from tests, linters, builds, or rendered behavior. The final handoff should describe the outcome, residual risks (such as unexecuted tests or unverified production impact), and validation—not merely claim success.

Autonomy is multidimensional. Permission to read a repository does not imply permission to execute arbitrary code, access a network, use credentials, modify production, or communicate externally. Reversibility, impact, and observability should determine which steps can proceed automatically and where human review belongs.

Agents can parallelize independent work, but coordination overhead and merge risk remain. Shared files, runtime state, and unclear ownership can erase the benefit. When splitting work, define independent scopes and assign clear ownership for integrating the outputs.
For parallel execution, isolating each workstream with `git worktree` helps reduce cross-task interference by giving each agent or contributor a separate working directory and branch context.

## Summary

Coding agents are participants in an engineering workflow, not autonomous sources of truth. Clear tasks, bounded authority, repository-aware execution, and evidence-based handoff make their work useful and reviewable.
