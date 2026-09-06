---
type: image
path: /ja/docs/data/engineering
---

# 画像ローカライズプロンプト — データエコシステムにおけるデータエンジニアリング

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/data-engineering-ecosystem.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **Data Engineering in the Data Ecosystem** → **データエコシステムにおけるデータエンジニアリング**
- **Metadata — describes and connects** → **メタデータ — 記述して接続する**
- **Data Architecture** → **データアーキテクチャ**
- **Structure & Patterns** → **構造とパターン**
- **Data Engineering** → **データエンジニアリング**
- **Implementation & Operations** → **実装と運用**
- **Data Management** → **データマネジメント**
- **Trust & Sustainability** → **信頼と持続性**
- **Ingestion** → **取り込み**
- **Processing** → **処理**
- **Orchestration** → **オーケストレーション**
- **Observability** → **可観測性**
- **Privacy — constrains responsible handling** → **プライバシー — 責任ある取扱いを制約する**

## Invariants

- Change text only.
- Preserve the exact canvas size, three peer-card positions and equal sizes, icons, four capability-chip positions, metadata and privacy band geometry, colors, borders, line weights, background, spacing, and visual hierarchy.
- Preserve the peer relationship among Architecture, Engineering, and Management; do not introduce hierarchy.
- Fit Japanese labels within existing areas using line breaks or smaller font only; do not resize or move containers.
- Use a clean Japanese sans-serif typeface matching the English typography.
- Render every Japanese label exactly and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
