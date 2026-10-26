---
type: image
path: /blog/ai-assisted-content-workflow
description: Three-stage visual guide for the article sections on planning, visual production, and integration and publication.
---

# Image Generation Prompt — Three Stages from Draft to Publication

## Concept

Create a publication-ready infographic that previews and clarifies the three consecutive sections following the article's main workflow overview. Show how planning produces a focused writing brief, how that brief guides a Markdown draft, and how a person and AI collaborate through review and revision to finish the article. Then show how suitable visual material is created and reviewed, and how the complete page is checked and integrated before it is merged to `main` and published on GitHub Pages.

The central message is that writing, visual production, and repository integration are connected stages. In the visual-production stage, conceptual images and structurally precise Mermaid diagrams are alternative methods chosen according to what the reader needs to understand. Both methods converge on review and integration before publication.

## Layout

Use a landscape **16:9 aspect ratio**. Treat **1600 × 900 pixels** as a suggested size only if the image-generation tool requires pixel dimensions; the aspect ratio is the requirement. Put the exact title **“Three Stages from Draft to Publication”** across the top. Below it, arrange three clearly numbered panels from left to right, with equal visual weight and a single arrow connecting each panel to the next. Use blue for Panel 1, green for Panel 2, and purple for Panel 3.

Use this composition:

```text
[1. PLAN AND WRITE] → [2. CREATE VISUAL AIDS] → [3. INTEGRATE AND PUBLISH]
                                │
                  ┌─────────────┴─────────────┐
          [Conceptual image]          [Precise diagram]
                  └─────────────┬─────────────┘
                         [Review visual]
```

Panel 1 represents the section **“Planning and Brief-Driven Writing”**. Show exactly four numbered steps in a vertical top-to-bottom flow, connected by downward arrows. The four steps are: clarify the audience, purpose, and topic; set the outline and prepare a reusable writing brief; create a Markdown draft from that brief; have a person and AI review and revise together until the article is finished. Make the last step visibly distinct from drafting so readers understand that the draft is an intermediate deliverable and collaborative review and revision produce the finished article. Do not display AI product names in the image.

Render the four steps with these labels, in this order:

1. `Clarify audience, purpose, and topic`
2. `Set the outline and prepare the writing brief`
3. `Draft the Markdown article from the brief`
4. `Review and revise collaboratively to finish the article`

Panel 2 represents **“Image Generation and Diagrams”**. Show two alternatives side by side inside the green panel:

- **Conceptual image:** specify the concept, layout, visual cues, and style in a self-contained prompt; generate and inspect the image.
- **Precise diagram:** define nodes and connections; create and validate diagram source, using Mermaid as one concrete example; render a static image when needed.

Bring both alternatives to one shared step labelled **“Review visual”**, then connect the panel to Panel 3.

Panel 3 represents **“Review, Repository Integration, and Publication”** and must clearly show three sequential stages: (1) a grouped review and integration checklist for the complete page, (2) `Merge to main`, and (3) publication on `GitHub Pages`. Put the pre-merge review and integration items together inside one lightly shaded group. Include documentation metadata and sidebar order; previous/next and related-page links; content and visual assets with useful alternative text; and formatting and site-build checks. Treat the checklist items as parallel review concerns, not as an ordered sequence: do not connect checklist items to one another with arrows. Below the group, show `Merge to main`, followed by `GitHub Pages`, with a clear downward arrow from the group to the merge and another from the merge to publication. Do not add any other arrows inside Panel 3. Make clear that repository integration covers the complete page structure, metadata, and navigation as well as any images. The three stages must read visually as review/integration → merge → publication.

Use this Panel 3 arrangement:

```text
┌ Lightly shaded review and integration group ───────┐
│ Metadata and docs navigation                      │
│ Sidebar order and prev/next links                  │
│ Links and accessible image text                    │
│ Formatting and site-build checks                   │
└──────────────────────────┬────────────────────────┘
                           ↓
                    [Merge to main]
                           ↓
                     [GitHub Pages]
```

## Visual cues

Render these labels exactly, with capitalization and punctuation preserved:

- `Three Stages from Draft to Publication`
- `Plan and write`
- `Planning and Brief-Driven Writing`
- `Clarify audience, purpose, and topic`
- `Set the outline and prepare the writing brief`
- `Draft the Markdown article from the brief`
- `Review and revise collaboratively to finish the article`
- `Create visual aids`
- `Image Generation and Diagrams`
- `Conceptual image`
- `Precise diagram`
- `Self-contained prompt`
- `Diagram source`
- `Review visual`
- `Integrate and publish`
- `Review, Repository Integration, and Publication`
- `Metadata and docs navigation`
- `Sidebar order and prev/next links`
- `Links and accessible image text`
- `Formatting and site-build checks`
- `Merge to main`
- `GitHub Pages`

Show exactly two alternatives within Panel 2: a conceptual-image path and a precise-diagram path. Make both paths converge on `Review visual`, then continue to Panel 3. Within Panel 3, group all pre-merge review and integration checks together, then show the distinct sequence `Merge to main` → `GitHub Pages`. The main sequence must remain:

```text
Plan and write → Create visual aids → Integrate and publish
Conceptual image ─┐
                  ├→ Review visual → Integrate and publish
Precise diagram ──┘
```

Do not make either visual method feed directly to publication or bypass review. Do not present image generation as a substitute for exact structural relationships. Do not imply that every article requires both visual methods. Do not connect the pre-merge checks to one another with arrows. Do not add extra stages beyond the four steps within Panel 1 and the three main panels, additional branches, AI product names, product logos, unsupported metrics, or text beyond the labels and short phrases specified here. Do not add a subtitle or lead text below the title.

## Style

- Clean editorial infographic for a technical blog, not a product advertisement.
- Precise vector-like shapes and typography, with consistent arrows and clear grouping.
- Use a light neutral background and dark readable text. Color Panel 1 blue, Panel 2 green, and Panel 3 purple.
- Give the two visual alternatives distinct but balanced treatments within Panel 2; they may share green tones.
- Use generous whitespace and readable labels at normal article-column width.
- Keep the three main panels aligned and visually equal in importance.
- Use an opaque background and a raster-ready composition suitable for conversion to WebP.
- Avoid tiny text, dense paragraphs, decorative filler, gradients that reduce contrast, watermarks, and unnecessary icons.
