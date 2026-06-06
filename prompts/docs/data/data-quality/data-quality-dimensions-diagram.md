# The Conceptual Diagram

The model can be visualized as a single data quality domain with a stable center and several surrounding extension layers.

At the top level sits Data Quality as the overall concern. Directly beneath it is Core Dimensions, containing accuracy, completeness, consistency, timeliness, uniqueness, and validity. This is the smallest common model that most organizations can apply to nearly every dataset.

Around that core sit five extensions.

Structural Extensions capture schema and relationship quality where formal structure exists.
Runtime Extensions capture operational signals produced by pipelines, monitoring, and observability systems.
Semantic Extensions capture whether data is understandable and usable for consumers.
Governance Extensions capture whether data is controlled, traceable, and compliant.
AI Extensions capture whether data is fit for statistical learning and model operation.

The diagram is not meant to suggest a strict processing order. It expresses an architectural dependency. Organizations should stabilize the core first, then attach the extension layers according to their platform design, metadata maturity, regulatory requirements, and AI usage.
