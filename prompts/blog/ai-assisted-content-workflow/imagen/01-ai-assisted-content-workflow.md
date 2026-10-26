---
type: image
path: /blog/ai-assisted-content-workflow
description: Overview infographic replacing the article's Mermaid workflow diagram.
---

# Image Generation Prompt — AI-Assisted Content Workflow

## Concept

Create a publication-ready infographic that replaces a large workflow diagram in a technical blog article. Explain how an individual author uses ChatGPT, Codex, and GitHub Copilot to move an article from an idea through planning, writing, review, publication, and learning.

The central message is that these tools have complementary primary roles, while the author directs the process, verifies claims, and decides what is ready to publish. Show a repeatable workflow with clear handoffs and one feedback loop from later review and reader response back to future planning.

## Layout

Use a landscape **16:9 aspect ratio**. Treat **1600 × 900 pixels** as a suggested size only if the image-generation tool requires pixel dimensions; the aspect ratio is the requirement. Use a clear left-to-right flow with five equally sized stage cards and generous spacing. Place the exact title **“AI-Assisted Content Workflow”** at the top and the subtitle **“From idea to publication, with human direction”** directly beneath it.

Arrange the five cards in this order:

```text
[1. PLAN] → [2. BRIEF] → [3. DRAFT] → [4. REVIEW] → [5. PUBLISH]
     ↑                                                       │
     └──── Git history and reader response inform new plans ─┘
```

Include these elements inside the cards:

1. **Plan the idea** — ChatGPT helps clarify the audience, purpose, scope, and article structure. An idea can begin with the author, an AI assistant, or a discussion.
2. **Prepare the brief** — ChatGPT turns the article plan into a concrete writing brief that records the intended reader, outline, evidence needs, and scope boundaries. Show ChatGPT as the primary tool for this stage, and label the handoff location `prompts/`. Do not assign brief preparation to Codex.
3. **Draft the page** — Codex turns the brief into Markdown in `content/`, which contains both documentation and blog content. Include a small note that visual material is planned when it helps explain the article.
4. **Review together** — GitHub Copilot supports clarity and gap review; Codex can revise repository files. The author verifies evidence, links, metadata, any visual assets, and the rendered page.
5. **Publish and learn** — show pull-request checks before merge, then a merge to `main` leading to a production build and GitHub Pages publication. Reader response and later repository review inform future planning.

Connect each card to the next with one clear arrow. Draw a single feedback connector from stage 5 back to stage 1 below the cards. Keep the feedback connector separate from the forward path.

## Visual cues

Render these labels exactly, with capitalization and punctuation preserved:

- `AI-Assisted Content Workflow`
- `From idea to publication, with human direction`
- `Plan the idea`
- `Prepare the brief`
- `Draft the page`
- `Plan a visual when it helps`
- `Review together`
- `Publish and learn`
- `ChatGPT`
- `Codex`
- `GitHub Copilot`
- `prompts/`
- `content/`
- `main`
- `GitHub Pages`
- `Git history and reader response inform new plans`

Show `ChatGPT` as the primary tool in both the planning and brief-preparation stages. If a compact tool-role legend appears below the workflow, describe ChatGPT's role as `Planning, brief creation, and image generation`.

Use short supporting phrases only; do not add explanatory paragraphs inside the cards. Use generic, consistent line icons if needed, never product logos. Make the five forward stages visually distinct from the one return arrow.

The required connections are only:

```text
Plan the idea → Prepare the brief → Draft the page → Review together → Publish and learn
Publish and learn → Plan the idea (feedback loop)
```

Do not add a branch that bypasses the brief or review. Do not make image generation a required workflow stage: show visual planning as a conditional note within the drafting stage. Do not imply that ChatGPT, Codex, or GitHub Copilot is limited to only one capability; present their primary roles described above. In particular, show ChatGPT preparing the brief and Codex drafting from it. Do not imply that AI output or AI review guarantees factual correctness.

## Style

- Clean editorial infographic for a technical blog.
- Precise vector-like shapes and typography, with strong contrast and generous whitespace.
- Calm, coordinated colors that distinguish the five stages without implying a quality ranking.
- Use a light neutral background and readable dark text.
- Make labels legible at a typical article-column display size.
- Keep the layout balanced and compact; avoid a tall, sprawling flowchart.
- Use an opaque background and a raster-ready composition suitable for conversion to WebP.
- No decorative filler, gradients that reduce contrast, small footnotes, watermarks, or extra text.
