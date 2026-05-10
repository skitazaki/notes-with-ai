+++
date = '2026-05-10T12:30:00+09:00'
title = '人のアイデンティティとエンタープライズ IAM'
weight = 3
prev = '/docs/acc/landscape'
next = '/docs/acc/authorization-models'
+++

人のアイデンティティは、説明責任、承認、法的義務が最終的には人に紐づくため、依然としてエンタープライズアクセス制御の基盤です。

## Executive Summary

Enterprise IAM は、従業員や外部利用者の identity を、入社・登録から離脱まで管理します。設計課題は、従業員、契約社員、パートナー、ベンダー、顧客それぞれに必要な proofing、federation、review、privilege control をどう両立するかです。

成熟した IAM は、ログイン体験だけでなく lifecycle integrity に焦点を当てます。重大な失敗は、弱い認証だけではありません。古い権限、孤立アカウント、壊れた joiner-mover-leaver、過度な delegated administration、統制を迂回する特権アクセスが主な問題です。

## Core Concepts

### ライフサイクル管理

人のアクセスは、本人確認と、HR やパートナー台帳、顧客登録システムのような authoritative source から始まります。プロビジョニングは、これらのソースに追随すべきであり、独立した手作業であってはなりません。

主なライフサイクルは次の 3 つです。

- **Joiners**: アカウント作成、ベースロール付与、MFA 登録、デバイス登録
- **Movers**: チーム、地域、法人、責務変更に応じた権限更新
- **Leavers**: セッション失効、アカウント停止、共有資格情報のローテーション、所有権移管

### フェデレーションと利用体験

SSO、SAML、OpenID Connect、SCIM、ディレクトリ同期は、trust boundary を明確にした上で設計すれば運用の分散を抑えられます。フェデレーションの価値は、強いセッション制御、MFA、conditional access、risk-based step-up と組み合わせたときに最大化します。

### ガバナンスと特権アクセス

すべての権限を通常のロール割当で与えるべきではありません。高感度の capability には、次のような仕組みが必要です。

- 職務分掌の制約
- 承認ワークフロー
- 時間制限付きの権限昇格
- セッション録画やコマンドログ
- 定期的なアクセス認証

PAM は、identity、approval、runtime monitoring の接点にあります。単独の vault 製品として切り離して扱うべきではありません。

## Implementation and Operations

### 設計パターン

- ライフサイクルトリガーは authoritative system に寄せる
- ロール設計は個別例外ではなく職務単位で安定化する
- 高感度システムでは JIT provisioning / JIT elevation を優先する
- delegated administration は scope を限定し、監査可能かつ取り消し可能にする
- アクセスレビューはカレンダーよりリスクに基づいて設計する

### 典型的なアンチパターン

- 表計算ベースの手動プロビジョニング
- 運用都合で恒久的な administrator ロールを付与する
- 有効権限の把握が困難になるほど深いグループネスト
- 通常の offboarding 制御の外側で管理される contractor identity
- 明確な境界なしに customer identity と workforce identity を混在させる

目標は無条件に摩擦を減らすことではありません。事業上の説明責任に根ざした、迅速で説明可能かつ剥奪可能なアクセスを実現することです。
