---
date: "2026-10-19T09:00:00+09:00"
title: "Supervised Learning"
weight: 2
prev: "/docs/ai/machine-learning/learning-paradigms"
next: "/docs/ai/machine-learning/unsupervised-learning"
---

Within this documentation, a domain is the broader subject area, and a topic page is the more focused explanation of a concept, pattern, or operating concern within it. This page belongs to that broader domain and connects the related topic pages.

Supervised learning trains a model from examples that pair inputs with known targets. The model learns a mapping that can be applied to new inputs. Targets may be categories, numbers, rankings, or structured outputs, depending on the task.

## Classification and regression

Classification predicts a discrete category, such as whether a transaction is suspicious or which topic a document covers. Regression predicts a numeric quantity, such as delivery time or expected demand. The distinction comes from the target being predicted, not necessarily from the algorithm: some model families support both types of task.

Common methods include linear and logistic regression, decision trees, random forests, gradient-boosted trees, support vector machines, nearest-neighbor methods, and neural networks. These methods make different assumptions about data and tradeoffs in accuracy, interpretability, data requirements, and inference cost. There is no universally best method.

## Labels and learning objectives

Labels may be supplied by experts, derived from an existing process, measured by instruments, or observed later as an outcome. In each case, the label is an operational definition of what the model is asked to predict. For example, a fraud model trained on previously confirmed cases learns the historical confirmation process as well as any underlying fraud pattern.

The training objective specifies how model predictions are compared with targets and how errors contribute to learning. A useful objective should reflect the intended task, while evaluation should separately measure the errors that matter in use. Optimizing average accuracy may be inappropriate when classes are imbalanced or false negatives and false positives have very different costs.

## Data quality and evaluation

Training examples should represent the situations in which predictions will be used. Inconsistent labels teach inconsistent behavior; unrepresentative samples can produce gaps across populations or time periods. Data leakage occurs when training or evaluation includes information that would not be available at prediction time, creating an overly optimistic estimate.

Training data is used to fit parameters. Validation data supports model and configuration choices. A held-out test set estimates performance after those choices are complete. For time-dependent or grouped data, splits should respect chronology or group boundaries so related examples do not leak across sets. Evaluation should include appropriate metrics, error analysis, and checks on important subgroups.

## Applications and limits

Supervised learning is common in document and image classification, demand forecasting, quality inspection, risk scoring, and ranking. It is most straightforward when reliable examples and relevant outcomes are available. Label cost, delayed outcomes, changing definitions, and historical bias can limit its usefulness.

A model estimates patterns represented in its training experience; it does not establish causality simply by predicting well. Changes in input data or the relationship between inputs and outcomes can reduce performance. Monitoring and periodic reassessment are therefore part of a responsible supervised system.

## Summary

Supervised learning uses labeled examples to learn predictions for new cases. Its success depends on meaningful targets, representative data, evaluation that matches the intended use, and attention to how errors and data change over time.
