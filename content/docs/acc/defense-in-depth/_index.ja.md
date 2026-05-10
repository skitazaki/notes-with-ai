+++
date = '2026-05-10T13:10:00+09:00'
title = '多層防御アーキテクチャ'
weight = 7
prev = '/docs/acc/ai-agents'
next = '/docs/acc/governance'
+++

アクセス制御は、identity と authorization を取り巻く追加制御によって、誤設定・誤用・侵害の影響を抑えられるときに最も強くなります。

## Executive Summary

Defense in depth は、単一の制御では十分でないことを認める考え方です。認証はフィッシングされ得ますし、ポリシーは誤設定され得ます。トークンは盗まれ、ワークロードは侵害され、運用者は誤承認することもあります。多層防御は、攻撃者に複数の control domain を越えさせることで blast radius を下げます。

アクセス制御の文脈では、強い認証、device trust、network segmentation、conditional access、runtime authorization、行動分析、ログ、incident response が主な層になります。

## Core Concepts

### 多層の enforcement

高リスク要求は、しばしば次の複数ゲートを通ります。

1. identity proofing と MFA
2. device / workload trust 評価
3. network と session policy
4. 要求された action に対する authorization policy
5. anomaly detection と transaction monitoring
6. logging、alerting、containment control

各層は別々の問いに答えます。これらを組み合わせることで、認可だけに過剰な責務を背負わせずに済みます。

### Fail-open と fail-closed

重要システムでは、依存先が使えないときにどう振る舞うかを決める必要があります。fail-closed は安全性を高めますが可用性を損なう可能性があります。fail-open は継続性を守りますが重大な露出を生み得ます。正解は、事業重要度、安全性への影響、補完制御によって変わります。

### Break-glass access

緊急アクセスは現実の運用に必要ですが、例外でなければなりません。break-glass 経路には、明確な scope、時間制限、強いログ、事後レビュー、可能なら out-of-band 承認が必要です。

## Implementation and Operations

### 実務的な制御スタック

- 強い認証とフィッシング耐性 MFA
- device posture または workload attestation
- user、service、administrative path の分離
- application / API 層での文脈依存認可
- sandboxing や egress control などの runtime containment
- SIEM 連携と対応 playbook

### 監視すべきこと

- 異常な権限昇格や token 発行
- policy bypass の試み
- human identity に対する不自然な移動や地域変化
- 通常と異なる service-to-service 呼び出し経路
- denied action が続いた直後の privileged action 成功

Defense in depth が有効になるのは、アラートを identity、policy、回復アクションへ結び付けられる場合だけです。
