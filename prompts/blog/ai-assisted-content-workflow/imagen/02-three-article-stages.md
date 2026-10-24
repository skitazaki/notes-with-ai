---
type: image
path: /blog/ai-assisted-content-workflow
description: Three-stage visual guide for the article sections on planning, visual production, and integration and publication.
---

# Image Generation Prompt — Three Stages from Draft to Publication

## Concept

Create a publication-ready infographic that previews and clarifies the three consecutive sections following the article's main workflow overview. Show how a focused brief becomes a draft, how a suitable visual is selected and prepared, and how the complete page is integrated, reviewed, and published.

The central message is that writing, visual production, and repository integration are connected stages. In the visual-production stage, conceptual images and structurally precise Mermaid diagrams are alternative methods chosen according to what the reader needs to understand. Both methods converge on review and integration before publication.

## Layout

Use a landscape **16:9 aspect ratio**. Treat **1600 × 900 pixels** as a suggested size only if the image-generation tool requires pixel dimensions; the aspect ratio is the requirement. Put the exact title **“Three Stages from Draft to Publication”** across the top. Below it, arrange three clearly numbered panels from left to right, with equal visual weight and a single arrow connecting each panel to the next.

Use this composition:

```text
[1. PLAN AND WRITE] → [2. CREATE VISUAL AIDS] → [3. INTEGRATE AND PUBLISH]
                                │
                  ┌─────────────┴─────────────┐
          [Conceptual image]          [Precise diagram]
                  └─────────────┬─────────────┘
                         [Review visual]
```

Panel 1 represents the section **“Planning and Brief-Driven Writing”**. Show this sequence: define audience, purpose, scope, and central message; prepare a reusable brief; use the brief to guide a Markdown draft.

Panel 2 represents **“Image Generation and Mermaid Diagrams”**. Show two alternatives side by side inside this panel:

- **Conceptual image:** specify the concept, layout, visual cues, and style in a self-contained prompt; generate and inspect the image.
- **Precise diagram:** define nodes and connections; create and validate Mermaid source; render a static image when needed.

Bring both alternatives to one shared step labelled **“Review visual”**, then connect the panel to Panel 3.

Panel 3 represents **“Review, Repository Integration, and Publication”**. Show the complete page being integrated and checked: documentation metadata and sidebar order; previous/next and related-page links; content and visual assets with useful alternative text; formatting and site-build review; merge to `main` and GitHub Pages publication. Make it clear that repository integration includes the page structure, metadata, and navigation as well as any images.

## Visual cues

Render these labels exactly, with capitalization and punctuation preserved:

- `Three Stages from Draft to Publication`
- `Plan and write`
- `Planning and Brief-Driven Writing`
- `Create visual aids`
- `Image Generation and Mermaid Diagrams`
- `Conceptual image`
- `Precise diagram`
- `Self-contained prompt`
- `Mermaid source`
- `Review visual`
- `Integrate and publish`
- `Review, Repository Integration, and Publication`
- `Metadata and docs navigation`
- `Sidebar order and prev/next links`
- `Links and accessible image text`
- `Merge to main`
- `GitHub Pages`

Show exactly two alternatives within Panel 2: a conceptual-image path and a precise-diagram path. Make both paths converge on `Review visual`, then continue to Panel 3. The main sequence must remain:

```text
Plan and write → Create visual aids → Integrate and publish
Conceptual image ─┐
                  ├→ Review visual → Integrate and publish
Precise diagram ──┘
```

Do not make either visual method feed directly to publication or bypass review. Do not present image generation as a substitute for exact structural relationships. Do not imply that every article requires both visual methods. Do not add extra stages, additional branches, product logos, unsupported metrics, or text beyond the labels and short phrases specified here.

## Style

- Clean editorial infographic for a technical blog, not a product advertisement.
- Precise vector-like shapes and typography, with consistent arrows and clear grouping.
- Use a light neutral background, dark readable text, and three coordinated accent colors, one for each main panel.
- Give the two visual alternatives distinct but balanced treatments within Panel 2.
- Use generous whitespace and readable labels at normal article-column width.
- Keep the three main panels aligned and visually equal in importance.
- Use an opaque background and a raster-ready composition suitable for conversion to WebP.
- Avoid tiny text, dense paragraphs, decorative filler, gradients that reduce contrast, watermarks, and unnecessary icons.
