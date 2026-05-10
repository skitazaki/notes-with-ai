+++
date = '2026-05-10T13:40:00+09:00'
title = '脅威モデル集'
weight = 10
prev = '/docs/acc/patterns'
next = '/docs/acc/decision-frameworks'
+++

脅威モデルは、一般論の不安を、具体的な attack path、trust boundary 分析、緩和策の選択へ落とし込むための道具です。

## Executive Summary

アクセス制御の失敗は単一バグとして現れることは稀です。多くは連鎖です。たとえば stale permission と弱い review、token theft と segmentation 不足、prompt injection と広すぎる tool access、service-account sprawl と attribution 不足の組み合わせです。脅威カタログは、インシデント前にこれらを議論する共通言語を提供します。

## Core Concepts

### 代表的な脅威カテゴリ

- **Privilege escalation**: 誤設定、ロール継承、欠陥のある policy evaluation による昇格
- **Token / credential theft**: エンドポイント、ワークロード、CI/CD、ログからの窃取
- **Lateral movement**: 広すぎる service trust や共有資格情報を使った横展開
- **Orphaned accounts**: 所有者消失後も残るアカウント
- **Shadow administration**: 間接権限や統制外サポートツールによる隠れた管理権限
- **Confused deputy**: 信頼されたサービスが他者の意図で権限を誤用する
- **Prompt injection**: エージェントの tool 利用やデータ解釈に影響する入力
- **Policy bypass**: 文書化されていない例外経路や層ごとの enforcement 不一致

### 脅威モデルの構造

各脅威について、少なくとも次を整理します。

1. 攻撃者の前提条件
2. 越えられる trust boundary
3. 危険に晒される asset
4. 検知機会
5. 予防的制御と補完的制御

## Implementation and Operations

### 緩和策の例

- stale permission -> lifecycle automation、access review、ownership mapping
- token theft -> 短命資格情報、device binding、vault hygiene、anomaly detection
- lateral movement -> segmentation、least privilege、service identity separation
- prompt injection -> tool allowlist、content isolation、approval gate、output filtering
- policy bypass -> 統一された policy semantics、negative testing、一貫した logging

脅威モデルが最も有効なのは、静的なコンプライアンス資料として保存されるときではなく、アーキテクチャレビュー、制御テスト、事後学習に結び付いているときです。
