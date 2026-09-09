---
date: "2026-09-09T00:00:00+09:00"
title: "Test Levels"
weight: 20
prev: "/docs/swe/testing-quality-engineering/test-strategy"
next: "/docs/swe/testing-quality-engineering/non-functional-quality"
---

Test levels describe the scope of behavior and boundaries exercised by a check. They are complementary viewpoints, not a ranking from less to more valuable.

## Local and boundary evidence

Unit tests exercise a small unit of behavior and usually give fast, precise failures. The unit may be a function, object, module, or cohesive capability; it is not defined by a mocking framework. Tests should emphasize stable behavior rather than reproduce private implementation structure.

Integration tests verify collaboration across real boundaries such as a database, queue, filesystem, runtime, or remote service. They reveal assumptions about serialization, transactions, configuration, timing, and failure handling. A smaller number of well-chosen integration tests often catches risks that many isolated mocks cannot.

Contract tests verify an interface between parties that can change independently. Consumer- and provider-side evidence can detect incompatible APIs or events without running an entire deployed system. Contracts need versioning, ownership, and retirement rules.

## System journeys

End-to-end tests follow a representative user or system journey through deployed components. They can verify wiring and critical outcomes, but failures are slower and harder to diagnose. Keep the set focused on high-value journeys and rely on lower levels for detailed variations.

The same behavior need not be repeated at every level. Overlap is justified when it protects a critical risk or improves diagnosis; accidental duplication raises maintenance cost without proportionate confidence. Test architecture should follow real system boundaries and supply the earliest credible feedback.

## Summary

Unit, integration, contract, and end-to-end tests answer different questions. A coherent portfolio uses each where its scope, realism, speed, and diagnostic value best match the risk.
