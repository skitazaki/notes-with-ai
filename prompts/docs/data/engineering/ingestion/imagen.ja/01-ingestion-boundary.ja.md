---
type: image
path: /docs/data/engineering/ingestion
---

# 画像ローカライズプロンプト — 収集から取り込みへ

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/ingestion/ingestion-boundary.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **From Collection to Ingestion** → **収集から取り込みへ**
- **Sources** → **ソース**
- **Data Collection** → **データ収集**
- **Platform Boundary** → **プラットフォーム境界**
- **Data Ingestion** → **データ取り込み**
- **Durable Landing / Raw State** → **永続的なランディング／生データ**
- **Data Processing** → **データ処理**

## Invariants

- Change text only.
- Preserve the exact canvas size, left-to-right sequence, card positions and sizes, source icons, platform-boundary position and line treatment, arrows, colors, borders, background, spacing, and visual hierarchy.
- Keep the platform boundary between Data Collection and Data Ingestion.
- Fit Japanese labels within existing areas using line breaks or smaller font only; do not resize or move containers.
- Use a clean Japanese sans-serif typeface matching the English typography.
- Render every Japanese label exactly and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
