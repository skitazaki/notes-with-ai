+++
date = '2026-05-10T12:20:00+09:00'
title = 'ランドスケープ概要'
weight = 2
prev = '/docs/acc/vision'
next = '/docs/acc/human-identity'
+++

アクセス制御の世界は、単一製品の比較ではなく、相互に連携するシステム群として理解するのが適切です。

## Executive Summary

現代のアーキテクチャでは、少なくとも本人確認、認証、認可、資格情報発行、enforcement point、テレメトリ、ガバナンス、復旧手順が必要です。企業ではこれらを、IdP、ディレクトリ、フェデレーションブローカー、ポリシーエンジン、PAM、シークレット管理、証明書基盤、ワークロード ID、API ゲートウェイ、SIEM など複数の仕組みで構成します。

本質的な設計課題は、単一制御の選定ではありません。これらのシステムをどう協調させ、矛盾した判断や運用上の空白を生まないかです。

## Core Concepts

### 主な制御ドメイン

- **Identity providers / directories**: principal が誰かを確立する
- **Federation systems**: 異なる trust domain 間で主張を受け入れる
- **Authentication factors**: 主張された identity の確度を高める
- **Authorization systems**: 要求された操作を許可するか判断する
- **Credential systems**: トークン、証明書、鍵を発行する
- **Enforcement points**: アプリ、ゲートウェイ、サイドカー、インフラ境界で判断を適用する
- **Governance systems**: 権限をレビュー、認証、剥奪する
- **Observability systems**: 判定を記録し、不正利用を検知する

### 認可モデルの分類

各モデルは異なる環境に向きます。

- **DAC**: 所有者裁量と単純さ
- **MAC**: 中央集権的な分類管理と厳格な階層
- **RBAC**: 職務単位の安定した権限割当
- **ABAC**: 文脈依存で動的な判断
- **ReBAC**: グラフ型の共有・協業モデル
- **PBAC**: 分離されたポリシー記述とプログラム可能な統制

これらは相互排他的ではありません。1 つのシステムが、粗い権限管理に RBAC、実行時条件に ABAC、共有意味論に ReBAC を使うこともあります。

### なぜ景観が拡大し続けるのか

複雑化の主因は 2 つあります。1 つは、分散システムにより human identity より machine identity の方が急増していること。もう 1 つは、AI 支援やイベント駆動ワークフローにより、ログイン中の人間が直接始めたわけではないリクエストが増えていることです。そのため対象は workforce IAM から trust orchestration 全体へ広がります。

## Implementation and Operations

### 実務的な見取り図

4 層で考えると整理しやすくなります。

1. **Identity layer**: proofing、lifecycle、authentication、federation
2. **Decision layer**: policies、roles、attributes、relationships、risk signals
3. **Enforcement layer**: application、gateway、mesh、database、SaaS、runtime
4. **Governance layer**: review、audit、testing、exception handling、incident response

### 典型的な統合ミス

- トークン発行を認可そのものとみなす
- 強い認証が自動的にリソース権限を意味すると考える
- ポリシー意味論は中央化したのに例外処理を文書化しない
- enterprise trust model の外側で machine identity を組み立てる
- 委譲と承認境界を定義せずに AI エージェントを追加する

本ライブラリの以降の文書では、これらの領域を個別に掘り下げます。
