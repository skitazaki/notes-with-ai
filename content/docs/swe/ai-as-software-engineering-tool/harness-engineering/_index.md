---
date: "2026-09-09T00:00:00+09:00"
title: "Harness Engineering"
weight: 20
prev: "/docs/swe/ai-as-software-engineering-tool/coding-agents"
next: "/docs/swe/ai-as-software-engineering-tool/evaluation-and-security"
---

Harness engineering designs the environment in which an AI agent performs work. The harness combines instructions, context, tools, permissions, execution isolation, feedback, state, and human checkpoints into a dependable workflow.

A useful way to think about it is that the model is the decision engine, while the harness is the operating system around it. The model proposes actions; the harness decides which actions are possible, which data the model can see, which tools it may call, what environment it runs in, and how results are validated before they become part of the system.

Repository-specific operating guidance belongs in [AGENTS.md](/docs/ai/context-engineering/agents-md/). Reusable procedures and resources live in [Agent Skills](/docs/ai/context-engineering/agent-skills/). Tool access and standards sit in [Tools and MCP](/docs/ai/context-engineering/tools-and-mcp/). These pieces are part of the same harness stack: they shape what the agent can do, what it knows, and how its work is checked.

## What the harness is responsible for

The harness is not a single switch or a single prompt. It is the full substrate that governs agent behavior across a task. In practical terms, it is a set of control layers that shape how the agent works and how its output is verified.

### 1. Task framing and constraints

A task should define the intended outcome, scope boundaries, invariants, and acceptance evidence. This is often more important than model quality. A vague request leads to broad exploration, weak decisions, and hidden assumptions; a well-scoped task narrows the search space and makes the result inspectable.

Good task framing should answer:

- What problem is being solved?
- What are the in-scope and out-of-scope areas?
- What is the expected change in behavior?
- What checks count as completion evidence?
- Which side effects require human review or approval?

The strongest task definitions are operational rather than literary. They describe the work in terms of repository actions, change boundaries, and validation criteria.

### 2. Authoritative context

Context is not a bag of information; it is a curated set of facts the agent can rely on. The best context is small, current, and aligned with the code it must modify. Repository instructions, architecture docs, issue descriptions, recent diffs, failing logs, and test outputs all become useful only when they help answer the actual question.

A common mistake is to overfeed the model with broad repository context or historical chatter. This increases noise, exposes unnecessary details, and makes important constraints harder to find. Instead, the harness should provide the smallest authoritative context needed for the decision at hand, and it should distinguish source-of-truth data from commentary or untrusted input.

In practice, the harness should separate:

- durable repository policy: architecture boundaries, conventions, commands, and ownership rules
- task context: issue, PR, failing test, and user goal
- runtime evidence: logs, build output, failure traces, and environment state
- low-trust material: web pages, issue comments, generated summaries, and ad hoc text that may be stale or incorrect

### 3. Tool surface and authority boundaries

The tool surface is the agent's interface to the real world. It defines which capabilities are actually exposed, what arguments they accept, and which authority each action carries. This is where the harness decides whether the agent can read a file, write a patch, run a shell command, or trigger a remote workflow.

This is not the same as controlling where the agent runs. The authority boundary answers: "What actions are available to this agent at all?" The runtime boundary answers: "What can this agent actually touch when it runs?"

A good harness separates:

- read-only tools from write tools
- local repository actions from remote actions
- shell execution from file modification
- API access from credential use
- user-approved actions from autonomous actions

At a minimum, the harness should decide whether a tool can:

- read a repository or a subset of files
- write files or create branches
- execute commands in a shell
- trigger networked workflows or external APIs
- use credentials or secrets
- modify environments or production systems
- send messages or create external artifacts

Permissions should be granted by risk, not by convenience. Reading a repository is not the same as making a production change, and writing a file is different from creating a deployment or modifying a database. Each authority should be explicit and separately reviewable.

Network access and credential access are often discussed alongside tool permissions, but the main responsibility here is policy at the interface layer: the harness decides which capabilities exist and which actors may invoke them. It does not, by itself, define the operating sandbox or secret storage boundary.

### 4. Execution isolation and runtime boundaries

Execution environment matters as much as prompt quality. A coding agent working in a local development directory, a temporary worktree, a sandboxed CI runner, or a remote execution host behaves differently because the environment changes what it can touch and what it can observe.

This layer is about the actual runtime boundary: where the work happens, what it can reach, and how credentials are resolved. The key distinction is that the tool surface describes available actions, while the runtime boundary describes the containment and control around those actions.

Good execution isolation provides at least four protections:

- filesystem isolation: a separate checkout or worktree reduces accidental cross-task interference
- process isolation: limited shell access prevents destructive commands and broad process execution
- network isolation: restricted outbound access reduces opportunities for abuse and accidental data egress
- credential isolation: secrets should remain outside the model context and be injected only through approved, scoped mechanisms

The harness is not just about security; it is about making agent behavior predictable. A controlled environment makes failures easier to diagnose and easier to replay. This is where network egress policy, secret storage, and runtime sandboxing belong; those are operational controls around the agent, not the capabilities exposed in the agent interface itself.

### 5. Feedback and observability

Agents need feedback they can interpret and act upon. Fast, focused checks guide local edits; broader tests and builds detect integration effects; visual or behavioral inspection validates what static checks cannot.

The harness should make the loop short and legible:

- the agent gets the result of a targeted check quickly
- failures are reported with enough state to diagnose the issue
- the next action is bounded by what the evidence supports
- uncertain conclusions are surfaced instead of silently assumed

Useful feedback is not only pass/fail. It also includes the exact command, the relevant files, the partial output, and the remaining decision point. For example, reporting only "failed" is not enough; returning the failing location and key log lines lets the model choose the next change based on evidence. Without that evidence, the model drifts toward guesswork, which increases unnecessary retries and incorrect patches.

### 6. State, memory, and coordination

A good harness treats memory as explicit state, not hidden conversation history. Plans, diffs, tool results, validation outcomes, and important decisions should persist in a structured form across steps and sessions.

This matters most when multiple agents or people participate. Shared state must answer questions such as:

- Which file or branch is owned by which actor?
- What has already been validated?
- Which plan is current?
- What is still pending review?

Without explicit state management, the system drifts toward confusion: duplicated edits, stale assumptions, conflicting plans, and inconsistent handoffs. In collaborative settings, the harness should define ownership boundaries and integration points before parallel work begins.

## Human checkpoints and approval design

Human-in-the-loop is not a single confirmation dialog. It is the deliberate placement of review where judgment matters most. The right checkpoint appears before actions that are costly, hard to reverse, or operationally sensitive.

Effective checkpoints include:

- the intended action and exact scope
- likely impact and affected systems
- available rollback or recovery options
- relevant evidence already gathered
- the decision the human is being asked to approve

A checkpoint should not be a generic "continue?" prompt. It should make the human's role obvious and the tradeoff legible. This avoids two bad extremes: too many low-value confirmations that cause habituation, and too few confirmations that leave no meaningful intervention point.

## Typical harness patterns

Different tasks require different harness shapes. The same model and tool stack can be used in several patterns, each with different tradeoffs.

### Focused editor assistant

This pattern is appropriate for short tasks in a single file or a tightly bounded slice of a repository. The harness emphasizes minimal operational overhead, fast feedback, and narrow context. Read/write authority is limited and review is lightweight.

### Repository task agent

This pattern is appropriate for real feature work or bug fixes across multiple files. The harness supplies a repository-aware context, explicit task boundaries, a controlled worktree, and a validation loop. It is designed for multi-step execution with clear handoff and re-checkpoints.

### Delegated automation or issue-driven agent

This pattern runs on recurring operational tasks or a specific issue, often without constant human steering. The harness needs stronger state tracking, permission boundaries, and result summarization because the agent acts over longer intervals and may need to resume later. To keep restarts consistent, teams should encode repeatable procedures in [Agent Skills](/docs/ai/context-engineering/agent-skills/).

### Multi-agent coordination

When several agents work in parallel, the harness must define shared boundaries and integration rules. Independent workstreams should be isolated by file ownership, worktree or branch separation, or explicit task partitioning. Coordination overhead and merge conflicts can erase any gain from parallel execution unless the harness is designed for them.

## Common failure modes

An insufficiently designed harness often fails in recognizable ways:

- The model is given too much irrelevant context and loses the actual constraint.
- Tools are too broad, allowing writes or commands without clear limits.
- The environment is shared across tasks, creating state leakage and inconsistent results.
- Validation is delayed until late, when hidden assumptions have already shaped the patch.
- Human review is placed too late, after a risky action has already happened.
- The model is trusted to remember intent across sessions instead of storing explicit state.

Most failures are not model failures alone. They are harness design failures: the environment did not constrain, observe, or verify the work well enough.

## Design principles

A robust harness follows a few simple principles:

- Break the task into executable steps and completion criteria before acting.
- Provide only context that is directly relevant, up to date, and source-backed.
- Avoid broad generic authority and expose purpose-scoped, safe tools with explicit interfaces.
- Separate read, write, execution, network, and credential authority.
- Use isolated execution environments and structured state.
- Close the feedback loop with fast, meaningful validation.
- Place human review at genuine decision points, not as ritual.

## Summary

Harness engineering converts general model capability into a constrained engineering process. The model is not the whole system; the system is the model plus the instructions, context, tools, permissions, environment, feedback loop, and checkpoints that govern its behavior. A good harness makes the work inspectable, auditable, and recoverable. That is what turns AI from a clever conversational tool into a usable engineering collaborator.
