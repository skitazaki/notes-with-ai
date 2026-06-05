---
type: docs
path: /docs/data/management/
---

Revise `content/docs/data/management/_index.md` so the `Data Quality Management` section defines a stable core model for data quality dimensions.

Writer role:

- You are a senior data architect and technical writer.

Primary objective:

- Define the core data quality dimensions for the Data Management page using the industry-standard core six.
- Explicitly include **Uniqueness** as a core dimension, not as an optional extension.
- Keep the treatment concise, concept-first, and aligned with the tone of the existing page.

Required outcome for the target page:

- The `Data Quality Management` section must name these six core dimensions: **Accuracy, Completeness, Consistency, Timeliness, Validity, and Uniqueness**.
- Briefly explain **Uniqueness** as control of unintended duplicates in records or entities.
- Present **Integrity**, **Reliability**, **Relevance**, observability metrics, and AI-specific concerns as adjacent or extended concerns rather than part of the universal core.
- Preserve the page's neutral explanatory style and avoid turning the section into a tooling guide.

Constraints:

- Do not reduce the core model to five dimensions.
- Do not replace **Uniqueness** with only implementation terms such as deduplication or key constraints without first naming it as a dimension.
- Do not expand the Data Management page into a full taxonomy of every possible quality attribute.

Japanese terminology guidance:

- In Japanese output, avoid translating `dimensions` as `次元`.
- Prefer `品質観点` when describing the core set or a perspective for evaluating quality.
- Prefer `品質特性` when referring to adjacent or extended quality properties.
