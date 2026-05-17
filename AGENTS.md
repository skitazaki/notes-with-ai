# AGENTS.md

This file defines how generative AI services should work in this repository.

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

## Workflow For AI Services

### 1. Work as content director first

Your first job is to clarify the writing assignment so another AI writer can execute it well.

A good prompt brief in this repository should define:

- target content type: `docs` or `blog`
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
type: docs
path: /docs/data/management
---
```

Use `type: docs` for documentation prompts and `type: blog` for blog prompts.

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

## File Placement Rules

Place prompts in the directory that mirrors the eventual content location as closely as practical.

Examples:

- documentation prompt for `content/docs/data/management/_index.md` -> `prompts/docs/data/data-management.md`
- documentation prompt for `content/docs/swe/idp/_index.md` -> `prompts/docs/swe/internal-developer-portal.md`
- blog prompt for `content/blog/2026-data-stack/index.md` -> `prompts/blog/2026-data-stack.md`

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
