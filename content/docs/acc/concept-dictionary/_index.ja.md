+++
date = '2026-05-10T14:10:00+09:00'
title = 'コンセプト辞書'
weight = 13
prev = '/docs/acc/reference-architectures'
+++

アクセス制御アーキテクチャでは、言葉の小さな違いが trust assumption の大きな違いを隠すため、共通語彙が不可欠です。

## Executive Summary

本辞書は、ライブラリ全体で使う主要用語を定義し、policy、engineering、platform、governance の各チームが曖昧さなく同じ概念を議論できるようにするものです。

## Core Concepts

### Principal

アクションを要求または実行する主体。人間の利用者、サービス、ワークロード、デバイス、AI エージェントが含まれます。

### Identity

ある trust domain において principal を表す、主張され検証された表現。1 つの principal が複数システムで複数の identity を持つことがあります。

### Subject

ポリシー判断の対象となる主体。多くのシステムでは subject と principal は実質同じですが、委譲された操作では区別が重要です。

### Resource

アクセス対象となるオブジェクト、サービス、データセット、エンドポイント、または capability。

### Entitlement

何らかの action を可能にする、付与済みの permission、role、または capability。

### Capability

特定の操作を行うための境界付き権限。委譲、scope 制限、時間制限を伴う設計と相性が良い概念です。

### Delegation

ある principal や policy domain の代わりに行動できる限定権限を、別の principal に与える行為。

### Policy

アクセスを許可、拒否、制約、または昇格要求するかを決める形式的なルール集合。

### Scope

credential、permission、delegated authority が有効な範囲。

### Trust boundary

identity、制御、データ取り扱いに関する前提を再評価すべき境界。

### Workload identity

実行中のサービス、ジョブ、コンテナ、関数、デバイスに対する、機械的に検証可能な identity。

### Agent

ある程度の自律性を持って計画と実行を行い、しばしば tools、memory、delegated permissions を利用するソフトウェアシステム。

## Implementation and Operations

用語は、policy code、audit record、architecture diagram、review process で標準化されるべきです。同じ言葉が違う意味で使われると、制御の失敗につながりやすくなります。
