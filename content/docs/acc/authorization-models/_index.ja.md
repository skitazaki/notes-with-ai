+++
date = '2026-05-10T12:40:00+09:00'
title = '認可モデルとポリシーシステム'
weight = 4
prev = '/docs/acc/human-identity'
next = '/docs/acc/workload-identity'
+++

認可は、認証済み principal が、特定の文脈において、特定の resource に対して、特定の action を実行できるかを判断する仕組みです。

## Executive Summary

あらゆる環境に万能な認可モデルはありません。実務上の課題は、組織の意味論を、スケーラビリティ、監査可能性、開発者体験を損なわずに enforcement 可能な判断へ写像することです。

DAC や MAC のような古典的モデルも概念上は重要ですが、現代の企業システムでは RBAC、ABAC、ReBAC、policy-as-code の組み合わせが中心になります。最も堅牢な構成は、安定した粗粒度ロール、実行時の文脈評価、そして高感度または共有基盤向けの明示的なポリシーエンジンを重ねる形です。

## Core Concepts

### 各モデルの概要

- **DAC**: リソース所有者が権限を付与する。協調型システムには向くが、中央統制には弱い
- **MAC**: ラベルとクリアランスを中央で強制する。規制環境では強いが、変化の速い業務には硬直的
- **RBAC**: 権限を role に、role を principal に割り当てる。説明しやすいが role explosion が起きやすい
- **ABAC**: subject、resource、action、environment の属性を用いて判断する。柔軟だが policy sprawl の危険がある
- **ReBAC**: owner、viewer、approver、team member などの関係グラフで判断する。協調型・マルチテナント製品に強い
- **PBAC**: ポリシーロジックを専用システムや言語に切り出し、アプリコードから独立して評価する

### RBAC と ABAC の比較

RBAC は、責務が安定している場合に運用しやすい反面、例外のたびにロールを増やすと急速に脆くなります。ABAC は、地域、デバイス状態、取引金額、テナント分類、時間帯のような動的条件に対応できますが、属性とポリシーが増えるほど追跡と監査が難しくなります。

本質的な差は、静的か動的かではなく、管理の単純さと判断精度のどちらに寄せるかです。

### ポリシーエンジンと評価フロー

現代のポリシーシステムは、しばしば次を分離します。

1. **Policy authoring**
2. **Policy distribution**
3. **Decision evaluation**
4. **Enforcement**
5. **Decision logging and explanation**

OPA、Cedar、Zanzibar 由来のグラフ型システム、XACML 系エンジンは、構文や配置形態は異なっても、同じ論点に直面します。すなわち latency、caching、consistency、policy rollout の安全性、explainability です。

## Implementation and Operations

### 実務上の指針

- 安定した基礎権限には RBAC を使う
- 新しい恒久ロールを作るべきでない実行時条件には ABAC を重ねる
- 共有、委譲、協調グラフには ReBAC を使う
- ポリシーコードはアプリコードと同様にバージョン管理し、テストし、レビューする
- リスクが高い領域では、競合解決のために明示的な deny 意味論を設計する

### スケーリング上の難所

大規模化すると難しいのは構文ではありません。データ鮮度、キャッシュ無効化、関係グラフの整合性、そして似たリクエストに異なる判断が出た理由を説明することです。

成熟度の良い指標は、認可ロジックをデプロイ前にテストできるか、インシデント分析時に過去の判断を再生できるかです。
