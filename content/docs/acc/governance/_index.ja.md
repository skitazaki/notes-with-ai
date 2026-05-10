+++
date = '2026-05-10T13:20:00+09:00'
title = 'ガバナンス、コンプライアンス、監査可能性'
weight = 8
prev = '/docs/acc/defense-in-depth'
next = '/docs/acc/patterns'
+++

アクセス制御が組織規模で信頼できるものになるのは、権限、ポリシー、例外が時間を通じて governable、explainable、reviewable である場合だけです。

## Executive Summary

ガバナンスは、技術的な認可と組織的な説明責任を接続する規律です。誰がアクセスを承認できるのか、権限レビューをどう行うのか、ポリシー変更をどうテストするのか、監査人、規制当局、顧客、内部統制部門にどのような証跡を示すのかを扱います。

SOC 2、ISO 27001、HIPAA、PCI DSS、GDPR などのフレームワークは 1 つのアーキテクチャを強制しませんが、アクセス、least privilege、証跡、インシデント対応を実証できることを求めます。

## Core Concepts

### Entitlement governance

権限には owner、purpose、review path、revocation path が必要です。所有者不明の entitlement は蓄積し、やがてレビュー不能になります。

強いガバナンスには通常、次が含まれます。

- access request と approval workflow
- 定期的な access certification
- segregation-of-duties ルール
- policy exception handling
- privileged access review

### Auditability と explainability

イベントだけを記録するログでは不十分です。実効的な auditability には、次を再構成できる必要があります。

- どの principal が行動したか
- どの resource と action が対象だったか
- どの policy または approval が許可したか
- どの文脈が判断に影響したか
- その後に何が変化したか

### Policy testing と evidence

ポリシー変更は、ロールアウト前にテスト可能であるべきです。証跡は監査時に手作業で寄せ集めるのではなく、通常運用の副産物として生成されるべきです。

## Implementation and Operations

### 運用モデル

- 必要に応じて policy owner と entitlement owner を分ける
- システムと権限を criticality で分類する
- review frequency は risk に基づいて決める
- 規制が必要とする場合は immutable または tamper-evident な decision record を保持する
- 規制対応を設計の唯一の目的にせず、control と義務を対応付ける

### 典型的な失敗モード

- スクリーンショットとメールに依存した監査
- simulation や regression check なしの policy 変更
- 一時例外の仕組みがないため恒久化する例外
- business approver と technical implementer の区別がない
- ログは存在するがシステム間で相関できない

良いガバナンスは監査の負担だけでなく、アクセス関連インシデントの理解と封じ込めに要する時間も減らします。
