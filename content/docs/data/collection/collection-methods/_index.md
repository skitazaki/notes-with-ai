---
date: "2026-08-30T00:00:00+09:00"
title: "Collection Methods"
weight: 2
prev: "/docs/data/collection/data-sources"
next: "/docs/data/collection/collection-design-and-sampling"
---

A collection method is the way a phenomenon, activity, assertion, or measurement becomes data. The method shapes what is visible, what is missed, how precise the result is, and how people or systems may change their behavior in response to observation.

## Common Methods

- **Direct observation and measurement** records a phenomenon through a person, instrument, or controlled procedure.
- **Application instrumentation** emits purpose-defined events and attributes as users and software interact with a system.
- **Transactional capture** creates records as part of executing a business transaction or workflow.
- **Forms and user input** collect information explicitly supplied by a person, operator, or representative.
- **Surveys and research methods** ask a selected population for responses under a defined study design.
- **Sensors and connected devices** convert physical conditions, locations, or equipment states into measurements.
- **Logs and telemetry** record software or infrastructure activity, usually to support operation, security, or analysis.
- **External acquisition** obtains datasets maintained by partners, vendors, researchers, or public bodies.
- **Web collection** observes accessible web content or behavior under applicable permissions, terms, and technical constraints.

These descriptions concern how information is created or selected. Whether the resulting records later move through files, APIs, database extraction, CDC, or event streams is an [ingestion](/docs/data/engineering/ingestion/) design question.

## Method Tradeoffs

**Active and passive collection.** Active collection asks a person or system to provide information, as with a form or survey. It can make purpose and requested fields explicit, but participation and response behavior affect coverage. Passive collection observes activity without a separate response, as with instrumentation or sensors. It can reduce respondent effort while increasing transparency, proportionality, and contextual-interpretation concerns.

**Direct and indirect collection.** Direct methods observe the phenomenon or obtain information from the person or system concerned. Indirect methods use proxies, intermediaries, or inferred attributes. Indirect data can expand coverage or reduce cost, but the proxy relationship and inference uncertainty must remain visible.

**First-party and third-party collection.** First-party data arises from an organization's own relationship or operation. Third-party data is obtained outside that relationship. This distinction affects provenance, control, permitted use, continuity, and the ability to correct errors; it does not by itself determine quality.

**Continuous and periodic observation.** Continuous observation can reveal sequence and transient states but increases volume, operational dependence, exposure, and retention implications. Periodic observation reduces cost and intrusion but may miss changes between measurement points.

**Exhaustive collection and sampling.** Attempting to capture every event may be appropriate for transactional accountability, yet even apparently exhaustive systems have boundaries and failures. Sampling can reduce cost and risk when designed for the intended inference. [Collection Design and Sampling](../collection-design-and-sampling/) explains those choices in depth.

## Method Shapes Meaning

The same label can represent different facts depending on its method. “Customer location” could mean a billing address entered months ago, a shipping destination for one transaction, an IP-derived estimate, or a device measurement at a specific time. Without the method, time, precision, and purpose, downstream users may treat unlike values as equivalent.

Capture contextual [metadata](/docs/data/metadata/) at creation: the instrument or form version, observation and recording times, unit, precision, collection channel, operator where relevant, and known transformation or inference. [Data Quality](/docs/data/management/data-quality-dimensions/) provides the broader framework for evaluating fitness for use; collection documentation explains why a result has particular quality properties.

## Summary

Choose a collection method for the information and decision it must support. Make the method's effect on behavior, coverage, precision, context, and permitted use explicit before optimizing how the records are transported.
