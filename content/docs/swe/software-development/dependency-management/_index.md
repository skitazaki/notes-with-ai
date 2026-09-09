---
date: "2026-09-09T00:00:00+09:00"
title: "Dependency Management"
weight: 30
prev: "/docs/swe/software-development/code-review-and-refactoring"
next: "/docs/swe/software-development"
---

Dependencies let teams reuse capabilities they do not need to build themselves. Every dependency also creates an external boundary whose availability, compatibility, security, licensing, and evolution affect the system.

## Know what the system depends on

Direct dependencies are only the visible edge of a larger graph. Transitive packages, build plugins, base images, hosted APIs, and runtime services can all influence production behavior. A useful inventory records versions and provenance and connects each component to an owner and update path.

Lockfiles and immutable artifacts make resolution repeatable. Reproducibility requires more than pinning versions: registries, build tools, platform targets, and generated outputs may also vary. Builds should fail visibly when an expected input cannot be verified rather than silently selecting a substitute.

## Updates and risk

Ignoring updates accumulates compatibility and security risk; accepting every update immediately transfers upstream instability into the product. Teams need an update cadence, automated compatibility evidence, clear handling for urgent vulnerabilities, and a way to retire unsupported components.

Version numbers communicate intent imperfectly. Release notes, API contracts, behavioral tests, and staged rollout provide stronger evidence. Major internal platforms and services should offer migration windows and explicit deprecation policies just as public libraries do.

Reducing dependency count is not an end in itself. A mature, well-supported library can reduce risk compared with bespoke code. The decision should consider criticality, substitutability, maintenance health, privileges, data exposure, and recovery options.

## Summary

Dependency management is lifecycle management for code and services a team uses but does not fully control. Inventories, reproducible resolution, update policy, validation, and retirement planning keep reuse from becoming invisible operational debt.
