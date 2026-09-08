---
type: image
path: /ja/docs/data/collection
---

# 画像ローカライズプロンプト — ソース側の境界

英語版 `content/docs/data/collection/source-side-boundary.webp` を編集対象として使用し、文字だけを日本語へ置き換えた 1536 × 1024 ピクセルのローカライズ版を作成してください。

Use case: text-localization
Asset type: Hugo ドキュメントページのリソース
Primary request: 英語版のすべての英文を、対応する日本語へ置換してください。タイトル、各カード、プラットフォーム境界、下部の統制帯以外には文字を追加しないでください。
Text replacements (verbatim): "The Source-Side Boundary" → 「ソース側の境界」; "Phenomena & Activities" → 「事象・活動」; "Source Discovery & Inventory" → 「ソースの発見と棚卸し」; "Data Sources" → 「データソース」; "Data Collection" → 「データ収集」; "Platform Boundary" → 「プラットフォーム境界」; "Data Ingestion" → 「データ取り込み」; "Metadata · Governance · Privacy · Security" → 「メタデータ・ガバナンス・プライバシー・セキュリティ」
Invariants: 英語版と同じキャンバス寸法、構図、カードの位置と寸法、余白、アイコンの種類・個数・位置、矢印の方向・位置・色、プラットフォーム境界線、統制帯、背景、配色、線幅、影、視覚的階層を保つ。変更するのは文字だけとし、日本語が収まるために必要な範囲でのみ文字サイズと改行を調整する
Constraints: 指定した日本語を正確に描画し、ドキュメント本文幅でも読めるようにする
Avoid: アイコンの追加・削除・置換、カードや矢印の変更、レイアウト変更、情報量の変更、英語の残存、指定外の文字、製品ロゴ、透かし
