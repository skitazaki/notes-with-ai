---
date: "2026-08-09T09:00:00+09:00"
title: "MLOps and LLMOps"
weight: 11
prev: "/docs/ai/data-for-ai"
next: "/docs/ai/mlops-and-llmops/model-operations"
---

Model deployment is not the end of AI delivery. It is the beginning of operational responsibility. Once a model influences real workflows, teams need repeatable ways to version it, observe it, evaluate drift, manage change, and improve behavior without losing control of production risk.

That is the shared logic behind MLOps and LLMOps. Both disciplines exist because AI systems are probabilistic, data-dependent, and sensitive to change in ways that traditional software delivery alone does not fully capture.

![MLOps and LLMOps comparison showing their shared operational lifecycle and the additional prompt, retrieval, safety, runtime, and feedback concerns in LLM-based applications.](mlops-and-llmops.webp)

## Definition

MLOps is the operational discipline for deploying, monitoring, versioning, and continuously improving machine-learning systems. LLMOps extends similar principles to systems built on large reusable models, where prompts, retrieved context, tool access, and safety constraints play a larger role in behavior.

The paired framing is useful because the operational patterns overlap strongly even when the system types differ.

## Why Operations Matter

An AI system can degrade without any application code changing. Data distributions drift, labels become stale, retrieval corpora evolve, prompts are revised, model providers change behavior, and cost or latency profiles shift under real demand. Operations matter because the system’s behavior surface is larger than a code deployment.

This means release discipline, observability, and evaluation must cover more than binaries or containers.

## Topic Pages

{{< cards >}}
{{< card link="model-operations/" title="Model Operations" icon="document-text" subtitle="Lifecycle control, observability, and operating concerns for ML and LLM systems" >}}
{{< /cards >}}

## Relationship to Engineering and Governance

AI engineering defines the product behavior that needs to be operated. MLOps and LLMOps keep that behavior measurable and manageable over time. Responsible AI depends on these operational disciplines because policy controls, review requirements, and incident response are ineffective if the system cannot be observed and versioned properly.

## Summary

MLOps and LLMOps bring delivery discipline to systems whose behavior depends on data, models, context, and runtime interaction. Their role is to keep AI systems observable, controllable, and improvable after initial release. That operational layer is what makes model-centric systems sustainable in production.
