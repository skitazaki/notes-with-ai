---
date: "2026-09-09T00:00:00+09:00"
title: "Evaluation & Security"
weight: 30
prev: "/docs/swe/ai-as-software-engineering-tool/harness-engineering"
next: "/docs/swe/ai-as-software-engineering-tool"
---

AI-generated engineering work should be evaluated as a change to a system, not as persuasive text. Security determines which inputs may influence the agent and which effects it is allowed to create.

A useful way to think about this topic is that evaluation and security are the same discipline from two angles. Evaluation asks, "How do we know this work is good enough?" Security asks, "What could go wrong if the agent is wrong, misled, or overly powerful?" In both cases, the goal is not to make the agent more convincing; it is to make its actions inspectable, attributable, and proportionate to risk. This also requires separating accountability from responsibility: accountability identifies who can justify a decision, while responsibility identifies who executes it and owns remediation when something fails.

## Evaluate the complete workflow

Useful evidence includes focused tests, regression checks, static analysis, builds, security scans, diff inspection, and direct validation of requested behavior. The mix follows impact: documentation formatting needs less assurance than authentication changes or production migrations.

Agent performance is task- and environment-specific. General benchmarks cannot establish reliability in a particular repository. Evaluate representative tasks, known failure modes, recovery effort, review burden, and whether the workflow improves outcomes rather than merely increasing generated output.

A practical evaluation harness should answer several questions:

- What was the exact task and the expected outcome?
- Which checks were run, and which were omitted?
- What evidence supports the claim that the change is correct?
- Which risks remain unverified?
- What would a human reviewer need to inspect before approving the change?

An independent evaluator can reduce correlated mistakes, but independence requires different evidence or perspective—not simply a second invocation with the same context. Human reviewers need the original request, resulting diff, validation results, and unresolved uncertainty.

## Constrain trust and authority

Prompts, repository files, issues, webpages, and tool output may contain untrusted instructions. The harness should separate data from authority, prioritize trusted policy, and prevent retrieved content from silently expanding permissions.

Use least privilege and short-lived access. Keep secrets outside model-visible context where possible, scope credentials to the operation, and record external effects. Approval should occur before the consequential action, with exact targets and impact visible. Logs must support accountability and responsibility handoff without becoming a new store of sensitive data.

Several design patterns make this easier:

- narrow trust boundaries: treat external text as input to reason about, not as policy
- least privilege: grant exactly the permissions required for the current action
- explicit approvals: require a human sign-off before high-risk or hard-to-reverse operations
- auditable logs: record the action, the actor, the evidence, and the approval path
- controlled side effects: isolate writes, deployments, and external calls behind reviewable boundaries

## Risk tiers and review posture

Not all AI-assisted work has the same risk profile. A low-risk change to a doc page, a style fix, or a small local refactor should not require the same review process as a production migration, a credential update, or a permissions change.

A good system maps each action to a risk tier using consistent criteria: potential impact, reversibility, and authority required.

- low risk
  - typical actions: read-only analysis, small local edits, reversible documentation or style changes
  - authority profile: no secret access and no external side effects
  - review posture: targeted checks and normal peer review are usually sufficient
- moderate risk
  - typical actions: multi-file refactor, config change, schema migration, or validation-dependent workflow change
  - authority profile: broader repository write scope or indirect operational impact
  - review posture: stronger evidence, explicit validation coverage, and clearer reviewer checkpoints
- high risk
  - typical actions: production deployments, destructive commands, permission changes, secret handling, cross-environment data changes
  - authority profile: direct operational control, sensitive data access, or hard-to-reverse effects
  - review posture: explicit pre-action approval, independent verification, and auditable decision records

The review posture should scale with the tier, not with developer confidence or output fluency.

## Common failure modes

Evaluation and security fail in predictable ways when harness design is insufficient:

- the agent is trusted because it writes plausible text rather than because the code is validated
- broad context is merged without verifying whether each source is authoritative and current
- credentials or secrets are exposed to the model or copied into logs
- an agent is allowed to create external effects without explicit approval
- the system treats a successful general benchmark as proof of repository-specific safety

The fix is not to add more cautionary language. It is to make the workflow explicit: define the scope, the authority, the evidence, and the review gates before the action is allowed.

## Summary

Evaluation establishes evidence for a particular change and workflow. Security limits what untrusted inputs and imperfect decisions can cause. Together they make agent-assisted work reviewable, attributable, and proportionate to risk.
