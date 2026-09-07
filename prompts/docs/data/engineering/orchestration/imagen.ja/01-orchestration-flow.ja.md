---
type: image
path: /docs/data/engineering/orchestration
---

# 画像ローカライズプロンプト — 信頼できるワークフローのオーケストレーション

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/orchestration/orchestration-flow.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **Orchestrating a Reliable Workflow** → **信頼できるワークフローのオーケストレーション**
- **Ingest** → **取り込み**
- **Validate** → **検証**
- **Transform** → **変換**
- **Quality Checks** → **品質チェック**
- **Publish** → **公開**
- **Notify** → **通知**
- **State** → **状態**
- **Retries** → **再試行**
- **Timeouts** → **タイムアウト**

## Invariants

- Change text only.
- Preserve the exact canvas size, workflow-frame geometry, node positions and sizes, icons, branch and rejoin routing, connector styles, three operational-control positions, colors, borders, background, spacing, and visual hierarchy.
- Keep Quality Checks as the required branch that rejoins before Publish.
- Fit Japanese labels within existing areas using line breaks or smaller font only; do not resize or move containers.
- Use a clean Japanese sans-serif typeface matching the English typography.
- Render every Japanese label exactly and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
