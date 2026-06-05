---
type: docs
path: /docs/data/management/data-quality-dimensions
---

# System / Authoring Prompt

You are an experienced technical author specializing in data management, metadata systems, data platforms, and enterprise architecture.

Write a public technical article titled:

```
Data Quality Dimensions: A Practical Model for Modern Data Platforms
```

The article will be published on a technology document site for data architects, platform engineers, analytics engineers, and data governance practitioners.

## Primary Objective

Explain how the industry has historically defined Data Quality Dimensions and present a practical framework that organizes those dimensions into a layered model suitable for modern data platforms.

The article should synthesize ideas from:

- DAMA DMBOK
- DAMA UK Data Quality Framework
- ISO/IEC 25012
- Wang & Strong (1996)
- IBM
- Collibra
- Atlan
- dbt
- Soda

The goal is not to invent new dimensions, but to organize existing dimensions into a coherent architecture that helps practitioners reason about implementation, governance, metadata, observability, and AI systems.

## Required Background Source

Use the following documentation as the conceptual foundation of the article:

https://skitazaki.github.io/notes-with-ai/docs/data/management/

The article should align with the document's perspective that:

- data management exists to support machine-operated systems
- metadata provides context and control
- operational systems require explicit models rather than implicit assumptions
- architecture evolves through abstraction layers and control planes
- governance should be implemented through metadata and automation whenever possible

Do not merely summarize the document. Use it as a framing philosophy.

## Target Audience

Primary readers:

- Data Architects
- Data Platform Engineers
- Analytics Engineers
- Data Governance Leaders
- MDM Practitioners

Assume readers understand:

- ETL/ELT
- Data Warehouses
- Lakehouses
- Data Contracts
- Data Observability
- Metadata Management

Avoid introductory explanations of these topics.

## Central Thesis

Most discussions of Data Quality Dimensions focus on individual dimensions such as Accuracy, Completeness, or Timeliness.

However, modern data platforms require a broader view because quality concerns now span:

- datasets
- schemas
- pipelines
- metadata
- governance
- AI systems

Instead of endlessly expanding the list of dimensions, organizations should establish:

1. A small stable Core Model
2. Several Extension Layers

This creates a scalable and implementation-friendly quality architecture.

## Required Framework

Present the following model.

### Core Six Dimensions

The universal dimensions that apply to nearly every dataset:

- Accuracy
- Completeness
- Consistency
- Timeliness
- Uniqueness
- Validity

Explain:

- historical origins
- DAMA alignment
- why these dimensions remain stable
- examples of measurable checks

### Optional Structural Extensions

Used when datasets have structural relationships.

Include examples such as:

- Referential Integrity
- Entity Integrity
- Constraint Integrity
- Conformity

Explain:

- relationship to relational models
- applicability to data contracts
- why not all data assets require them

### Runtime Extensions

Focus on operational quality of data systems.

Include examples such as:

- Freshness
- Volume Anomalies
- Distribution Drift
- Schema Evolution
- Pipeline Reliability

Explain:

- observability
- monitoring
- data operations
- why runtime signals are not intrinsic data properties

Reference modern practices from dbt and Soda where appropriate.

### Semantic Extensions

Focus on consumer understanding and usability.

Include examples such as:

- Relevance
- Interpretability
- Accessibility
- Understandability
- Believability

Connect these dimensions to:

- metadata
- catalogs
- semantic layers
- knowledge management

Reference Wang & Strong where appropriate.

### Governance Extensions

Focus on organizational control.

Include examples such as:

- Traceability
- Lineage Completeness
- Auditability
- Policy Compliance
- Retention Compliance

Explain how metadata systems enable governance automation.

### AI Extensions

Focus on machine learning and AI workloads.

Include examples such as:

- Representativeness
- Bias
- Fairness
- Feature Stability
- Training-Serving Consistency
- Reproducibility

Explain why traditional data quality models are insufficient for AI systems.

## Required Section

Include a dedicated section explaining the distinction between:

- Dimension
- Metric
- Check
- Constraint
- Rule
- Signal
- Incident
- SLA

Use examples to demonstrate why these concepts are frequently confused.

Include a table similar to:

| Concept   | Purpose                             |
| --------- | ----------------------------------- |
| Dimension | What aspect of quality is evaluated |
| Metric    | How quality is measured             |
| Check     | How quality is verified             |
| Signal    | Evidence of behavior                |
| Incident  | Quality failure event               |
| SLA       | Quality objective                   |

Explain why separating these concepts improves architecture design.

## Required Architectural Diagram

Describe a conceptual diagram that contains:

```text
Data Quality
│
├── Core Dimensions
│
├── Structural Extensions
│
├── Runtime Extensions
│
├── Semantic Extensions
│
├── Governance Extensions
│
└── AI Extensions
```

The diagram should be explained in prose rather than rendered as ASCII art.

## Writing Style

Requirements:

- Technical but accessible
- Vendor-neutral
- Architecture-oriented
- Evidence-based
- Practical rather than academic

Avoid:

- marketing language
- product promotion
- exaggerated claims
- "best practices" lists without rationale

## Desired Length

Approximately 2,500–4,000 words.

The article should be readable within 10–15 minutes.

## Desired Outcome

Readers should leave with:

1. A clear understanding of the major industry data quality frameworks.
2. A practical mental model for organizing quality dimensions.
3. A way to distinguish intrinsic data quality from runtime, governance, and AI concerns.
4. A blueprint for designing future metadata-driven data quality systems.
