---
date: "2026-08-30T00:00:00+09:00"
title: "Collection Design and Sampling"
weight: 3
prev: "/docs/data/collection/collection-methods"
next: "/docs/data/collection/external-and-third-party-data"
---

Collection design defines which parts of reality a dataset can represent. Before implementation, it establishes the population, observation unit, scope, granularity, timing, and selection method. These choices matter for analytical datasets and for operational data used to trigger actions, allocate resources, or maintain state.

## Define the Observation

Begin with the intended purpose and distinguish several elements:

- **Target population:** the people, entities, events, or conditions about which a conclusion or action is intended.
- **Unit of observation:** what one record or measurement represents, such as a person, account, device, transaction, visit, or time interval.
- **Scope and coverage:** which locations, channels, systems, periods, states, and eligible units can actually be observed.
- **Granularity:** the level of detail retained, including spatial, temporal, categorical, and numeric precision.
- **Frequency and timing:** when observations occur and how repeated observations relate to the phenomenon.
- **Observation window:** the period during which an event or condition can be detected and attributed.

These definitions prevent a convenient source from silently becoming the definition of the population. Application users, for example, are not necessarily equivalent to all customers, and completed transactions do not represent abandoned attempts.

## Sampling and Coverage

A sample selects part of a target population for observation. Probability-based designs can support quantified inference when selection probabilities and nonresponse are understood. Stratification, clustering, or deliberate oversampling may improve precision for important groups. Non-probability samples can still support operational or exploratory purposes, but their limits should not be hidden behind dataset size.

Coverage error occurs when the collection frame excludes or duplicates parts of the target population. Missing observations can also arise through nonresponse, offline devices, failed instrumentation, inaccessible channels, or rules that filter events before recording. Missingness is therefore often evidence about the collection process, not merely an empty value to impute later.

## Bias Introduced at Collection

- **Selection bias** arises when inclusion is related to the characteristic being studied or acted upon.
- **Measurement bias** arises when an instrument, question, proxy, or procedure systematically differs from the intended concept.
- **Survivorship effects** occur when only entities or processes that remain visible are analyzed.
- **Timing bias** occurs when observation windows favor particular cycles, states, or response patterns.
- **Behavioral effects** occur when observation or incentives change what participants report or do.

Representativeness is always relative to a target population and purpose. A dataset can be representative for service operations during staffed hours and unsuitable for estimating all-day customer demand.

## Precision, Cost, and Consequence

More data is not automatically better. Greater frequency and granularity can improve detection or analysis, but also increase collection cost, source load, privacy exposure, security obligations, and the chance that noisy precision is mistaken for accuracy. Set detail and cadence according to the decision's consequence and required uncertainty, then collect no more than the purpose justifies.

Document assumptions, exclusions, frame versions, sampling rules, instrument changes, and observation windows as [metadata](/docs/data/metadata/). Use [Data Understanding](/docs/data/analytics/data-understanding/) to examine how available data supports analysis, and [Data Quality](/docs/data/management/data-quality-dimensions/) for the wider quality-management framework.

## Why Processing Cannot Always Repair Collection

Downstream processing can standardize formats, detect anomalies, weight a known sample, and sometimes estimate missing values. It cannot recreate an unobserved population with certainty, determine an undocumented measurement method, or remove bias when the selection mechanism is unknown. A precise pipeline faithfully processing systematically incomplete observations still produces systematically incomplete evidence.

## Summary

Collection design makes the dataset's claim about reality explicit. Define population, observation unit, scope, timing, selection, and limitations before collection begins, and preserve those decisions so downstream users can judge fitness for purpose.
