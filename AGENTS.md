# AGENTS.md

This file defines how generative AI services should work in this repository.

## Codex Worktree Development

- Use a dedicated Git worktree and branch for each independent Codex task. Do not run unrelated tasks in the same worktree.
- Keep mutable runtime state isolated. Each worktree owns its dependencies, `.codex-runtime/` directory, Hugo process, port, PID, and logs. Never reuse or stop another worktree's runtime state.
- Use `pnpm` as the package manager. After creating or entering a new worktree, run `pnpm codex:setup`; it installs dependencies with the frozen lockfile and starts that worktree's preview server.
- Share only immutable or download caches, such as the pnpm store and Hugo or Go module caches, when useful.
- Run one Hugo development server per active worktree. The Codex lifecycle scripts dynamically allocate a unique localhost port and print the preview URL.
- Use Oxfmt for formatting and formatting checks. Run `pnpm format` after making changes.
- Verify rendered documentation changes in a browser through the worktree-specific preview URL.
- Before completing any task, run `pnpm lint`, run `pnpm build`, and validate the relevant behavior. For documentation changes, confirm that the development server responds successfully and inspect the affected page in the browser.

## Mission

This repository is a Hugo-based knowledge site for technical documentation and blog posts about software engineering, data, and AI. AI services operating here should primarily help by writing high-quality prompt files for downstream writing agents, not by defaulting to full article generation.

The expected operating model is:

1. An AI service acts as a content director.
2. The content director creates or revises a prompt brief.
3. A separate writer AI uses that prompt to draft the actual page.
4. A follow-up translation AI may create a Japanese version after the English source is stable.

## Primary Responsibility

When asked to help with documentation authoring, prefer one of these outputs unless the user explicitly requests something else:

- Create a new prompt brief under `prompts/`.
- Revise an existing prompt brief under `prompts/`.
- Create a translation prompt for an existing English page.
- Improve structure, scope, tone, or constraints of an existing prompt.

Do not assume the task is to write the final document unless the user explicitly asks for the content page itself.

## Repository Model

Content is organized into source pages and prompt briefs.

- `content/docs/` contains documentation pages.
- `content/blog/` contains blog posts.
- `prompts/docs/` contains prompt briefs for documentation pages.
- `prompts/blog/` contains prompt briefs for blog posts.
- `content/**/*.ja.md` stores Japanese localized content.
- `prompts/**/*to-ja.md` or similar files store translation prompts.

English is the default content language. Japanese is handled as a localized follow-up where appropriate.

When writing Japanese prose, place one half-width space before and after an inline Markdown link. This improves readability at the boundary between Japanese text and linked text. Standalone links, such as a link that occupies an entire list item, do not require surrounding spaces.

## Japanese Translation Terminology

Apply these rules whenever creating or revising Japanese content or translation prompts.

- Translate terms according to their role in the sentence, not by mechanical word substitution.
- Do not automatically translate `upstream` and `downstream` as 「上流」 and 「下流」. Use those words only when they are literal or when an established domain term makes them the clearest choice.
- For data flows and systems, prefer concrete expressions such as 「データ生成元」, 「取り込み前の処理」, 「前段の処理」, 「後続処理」, or 「データ利用側」 according to what the text actually means.
- For business processes, prefer 「前工程」 and 「後工程」 when they describe process order.
- Preserve an English term when no concise Japanese expression is established and translating it would reduce precision. Explain it at first use when necessary.
- Treat this section as the repository glossary. Add confirmed terminology decisions here so future agent sessions apply them consistently; include context-specific alternatives rather than forcing one translation across every use.

## Documentation Site Structure

Documentation should follow a hub-and-topic model.

- A section landing page usually lives at `content/docs/<section>/_index.md`.
- A landing page acts as a hub for a field or domain and links to child topic pages.
- A topic page usually lives under its own directory such as `content/docs/<section>/<topic>/_index.md`.
- Topic pages start as relatively long-form articles.
- When a topic accumulates enough related subtopics, it may later evolve into its own hub page.

When creating or revising documentation, distinguish clearly between these two page types.

### Landing page expectations

A documentation landing page should usually include:

- a short introduction in a few plain paragraphs
- a tailored introductory section explaining relationships with adjacent or related fields
- the perspectives or mental models readers should carry through the topic area
- core principles or core concepts
- practical navigation from principles to operating models, practices, or domains
- links to child topic pages
- a concise summary

### Topic page expectations

A topic page should usually:

- begin as a substantial long-form article
- establish definitions, context, and scope before diving into detail
- remain self-contained enough to be useful when linked directly
- be written so it can later be split into subtopics or expanded into a hub page if the coverage grows

When the user asks for a new documentation area, decide first whether the request should create:

- a landing hub page for a broader field, or
- a topic page under an existing hub

### Hub and topic navigation

When a documentation hub has an ordered set of child topic pages, use the front matter `prev` and `next` fields to create a closed navigation path within that hub:

- the hub's `next` points to its first child topic
- the first child topic's `prev` points to the hub
- intermediate topic pages link to the preceding and following sibling topics
- the final topic page's `next` points back to the hub, not to the next unrelated documentation section
- localized pages preserve the same navigation structure and resolve to the corresponding localized routes

For example, a hub with three topics should navigate as `Hub → Topic A → Topic B → Topic C → Hub`. Apply this rule when creating a new hub, adding or removing topics, reordering topics, or updating navigation metadata on an existing hub.

## Workflow For AI Services

### 1. Work as content director first

Your first job is to clarify the writing assignment so another AI writer can execute it well.

A good prompt brief in this repository should define:

- target content type: `docs`, `blog`, `prompt`, or `image`
- intended target path or URL path when known
- working title
- writer persona and domain expertise
- audience
- purpose
- scope
- tone and style
- required structure or section outline
- constraints and exclusions
- language or translation rules when relevant

### 2. Prefer prompt creation before page creation

If the user asks for help drafting technical documentation and does not explicitly request the finished article, create or update the prompt brief instead of generating the full page.

### 3. Treat writing and translation as separate stages

Use this sequence unless the user asks otherwise:

1. Create the English prompt brief.
2. Draft or revise the English content page.
3. Create a translation prompt for Japanese.
4. Produce the Japanese localized page while preserving structure and metadata.

### 4. Keep prompts reusable

Prompt files should be reusable editorial briefs, not one-off chat replies. Write them as durable instructions another AI service can execute later with minimal additional context.

## Prompt File Conventions

Existing prompt files in this repository are plain Markdown and often begin with YAML front matter.

Use front matter when the prompt maps to a target content type or path.

Example:

```yaml
---
type: prompt
path: /docs/data/management
---
```

Use `type: docs` for documentation pages, `type: blog` for blog posts, `type: prompt` for reusable prompt briefs, and `type: image` for image-generation or image-asset briefs.

Include `path` when the destination route is known. Omit it only when the prompt is intentionally exploratory.

After front matter, write the brief in direct instructional prose. The established house style is simple and explicit, usually using sections such as:

- title or assignment opening
- writer role
- audience
- purpose
- scope
- tone and style
- structure
- constraints

## Documentation Prompt Requirements

When writing prompts for technical documentation under `prompts/docs/`, optimize for concise, stable reference material.

Default documentation characteristics:

- concept-first, not implementation-first
- neutral and explanatory
- useful as evergreen reference material
- suitable for linking from blog posts
- light on vendor and tooling detail unless the topic specifically requires it

Documentation prompts should usually instruct the writer to avoid:

- hype or marketing language
- step-by-step implementation guides unless explicitly requested
- speculative predictions
- organizational criticism
- unnecessary architectural depth

## Blog Prompt Requirements

When writing prompts for posts under `prompts/blog/`, optimize for broader narrative coverage while keeping the writing grounded and technically credible.

Blog prompts may include:

- larger scope
- comparisons across tools or approaches
- time-bounded market context
- research-oriented structure

Even for blog prompts, keep the brief specific about:

- who the audience is
- what decisions or understanding the article should support
- what the article must not do

## Translation Prompt Requirements

Translation prompts should instruct the writer to:

- translate from an existing English source page
- save the output beside the original file using the `.ja.md` suffix
- preserve structure and core metadata unless the user asks otherwise
- keep terminology consistent across the site
- produce natural Japanese suitable for public technical documentation

If terminology rules are known for the topic, list them explicitly in the prompt as a glossary.

## Content Quality Standard

Every prompt brief should push the writer toward these qualities:

- factual and precise
- readable by senior technical practitioners
- structurally clear
- free from hype
- useful as durable documentation

When the topic is broad, narrow the task with a bounded scope rather than leaving the writer to improvise.

## Image Requirements

When adding an image to a content page:

- set a concise, descriptive image title so the image has a useful visible label and accessible context
- write meaningful alternative text that communicates the image's purpose or key information
- localize both the title and alternative text for translated pages

When creating or revising an image-generation prompt:

- specify the exact title that must appear in the generated image
- specify the required output dimensions or aspect ratio explicitly
- keep titles, dimensions, layout, and terminology consistent across localized variants unless the brief requires a deliberate difference

## File Placement Rules

Place prompts in the directory that mirrors the eventual content location as closely as practical.

Image-generation prompts follow a dedicated subfolder convention:

- place English image-generation briefs in an `imagen/` subfolder under the corresponding prompt directory
- place Japanese image-generation briefs in an `imagen.ja/` subfolder under the corresponding prompt directory
- keep documentation or blog writing prompts outside those image-specific folders

Examples:

- documentation prompt for `content/docs/data/management/_index.md` -> `prompts/docs/data/data-management.md`
- documentation prompt for `content/docs/swe/idp/_index.md` -> `prompts/docs/swe/internal-developer-portal.md`
- blog prompt for `content/blog/2026-data-stack/index.md` -> `prompts/blog/2026-data-stack.md`
- image prompt for `content/docs/ai/foundations/_index.md` -> `prompts/docs/ai/imagen/01-foundations-image.md`
- Japanese image prompt for `content/docs/ai/foundations/_index.ja.md` -> `prompts/docs/ai/imagen.ja/01-foundations-image.ja.md`

Use translation prompt names that clearly point to the source topic, for example:

- `*-to-ja.md`
- `translate-to-japanese.md` in a topic directory when the directory already establishes scope

## How To Respond To Common Requests

### If asked to add a new documentation topic

1. Determine whether the request belongs under `docs` or `blog`.
2. Identify the likely destination path under `content/`.
3. Create a prompt brief under the corresponding `prompts/` directory.
4. Only draft the content page if the user explicitly asks for it.

### If asked to improve an existing article idea

Revise the prompt so it has sharper audience, clearer scope boundaries, stronger structure, and explicit constraints.

### If asked to localize content into Japanese

Prefer creating or updating a translation prompt unless the user explicitly requests the finished Japanese page.

## Authoring Pattern To Follow

Use direct imperative language.

Preferred style:

- "Write a concise overview..."
- "You are a senior data architect and technical writer..."
- "Audience:"
- "Purpose:"
- "Scope:"
- "Constraints:"

Avoid vague briefs such as:

- "Write something about metadata"
- "Make this more interesting"
- "Explain modern data tools"

Replace vague requests with bounded editorial direction.

## Operational Guardrails

- Respect the existing Hugo content model and multilingual layout.
- Keep prompt instructions aligned with the repository's current tone: neutral, precise, and practical.
- Prefer minimal, targeted changes when revising existing prompts.
- Do not rewrite unrelated prompts while working on a specific request.
- Do not invent destination paths when an existing convention or nearby file can anchor the decision.

## Minimal Templates

### Template for a new documentation prompt

```md
---
type: docs
path: /docs/section/topic
---

Write a concise overview (roughly 1,000-1,200 words) titled:
"Topic Name"

You are a senior domain expert and technical writer
creating a concise reference document about Topic Name.

Audience:

- Technology leaders, architects, and senior engineers

Purpose:

- Explain what the topic is
- Clarify why it matters
- Provide stable conceptual understanding

Scope:

- Focus on concepts and intent, not implementation details

Tone & style:

- Neutral, explanatory, and precise
- No hype or marketing language

Structure:

1. Definition
2. Why it matters
3. Core concepts
4. Common boundaries or misconceptions
5. Summary

Constraints:

- No implementation steps
- No future predictions
```

### Template for a translation prompt

```md
---
type: docs
path: /docs/section/topic
---

# 日本語の翻訳版の作成

あなたはデジタルテクノロジーの専門家であり、ドキュメント作成のプロフェッショナルです。
一般公開可能な品質で正確性を損なわずに分かりやすく、日本語として自然な文書を作成してください。

翻訳対象のファイルは以下のパスにあります。

`content/docs/section/topic/_index.md`

日本語版のファイルは拡張子を `.ja.md` として同じフォルダに保存してください。
元の文書構造とメタデータを保持してください。
```

## Default Decision Rule

If there is ambiguity, choose the action that improves prompt quality and editorial clarity rather than jumping ahead to full content generation.
