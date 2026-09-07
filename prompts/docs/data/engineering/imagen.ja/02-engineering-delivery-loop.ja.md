---
type: image
path: /docs/data/engineering
---

# 画像ローカライズプロンプト — エンジニアリングのデリバリーループ

英語版画像を編集対象として使用し、日本語版へローカライズしてください。

Use case: text-localization
Asset type: Hugo documentation page resource
Input image: `content/docs/data/engineering/engineering-delivery-loop.webp` — edit target and authoritative layout reference
Primary request: Replace only the English text with the Japanese text mapping below.
Output: 1536 × 1024 pixels, 3:2 landscape

## Text replacement map

- **Engineering Delivery Loop** → **エンジニアリングのデリバリーループ**
- **Code** → **コード**
- **Test** → **テスト**
- **Build** → **ビルド**
- **Deploy** → **デプロイ**
- **Operate** → **運用**
- **Observe** → **観測**
- **Feedback** → **フィードバック**

## Invariants

- Change text only.
- Preserve the exact canvas size, clockwise loop, six card positions and sizes, icons, arrow direction and routing, feedback label position, colors, borders, line weights, background, spacing, and visual hierarchy.
- Use one continuous connector with exactly one arrowhead at the destination of each adjacent stage.
- The Build-to-Deploy connector must run rightward, curve downward, and then curve leftward into Deploy. Remove the intermediate downward arrowhead and any connector break; retain only the final left-pointing arrowhead entering Deploy.
- Keep all six stages equal in visual weight.
- Fit Japanese labels inside the existing text areas by adjusting font size only when necessary; do not move or resize cards.
- Use a clean Japanese sans-serif typeface matching the English typography.
- Render every Japanese label exactly and remove all English text.
- Do not add, remove, redraw, or reinterpret any visual element.
