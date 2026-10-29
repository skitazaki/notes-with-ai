---
date: "2026-08-17T09:00:00+09:00"
title: "Data Observability"
weight: 4
prev: "/docs/data/engineering/orchestration"
next: "/docs/data/engineering"
---

Data Observability provides the signals and context needed to understand the operational state of data pipelines and data flows. It helps operators answer: **What is happening in the data system, and why?**

Monitoring checks known conditions. Observability combines multiple signals and dependencies so teams can investigate conditions they did not predict in advance. Effective observability connects execution behavior to the data assets and consumers affected by it.

```text
Pipeline
├── Execution
│   ├── status
│   ├── duration
│   └── failures
│
├── Data Flow
│   ├── freshness
│   ├── volume
│   └── schema
│
└── Dependencies
    ├── upstream
    └── downstream
```

## Operational Signals

### Pipeline Health and Execution

Execution signals include run status, task duration, retry count, queue time, resource use, and failure category. They show whether work started, progressed, completed, or stalled. Logs and traces add diagnostic detail, while deployment and configuration records show what changed before an incident.

A successful task is necessary but not always sufficient. It may have processed no input, produced an unusually small output, or published later than consumers require.

### Freshness and Latency

**Freshness** describes how current an available dataset is relative to its source or expected update. **Latency** measures elapsed time through part or all of a flow. End-to-end latency can include source publication, ingestion delay, queue time, processing, and serving.

These signals should be interpreted against explicit service expectations. A five-minute delay may be irrelevant for a monthly report and critical for an operational decision.

### Throughput and Volume

Record counts, byte rates, partitions, and event throughput reveal missing, duplicated, delayed, or unexpectedly large inputs. Changes may indicate a failure, a legitimate business event, or an upstream behavior change. Observability identifies the deviation and supplies context; it does not decide fitness for use without domain expectations.

### Schema Changes

Schema additions, removals, type changes, and compatibility violations can break a flow or silently alter meaning. Capturing schema versions and comparing them across producers, pipelines, and consumers makes the scope of a change visible.

### Dependencies and Lineage

An individual failure matters in proportion to what depends on it. Upstream dependencies help locate the cause; downstream lineage helps identify affected datasets, dashboards, applications, and AI workflows. Ownership and criticality metadata route incidents and help prioritize response.

See [Metadata](/docs/data/metadata/) for deeper treatment of lineage, dependency information, ownership, and operational metadata.

## Alerting

Alerts should represent actionable conditions rather than every abnormal measurement. Useful alerts identify the affected asset, observed behavior, expected behavior, severity, time window, recent changes, dependencies, owner, and investigation entry point.

Static thresholds work for clear limits. Rate-of-change and anomaly detection can reveal less predictable behavior, but they require controls for seasonality and normal variation. Alert routing, grouping, suppression, and escalation reduce noise and preserve operator attention.

An alert is the start of response, not the observability outcome. Teams also need dashboards for situational awareness, retained evidence for investigation, and service-level reporting for recurring improvement.

## Incident Investigation

A practical investigation moves from impact toward cause:

1. Identify affected data assets and consumers.
2. Establish when the behavior began and which service expectation was breached.
3. Inspect recent code, configuration, schema, source, and infrastructure changes.
4. Follow lineage and dependencies upstream to locate the earliest abnormal signal.
5. Determine whether retry, replay, rollback, backfill, or quarantine is safe.
6. Validate restored outputs and communicate remaining uncertainty downstream.

Correlation identifiers, run IDs, dataset versions, event positions, and deployment records make this path reproducible. Without them, operators are forced to infer relationships from timestamps and names.

## Observability and Data Quality

**Observability asks:** What is happening in the data system, and why?

**Data Quality asks:** Does the data meet the expectations required for its intended use?

The concepts overlap. Freshness, unexpected volume, schema drift, or distribution changes can be both operational and quality signals. The distinction is their purpose: observability exposes system and data behavior for operation and diagnosis, while Data Quality Management defines, measures, and governs fitness-for-use expectations.

Pipeline checks can implement quality rules and observability can report their results, but neither should silently define business acceptability. See [Data Management](/docs/data/management/) and [Data Quality Dimensions](/docs/data/management/data-quality-dimensions/) for quality concepts and management practices.

## Designing for Diagnosis

Observability cannot be added entirely after a pipeline is built. [Data Ingestion](../ingestion/) should preserve event and ingestion times, source positions, and replay context. [Data Processing](../processing/) should record input and output versions, partition boundaries, and transformation identity. [Data Orchestration](../orchestration/) should expose workflow state, parameters, attempts, and dependencies.

Together, these signals make recovery safer. Operators can determine what ran, what data it handled, which outputs it produced, who depends on them, and whether a retry or backfill will create duplicate or inconsistent results.
