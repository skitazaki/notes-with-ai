---
type: image
path: /ja/docs/data/engineering/processing
---

# 画像ローカライズプロンプト — データ処理の契約

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/processing/data-processing-contract.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **Data Processing Contract** → **データ処理の契約**
- **Ingested Data** → **取り込み済みデータ**
- **Data Processing** → **データ処理**
- **Filter** → **抽出**
- **Join** → **結合**
- **Aggregate** → **集計**
- **Enrich** → **付加**
- **Validate** → **検証**
- **Published Data** → **公開データ**
- **Repeatable** → **反復可能**
- **Recoverable** → **復旧可能**
- **Observable** → **観測可能**

## Invariants

- Change text only.
- Preserve the exact canvas size, input-processing-output layout, container positions and sizes, five operation cards and their icons, validation-gate position, three quality chips, arrows, colors, borders, background, spacing, and visual hierarchy.
- Keep Filter, Join, Aggregate, and Enrich equal in visual weight.
- Do not introduce additional contract, schema, or meaning labels.
- Fit Japanese labels within existing areas using line breaks or smaller font only; do not resize or move containers.
- Use a clean Japanese sans-serif typeface matching the English typography.
- Render every Japanese label exactly and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
