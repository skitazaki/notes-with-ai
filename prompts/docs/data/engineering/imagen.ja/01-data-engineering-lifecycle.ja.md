---
type: image
path: /ja/docs/data/engineering
---

# 画像ローカライズプロンプト — データエンジニアリングのライフサイクル

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/data-engineering-lifecycle.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **Data Engineering Lifecycle** → **データエンジニアリングのライフサイクル**
- **Source Systems** → **ソースシステム**
- **Data Ingestion** → **データ取り込み**
- **Processing & Transformation** → **処理と変換**
- **Delivery & Serving** → **配信と提供**
- **Analytics, Applications & AI** → **分析・アプリケーション・AI**
- **Orchestration** → **オーケストレーション**
- **Observability** → **可観測性**
- **Automation** → **自動化**
- **Reliability** → **信頼性**

## Invariants

- Change text only.
- Preserve the exact canvas size, composition, card positions and sizes, icon selection and placement, arrow routing, foundation-band geometry, colors, borders, line weights, background, spacing, and visual hierarchy of the English image.
- Preserve the five-stage left-to-right flow and the four-item foundation band exactly.
- Fit Japanese labels by adjusting font size or line breaks inside the existing text areas only; do not resize or move containers.
- Use a clean Japanese sans-serif typeface with weight and visual size matching the English typography.
- Render every Japanese label exactly as written and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
