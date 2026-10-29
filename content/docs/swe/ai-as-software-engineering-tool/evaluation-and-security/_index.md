---
date: "2026-09-09T00:00:00+09:00"
title: "Evaluation & Security"
weight: 30
prev: "/docs/swe/ai-as-software-engineering-tool/harness-engineering"
next: "/docs/swe/ai-as-software-engineering-tool"
---

AI-generated engineering work should be evaluated as a change to a system, not as persuasive text. Security determines which inputs may influence the agent and which effects it is allowed to create.

## Evaluate the complete workflow

Useful evidence includes focused tests, regression checks, static analysis, builds, security scans, diff inspection, and direct validation of requested behavior. The mix follows impact: documentation formatting needs less assurance than authentication changes or production migrations.

Agent performance is task- and environment-specific. General benchmarks cannot establish reliability in a particular repository. Evaluate representative tasks, known failure modes, recovery effort, review burden, and whether the workflow improves outcomes rather than merely increasing generated output.

An independent evaluator can reduce correlated mistakes, but independence requires different evidence or perspective—not simply a second invocation with the same context. Human reviewers need the original request, resulting diff, validation results, and unresolved uncertainty.

## Constrain trust and authority

Prompts, repository files, issues, webpages, and tool output may contain untrusted instructions. The harness should separate data from authority, prioritize trusted policy, and prevent retrieved content from silently expanding permissions.

Use least privilege and short-lived access. Keep secrets outside model-visible context where possible, scope credentials to the operation, and record external effects. Approval should occur before the consequential action, with exact targets and impact visible. Logs must support accountability without becoming a new store of sensitive data.

## Summary

Evaluation establishes evidence for a particular change and workflow. Security limits what untrusted inputs and imperfect decisions can cause. Together they make agent-assisted work reviewable, attributable, and proportionate to risk.
