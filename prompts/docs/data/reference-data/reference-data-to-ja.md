---
type: docs
path: /docs/data/management/reference-data
---

# 日本語の翻訳版の作成

あなたはデータ管理の専門家であり、公開技術ドキュメントを作成するプロフェッショナルです。正確性を損なわず、自然で読みやすい日本語版を作成してください。

翻訳対象のファイルは次のパスにあります。

`content/docs/data/management/reference-data/_index.md`

日本語版は、同じフォルダの `_index.ja.md` に保存してください。文書構造とメタデータを保持し、文末はです・ます調で統一してください。

翻訳方針：

- Reference Data Management -> 参照データ管理
- reference data -> 参照データ
- master data -> マスタデータ
- controlled vocabulary -> 統制語彙
- code set -> コードセット
- crosswalk -> クロスウォーク
- mapping -> マッピング
- effective dating -> 有効期間の管理
- stewardship -> スチュワードシップ
- consuming system -> 利用システム
- shared identity -> 共有アイデンティティ
- shared vocabulary -> 共有語彙
- shared context and meaning -> 共有された文脈と意味

コード値、属性名、JSON、SQL、API、MDM、SCD Type 2 などの識別子や略語は、意味が変わらないよう原文を維持してください。特に `Status = Active`、`State Code = A`、`is_status = 1`、`JPN-YEN-LIVE` の表記を変更しないでください。

日本語文中のインライン Markdown リンクの前後には半角スペースを入れてください。画像は日本語版の `reference-data-across-systems.ja.webp` を参照し、画像タイトルと代替テキストも日本語化してください。

直訳調やマーケティング表現を避け、英語版と同程度の文量で、概念の境界が明確な公開ドキュメントにしてください。
