+++
date = '2026-05-10T12:00:00+09:00'
title = 'アクセス制御'
weight = 2
+++

アクセス制御は、誰または何が、どの条件で、どの程度の保証を伴って、どの操作を実行できるかを定義するアーキテクチャ上の中核領域です。
現代のシステムでは、この問いは従業員や顧客だけでなく、ワークロード、API、外部サービス、AI エージェント、そしてクラウドとオンプレミスをまたぐ信頼境界全体に広がります。

本セクションは、単一の長文レポートではなく、セキュリティアーキテクチャのライブラリとして構成しています。
基本原則、技術ドメイン、運用統制、再利用可能な参照資料を分離し、戦略から実装までを一貫した概念モデルのまま辿れるようにしています。

推奨する読書順は次のとおりです。

1. ビジョンと原則
2. ランドスケープと分類体系
3. 人のアイデンティティ、認可モデル、ワークロード ID、AI エージェント制御
4. 多層防御とガバナンス
5. パターン、脅威モデル、設計トレードオフ、参照アーキテクチャ

各ドキュメントは共通して次の 3 層で構成します。

- **Executive Summary**: 全体像の把握
- **Core Concepts**: 概念モデルの理解
- **Implementation and Operations**: 実装・運用上の論点

<!-- deno-fmt-ignore-start -->

{{< cards >}}
{{< card link="vision/" title="ビジョンと原則" icon="sparkles" subtitle="アイデンティティ中心のセキュリティを支える北極星" >}}
{{< card link="landscape/" title="ランドスケープ概要" icon="document-text" subtitle="アクセス制御の全体像と分類" >}}
{{< card link="human-identity/" title="人のアイデンティティとエンタープライズ IAM" icon="users" subtitle="ライフサイクル、連携、PAM、統制" >}}
{{< card link="authorization-models/" title="認可モデルとポリシーシステム" icon="shield-check" subtitle="DAC、MAC、RBAC、ABAC、ReBAC、PBAC とポリシー評価" >}}
{{< card link="workload-identity/" title="ワークロードとマシン ID" icon="document-text" subtitle="分散システムにおけるマシン間信頼" >}}
{{< card link="ai-agents/" title="AI エージェントと自律的認可" icon="document-text" subtitle="エージェント ID、制約付き実行、承認境界" >}}
{{< card link="defense-in-depth/" title="多層防御アーキテクチャ" icon="document-text" subtitle="ID、ネットワーク、ランタイム、可観測性をまたぐ防御" >}}
{{< card link="governance/" title="ガバナンス、コンプライアンス、監査可能性" icon="document-text" subtitle="証跡、説明可能性、権限統制、規制対応" >}}
{{< card link="patterns/" title="アーキテクチャパターン集" icon="document-text" subtitle="再利用可能な enforcement / 配置パターン" >}}
{{< card link="threat-models/" title="脅威モデル集" icon="document-text" subtitle="典型的な攻撃経路、失敗モード、緩和策" >}}
{{< card link="decision-frameworks/" title="意思決定フレームワークとトレードオフ" icon="scale" subtitle="設計選択を整理するための比較軸" >}}
{{< card link="reference-architectures/" title="参照アーキテクチャ" icon="document-text" subtitle="全体像を掴むための代表構成" >}}
{{< card link="concept-dictionary/" title="コンセプト辞書" icon="book-open" subtitle="principal、policy、scope、trust boundary などの共通語彙" >}}
{{< /cards >}}

<!-- deno-fmt-ignore-end -->
