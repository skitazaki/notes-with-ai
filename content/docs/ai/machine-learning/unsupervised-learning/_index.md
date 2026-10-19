---
date: "2026-10-19T09:00:00+09:00"
title: "Unsupervised Learning"
weight: 2
prev: "/docs/ai/machine-learning/supervised-learning"
next: "/docs/ai/machine-learning/self-supervised-learning"
---

Unsupervised learning studies data without an explicit target label for each example. Instead of learning a specified input-to-answer mapping, a method searches for structure that may help describe, organize, or simplify the data. The result is a candidate representation or pattern; people still need to decide whether it is useful for a particular purpose.

## Common tasks

Clustering groups examples according to similarity under a chosen representation and distance measure. K-means, hierarchical clustering, and density-based methods such as DBSCAN illustrate different assumptions about group shape and density. A cluster is not automatically a naturally occurring or meaningful category.

Dimensionality reduction creates a lower-dimensional representation while preserving selected properties of the data. Principal component analysis captures directions of high variance using linear combinations; nonlinear approaches can preserve neighborhood structure or learn useful embeddings. Reduced representations support visualization, compression, or later modeling, but a two-dimensional plot can distort relationships in the original data.

Density estimation models which regions of the input space are common. Anomaly detection uses deviations from those patterns to identify observations for review. Topic modeling and exploratory segmentation seek recurring themes or groups in collections such as documents or customer records. These tasks overlap in practice and may use methods from statistics, information retrieval, and deep learning.

## Use cases

Unsupervised methods can help analysts explore unfamiliar data, identify duplicate or related documents, summarize customer behavior, detect unusual sensor readings, or create representations for search and downstream prediction. They are particularly useful when no agreed target exists or when the goal is to form hypotheses for further investigation.

The output depends on choices such as features, scaling, distance, number of clusters, and algorithm. Different reasonable choices can reveal different structures. Human interpretation and domain context help determine whether a discovered pattern is actionable rather than an artifact of the representation.

## Evaluation and limitations

Without target labels, evaluation is less direct than in supervised learning. Internal measures can show compactness or separation under an algorithm's own assumptions, but a strong score does not establish practical value. Analysts can check stability across samples and settings, inspect representative examples, compare with domain knowledge, and test whether the structure supports a downstream decision.

Anomaly scores are not explanations or proof of error; rare observations may be valid and important. Likewise, clusters can reflect data collection choices or historical bias. When results affect people or operations, validate the interpretation with relevant stakeholders and use the method as one source of evidence.

## Relationship to other paradigms

Self-supervised learning also uses data without human-assigned labels, but it constructs explicit prediction targets from the inputs. Unsupervised learning is the broader family of methods that discover or represent structure without externally specified targets. In applied systems, unsupervised exploration may precede supervised model development, or learned representations may be used as inputs to a later task.

## Summary

Unsupervised learning helps reveal and represent structure when explicit labels are absent. Its outputs are hypotheses that require interpretation and task-aware validation before they guide decisions.
