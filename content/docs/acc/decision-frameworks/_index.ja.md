+++
date = '2026-05-10T13:50:00+09:00'
title = '意思決定フレームワークとトレードオフ'
weight = 11
prev = '/docs/acc/threat-models'
next = '/docs/acc/reference-architectures'
+++

良いアクセス制御設計は、普遍的な正解よりも、明示的なトレードオフ管理に依存します。

## Executive Summary

RBAC と ABAC、JWT と opaque token、centralized と decentralized authorization、長寿命資格情報と ephemeral credential のような選択は、それぞれ異なる運用現実を最適化します。機能比較だけで判断すると誤りやすく、実際には scalability、failure mode、governance cost、migration burden、trust boundary の形を含めて比較する必要があります。

## Core Concepts

### 典型的な比較軸

- **RBAC vs ABAC**: 安定運用と動的精度
- **Centralized vs decentralized authorization**: 一貫性とローカル自律性
- **JWT vs opaque tokens**: ローカル検証とサーバー側の強い失効制御
- **Static vs continuous authorization**: 低い実行コストと変化するリスクへの追従
- **Long-lived vs ephemeral credentials**: 運用容易性と封じ込め・属性把握

### 先に問うべきこと

1. 監査人、運用者、開発者に何を説明しなければならないか
2. 判断時点で鮮度が必要なデータは何か
3. 許容できる失敗は何か: latency、inconsistency、availability 低下のどれか
4. policy semantics と rollout safety は誰が持つか
5. 最初のモデルが足りなかった場合の migration はどれほど困難か

## Implementation and Operations

### 判断のヒューリスティクス

- trust boundary に合う範囲で最も単純なモデルを優先する
- 実行時に本当にリスクが変わる場合にだけ動的性を追加する
- semantic drift を許容できないなら policy logic を全チームに分散しない
- 既存 RBAC の周囲に文脈条件を足すなど、可逆的な移行経路を優先する
- 理論上の表現力ではなく運用コストを測る

トレードオフ文書が有用なのは、設計意図を保存できるからです。なぜその選択をしたのかが残っていれば、場当たり的な例外でアーキテクチャが崩れにくくなります。
