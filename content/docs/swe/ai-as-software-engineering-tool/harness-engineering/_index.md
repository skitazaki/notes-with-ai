---
date: "2026-09-09T00:00:00+09:00"
title: "Harness Engineering"
weight: 20
prev: "/docs/swe/ai-as-software-engineering-tool/coding-agents"
next: "/docs/swe/ai-as-software-engineering-tool/evaluation-and-security"
---

Harness engineering designs the environment in which an AI agent performs work. The harness combines instructions, context, tools, permissions, execution isolation, feedback, state, and human checkpoints into a dependable workflow.

## Shape the work environment

Instructions should define outcomes and durable constraints without prescribing unnecessary implementation detail. Context should be authoritative, relevant, and current. Repository-scoped guidance can encode commands, architecture boundaries, and validation expectations close to the code they govern.

Tools turn model proposals into observable operations. Narrow schemas, explicit targets, timeouts, and structured results reduce ambiguity. Read, write, execute, network, credential, and external-effect capabilities should be granted separately. Sandboxing limits consequences but does not determine whether an action is appropriate.

## Close the feedback loop

Agents need feedback they can interpret and act upon. Fast focused checks guide local edits; broader tests and builds detect integration effects; visual or behavioral inspection validates what static checks cannot. Failures should expose enough context for diagnosis without leaking secrets.

State management determines what persists across steps and sessions. Plans, diffs, test results, and explicit decisions are safer than relying on hidden conversational memory. When multiple agents or people participate, ownership of files, runtime resources, and final integration must be clear.

Human checkpoints belong before consequential or difficult-to-reverse actions and where requirements are genuinely ambiguous. Too many low-value confirmations create habituation; too few make intervention impossible. A checkpoint should present the intended action, exact scope, likely impact, and available recovery.

## Summary

Harness engineering converts general model capability into a constrained engineering process. Good context, purpose-built tools, separated authorities, useful feedback, explicit state, and meaningful human control determine the quality of the complete system.
