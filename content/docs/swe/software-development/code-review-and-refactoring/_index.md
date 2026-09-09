---
date: "2026-09-09T00:00:00+09:00"
title: "Code Review & Refactoring"
weight: 20
prev: "/docs/swe/software-development/version-control-and-integration"
next: "/docs/swe/software-development/dependency-management"
---

Code review and refactoring are complementary practices for keeping change understandable. Review tests a proposed change against shared knowledge; refactoring improves internal structure so later changes remain economical.

## Reviewing intent and risk

A review begins with the problem, constraints, and expected behavior—not with formatting details in the diff. Automated tools should handle repeatable mechanical checks. Reviewers can then focus on correctness, boundaries, failure modes, security, operability, and whether the change is simpler than its alternatives.

Small changes shorten review time and make missing cases easier to see. Authors should provide context and validation evidence; reviewers should distinguish blocking defects from suggestions. Ownership remains shared: approval is evidence of review, not a transfer of responsibility from author to reviewer.

## Refactoring safely

Refactoring changes internal structure without intentionally changing observable behavior. Common goals include clarifying names, separating responsibilities, removing duplication, and replacing hidden coupling with explicit interfaces. The goal is not maximal abstraction, but a structure that fits current knowledge and likely change.

Behavior-preserving work needs a safety net. Focused tests, incremental commits, static analysis, and comparison of production signals can all provide evidence. Large rewrites combine structural and behavioral change, making failures harder to localize; a sequence of bounded transformations is usually safer.

Review also spreads system knowledge, but it should not be the only mechanism. Design notes, pairing, ownership rotation, and readable code prevent critical understanding from depending on one recurring reviewer.

## Summary

Effective review directs scarce human attention toward intent and risk. Disciplined refactoring uses evidence and incremental change to preserve the system's capacity to evolve.
