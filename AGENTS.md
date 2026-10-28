# AGENTS.md

This file defines how generative AI services should work in this repository.

## Commit message conventions

Use Conventional Commits for all repository changes. The commit message format should be:

`<type>(<scope>): <summary>`

Use a lowercase type and an imperative summary. Keep the scope optional when it would add noise. Examples:

- `docs: clarify AGENTS guidance`
- `chore: align repo rules with local Codex setup`
- `fix: correct broken link in navigation`

Preferred types include `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `build`, `ci`, and `revert`. Avoid vague messages such as `update`, `changes`, or `fix stuff`.

## Branch and commit workflow

Never commit directly to `main`. Before making repository changes, inspect the current branch and working tree so existing work is preserved and the destination for any commit is clear.

- Reuse the current branch when it is already an appropriate task branch. Do not create another branch just because a new request arrived; follow-up work on the same task can stay on its existing branch.
- When starting work from `main` that is expected to be committed, create or select an appropriate task branch before committing.
- Prefer descriptive task prefixes such as `docs/`, `fix/`, `chore/`, or `refactor/` for normal work.
- Use tool-specific prefixes such as `codex/`, `claude/`, or `copilot/` only for independent, parallel workstreams owned by separate assistants.
- Whether to create a new branch for a task depends on the context. Consider whether the work is part of an existing task, needs isolation, or will be committed. Regardless, commits must be made on a branch other than `main`.
- Before committing, verify the current branch again. If it is `main`, switch to an appropriate task branch first, preserving the changes and commits.
- For independent parallel tasks, use a separate worktree and branch for each task. Never let two agents modify the same worktree.
- Default branch naming to the work being done; reserve tool-specific prefixes for truly separate agent-specific tasks that run alongside other workstreams.
- When creating a pull request, identify and run the repository's standard lint or format checks, then record the commands and results in the PR body.
- For this repository, the standard format check is `pnpm exec oxfmt --check .` and the standard build validation is `hugo --quiet`.
- If a PR changes Markdown or repository formatting, run the formatter check before considering the work ready to review.

## Mission

This repository is a Hugo-based knowledge site for technical documentation and blog posts about software engineering, data, and AI. AI services operating here should primarily help by writing high-quality prompt files for downstream writing agents, not by defaulting to full article generation.

The expected operating model is:

1. An AI service acts as a content director.
2. The content director creates or revises a prompt brief.
3. A separate writer AI uses that prompt to draft the actual page.
4. A follow-up translation AI may create a Japanese version after the English source is stable.

## Primary Responsibility

For prompt-first authoring guidance, including when to create a prompt versus a content page, follow [prompts/AGENTS.md](prompts/AGENTS.md).

## Repository Model

Content is organized into source pages and prompt briefs.

- `content/docs/` contains documentation pages.
- `content/blog/` contains blog posts.
- `prompts/docs/` contains prompt briefs for documentation pages.
- `prompts/blog/` contains prompt briefs for blog posts.
- `content/**/*.ja.md` stores Japanese localized content.
- `prompts/**/*to-ja.md` or similar files store translation prompts.

English is the default content language. Japanese is handled as a localized follow-up where appropriate.

When writing Japanese prose, place one half-width space before and after an inline Markdown link. This improves readability at the boundary between Japanese text and linked text. Do not insert a space immediately after Japanese punctuation such as 「、」 or 「。」 when a link follows; keep the punctuation attached to the preceding text and place the space before the link instead. Standalone links, such as a link that occupies an entire list item, do not require surrounding spaces.

## Japanese Translation Terminology

Apply these rules whenever creating or revising Japanese content or translation prompts.

- Translate terms according to their role in the sentence, not by mechanical word substitution.
- Do not automatically translate `upstream` and `downstream` as 「上流」 and 「下流」. Use those words only when they are literal or when an established domain term makes them the clearest choice.
- For data flows and systems, prefer concrete expressions such as 「データ生成元」, 「取り込み前の処理」, 「前段の処理」, 「後続処理」, or 「データ利用側」 according to what the text actually means.
- For business processes, prefer 「前工程」 and 「後工程」 when they describe process order.
- Preserve an English term when no concise Japanese expression is established and translating it would reduce precision. Explain it at first use when necessary.
- Treat this section as the repository glossary. Add confirmed terminology decisions here so future agent sessions apply them consistently; include context-specific alternatives rather than forcing one translation across every use.

## Documentation Site Structure

Documentation should follow a domain-and-topic model.

- A domain overview page usually lives at `content/docs/<section>/_index.md`.
- A domain overview introduces a technical domain and links to the topic pages within it.
- A topic page usually lives under its own directory such as `content/docs/<section>/<topic>/_index.md`.
- Topic pages start as relatively long-form articles.
- A topic may contain nested subtopics, and a mature topic area can later become a broader domain overview in its own right.

Use these terms consistently:

- `domain`: a top-level technical area such as Data, AI, or Software Architecture
- `topic`: a major thematic area within a domain
- `subtopic`: a nested topic inside a topic when the subject expands further

When creating or revising documentation, distinguish clearly between these page types.

### Domain overview expectations

A domain overview should usually include:

- a short introduction in a few plain paragraphs
- a tailored introductory section explaining relationships with adjacent or related domains
- the perspectives or mental models readers should carry through the domain
- core principles or core concepts
- practical navigation from principles to operating models, practices, or adjacent domains
- links to child topic pages
- a concise summary

### Topic page expectations

A topic page should usually:

- begin as a substantial long-form article
- establish definitions, context, and scope before diving into detail
- remain self-contained enough to be useful when linked directly
- be written so it can later be split into subtopics or expanded into a broader domain overview if the coverage grows

When the user asks for a new documentation area, decide first whether the request should create:

- a domain overview for a broader technical area, or
- a topic page under an existing domain

### Domain and topic navigation

When a domain overview has an ordered set of child topic pages, use the front matter `prev` and `next` fields to create a closed navigation path within that domain:

- the domain overview's `next` points to its first child topic
- the first child topic's `prev` points to the domain overview
- intermediate topic pages link to the preceding and following sibling topics
- the final topic page's `next` points back to the domain overview, not to the next unrelated documentation section
- localized pages preserve the same navigation structure and resolve to the corresponding localized routes

For example, a domain with three topics should navigate as `Domain → Topic A → Topic B → Topic C → Domain`. Apply this rule when creating a new domain overview, adding or removing topics, reordering topics, or updating navigation metadata on an existing domain page.

## Image Requirements

When adding an image to a content page:

- set a concise, descriptive image title so the image has a useful visible label and accessible context
- write meaningful alternative text that communicates the image's purpose or key information
- localize both the title and alternative text for translated pages
- convert display images to WebP before committing them, and reference the WebP asset from the content page

For prompt creation and revision, including translation and image-generation briefs, follow [prompts/AGENTS.md](prompts/AGENTS.md). It is the source of truth for prompt structure, requirements, placement, and review.
