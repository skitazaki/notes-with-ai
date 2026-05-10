+++
date = '2026-05-10T12:50:00+09:00'
title = 'ワークロードとマシン ID'
weight = 5
prev = '/docs/acc/authorization-models'
next = '/docs/acc/ai-agents'
+++

マシン ID は、現代のシステムに人間の運用者よりもはるかに多くのサービス、ワークロード、パイプライン、デバイスが存在するため、アクセス制御アーキテクチャの中でも急速に重要性を増している領域です。

## Executive Summary

Workload identity は、「あるマシンが別のマシンを何者として認識し、どの条件で信頼するか」という根本問題に答えます。従来は静的シークレットや長寿命サービスアカウントに依存しがちでしたが、現代では attestation、短命資格情報、証明書ベース identity、厳密に絞られた service-to-service authorization が中心になります。

この領域は、Kubernetes、serverless、CI/CD、API、service mesh、ロボティックオートメーション、IoT にまたがります。課題はワークロードを認証することだけではありません。その実行役割に必要最小限の identity と capability を与えることです。

## Core Concepts

### 主な identity 形態

マシン ID は主に次の形で現れます。

- service account や cloud role
- X.509 証明書と mTLS identity
- workload federation 用の OIDC / OAuth token
- 署名付き workload attestation
- ハードウェアに根差した device identity

### なぜ静的シークレットは破綻しやすいか

長寿命の共有シークレットは、blast radius を広げ、属性把握を弱くし、ローテーションを困難にします。複数サービスが同じ資格情報を提示するため、どの workload が動いたのかも曖昧になります。

attestation、rotation、workload metadata に結び付いた policy check を伴う自動発行の短命資格情報は、封じ込めと可観測性を改善します。

### SPIFFE / SPIRE と workload trust

SPIFFE / SPIRE のような枠組みは、標準化された識別子と発行フローで workload identity を定式化します。価値は相互運用性だけではありません。identity を検証可能な workload context に明示的に束ねることにあります。

## Implementation and Operations

### 推奨パターン

- クラウドが対応しているなら federated workload identity を使う
- 広すぎる service account を狭い runtime identity に置き換える
- pod、namespace、cluster、image signature、build provenance などの証拠に identity を結び付ける
- workload の認証と、その action の認可を分離する
- 資格情報は自動ローテーションし、発行異常を監視する

### 高リスク領域

- 広い本番権限を持つ CI/CD システム
- 複数業務で使い回される共有 robot / batch identity
- 期限切れしない API token
- 過剰権限 workload にマウントされた Kubernetes service account
- revocation や attestation を持たない device fleet

運用上の目標は、machine trust を secret 配布の問題から、identity と policy の問題へ変えることです。
