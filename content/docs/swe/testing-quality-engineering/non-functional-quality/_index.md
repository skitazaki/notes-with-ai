---
date: "2026-09-09T00:00:00+09:00"
title: "Non-Functional Quality"
weight: 30
prev: "/docs/swe/testing-quality-engineering/test-levels"
next: "/docs/swe/testing-quality-engineering"
---

Software can produce correct answers and still be unfit for use. Performance, security, accessibility, resilience, usability, and operability shape whether behavior remains acceptable under real conditions.

## Make qualities testable

The label “non-functional” can be misleading: these qualities are experienced as concrete system behavior. Replace vague goals such as “fast” or “secure” with observable expectations tied to users, workloads, threats, and operating limits.

Performance testing examines latency, throughput, resource use, and saturation under representative load. Results depend on data shape, concurrency, dependencies, and environment, so a single headline number is rarely sufficient. Budgets and distributions are more informative than averages alone.

Security testing combines static and dynamic analysis, dependency checks, configuration review, threat-informed scenarios, and human expertise. Passing a scanner does not establish security; controls must be evaluated against relevant attacker capabilities and trust boundaries.

Accessibility testing uses automated checks to find detectable issues and manual evaluation to assess keyboard operation, assistive technology, content meaning, and complete journeys. Resilience testing introduces controlled failures to verify timeouts, isolation, degradation, and recovery. Such experiments require explicit limits and observability.

Quality attributes interact. Encryption may add latency, caching may weaken freshness, redundancy may increase cost, and aggressive recovery may overload dependencies. Testing should expose these trade-offs so product and engineering decisions are explicit.

## Summary

Non-functional quality is observable behavior under constraints. Measurable expectations, representative conditions, complementary methods, and explicit trade-offs turn broad quality claims into engineering evidence.
