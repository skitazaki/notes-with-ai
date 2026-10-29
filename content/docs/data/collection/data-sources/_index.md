---
date: "2026-08-30T00:00:00+09:00"
title: "Data Sources"
weight: 1
prev: "/docs/data/collection"
next: "/docs/data/collection/collection-methods"
---

A data source is the origin from which observations, records, measurements, or assertions are acquired. A source is defined by its relationship to the information—not by the connector used to reach it. The same API or file interface can expose an authoritative operational record, a delayed replica, a vendor-curated dataset, or an undocumented derivative, each with different implications.

## Major Source Categories

- **Operational and transactional systems** record business events and current operational state, such as orders, payments, inventory movements, or service cases.
- **Business applications** hold workflow, customer, workforce, finance, and collaboration data, often within externally operated services.
- **Human-entered sources** include forms, interviews, annotations, surveys, and manually maintained records.
- **Application and machine-generated sources** include application events, logs, traces, model outputs, and equipment telemetry.
- **Sensors and devices** measure physical conditions or behavior with limits determined by placement, calibration, resolution, and connectivity.
- **Partners and suppliers** provide data created within another organization's processes and control environment.
- **Commercial and licensed datasets** are acquired under terms that may constrain use, combination, retention, and redistribution.
- **Public and open data** is published for broad access under stated licenses, policies, or public mandates.
- **Web-derived data** is observed from web resources whose availability, meaning, terms, and structure can change without notice.

These categories can overlap. A partner feed may originate in an operational system; a public dataset may aggregate sensor observations; an application log may contain human activity. Classification is useful only when it exposes ownership, authority, and limitations.

## Authority and Ownership

A **system of record** is recognized as authoritative for a defined fact or process. It is not necessarily authoritative for every field it contains. A customer-service system might be authoritative for case status while only copying a customer address from another system.

A **secondary source** reproduces, transforms, aggregates, or republishes information from elsewhere. Secondary sources can be easier or safer to access, but may introduce delay, filtering, altered definitions, or uncertain correction behavior. Teams should record both the immediate source and, where known, the original authority.

Source ownership answers who can explain the data, approve access, correct errors, communicate changes, and accept collection impact. Technical custody alone does not establish authority. For external data, these responsibilities may be divided among the originating organization, publisher, reseller, and internal contract owner.

## Evaluating a Source

Evaluate a candidate source against the intended purpose rather than applying a universal trust score:

| Concern       | Questions to ask                                                           |
| ------------- | -------------------------------------------------------------------------- |
| Authority     | Who creates the fact, and is this the recognized source for it?            |
| Provenance    | Can the data be traced to its origin, method, and version?                 |
| Reliability   | Are omissions, corrections, delays, and outages visible?                   |
| Volatility    | How often do values, definitions, interfaces, or availability change?      |
| Accessibility | Is access technically feasible and organizationally authorized?            |
| Coverage      | Which populations, events, regions, or periods are represented or absent?  |
| Constraints   | What operational, legal, contractual, ethical, cost, or rate limits apply? |

Trustworthiness is contextual. A rapidly updated secondary feed may be suitable for situational awareness but not for financial reconciliation. A system of record can still contain measurement error or exclude activity that occurs outside its workflow.

## Primary and Derived Data

**Primary data** is collected directly for the present purpose or directly from the observed source. **Derived data** results from transformation, inference, aggregation, linkage, or republishing. The distinction affects how confidently a consumer can interpret values and correct errors, but primary does not automatically mean accurate and derived does not automatically mean inferior.

Preserve enough [metadata](/docs/data/metadata/) to distinguish observation from inference and to identify source, owner, collection method, observation time, processing history, and applicable restrictions. [Data Architecture](/docs/data/architecture/) addresses how sources fit into the wider system topology. Once a source and collection scope are established, [Data Ingestion](/docs/data/engineering/ingestion/) addresses reliable transfer rather than source authority.

## Summary

Source selection determines the authority, coverage, continuity, and constraints inherited by a dataset. Treat sources as accountable origins with known provenance and limitations, not merely endpoints from which records can be extracted.
