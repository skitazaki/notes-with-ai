+++
date = '2026-05-10T13:30:00+09:00'
title = 'アーキテクチャパターン集'
weight = 9
prev = '/docs/acc/governance'
next = '/docs/acc/threat-models'
+++

アーキテクチャパターンは、繰り返し現れる enforcement と trust distribution の問題に対する再利用可能な答えです。

## Executive Summary

パターンが重要なのは、アクセス制御が個別アルゴリズムの品質よりも、統合点で失敗しやすいからです。再利用可能なパターンは、policy がどこにあり、判断がどう伝播し、どこで trust assumption が危険になるかを整理する助けになります。

## Core Concepts

### Centralized authorization

中央の policy service が多数のアプリケーションの判断を行います。一貫性とガバナンスは強まりますが、latency、availability、policy distribution が論点になります。

### Embedded authorization

アプリケーションがプロセス内でポリシーを評価します。自律性とローカル耐障害性は高まりますが、意味論が標準化されていないと policy drift を招きます。

### Sidecar / service mesh enforcement

プロキシや sidecar が workload の近くで identity と粗粒度ポリシーを強制します。service-to-service 制御、mTLS、統一テレメトリには有効ですが、業務固有の認可は依然としてアプリ内ロジックが必要になりやすいです。

### API gateway enforcement

ゲートウェイは、認証、トークン検証、tenant routing、粗い rate control、広域 API policy に向きます。ただし高感度な業務認可をそこだけに押し込むべきではありません。

### Multi-tenant / B2B federation パターン

共有プラットフォームでは、tenant isolation、delegated administration、外部 identity federation、partner ごとの policy overlay が必要です。この領域では ReBAC と scoped delegation が重要になります。

## Implementation and Operations

### パターン選択の基準

- latency 許容度
- consistency 要件
- team autonomy モデル
- auditability / explainability の要求
- trust boundary の位置
- policy rollout / rollback を運用できる成熟度

### 実務的な推奨

大規模システムの多くは最終的にハイブリッドになります。中央で policy semantics を定義し、enforcement は分散し、業務不変条件はアプリが確認します。重要なのは純粋性ではなく、責任分界を明示することです。
