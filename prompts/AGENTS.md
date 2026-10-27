# Prompt Writing Guidelines

Use these guidelines when creating or revising prompts in this directory. Prompts are durable briefs for a later writing or image-generation step. Give the next agent enough context to work without relying on the conversation that created the prompt.

## Writing prompts

Start by identifying the deliverable and its destination. Follow nearby prompt conventions and the repository's content model. Include YAML front matter when the prompt maps to a known content type or route:

```yaml
---
type: docs
path: /docs/section/topic
---
```

Use `type: docs`, `blog`, `prompt`, or `image` as appropriate. Omit `path` only when the destination is intentionally undecided.

Write direct, reusable instructions. Define the following as needed:

- **Assignment:** the target content type, working title, destination, and expected length when useful.
- **Writer role and audience:** the expertise to bring and the readers the piece serves.
- **Purpose:** what readers should understand or be able to decide after reading.
- **Scope:** the subject boundaries, time horizon, and level of detail.
- **Structure:** a logical outline suited to the argument, rather than a generic list of headings.
- **Tone and style:** clear, precise, practical, and appropriate to the target page.
- **Constraints:** required evidence, exclusions, terminology, links, metadata, or other acceptance criteria.

For technical documentation, favor concept-first, neutral, evergreen reference material. Keep implementation steps, vendor details, predictions, and organizational commentary out unless the assignment needs them. For blog posts, allow a broader narrative and timely comparisons while keeping claims grounded and the audience and decision context explicit.

Build a coherent argument. “An AI-Assisted Content Creation Workflow: From Planning to Publication” is a useful example: it moves from the reader's problem to a clear working model, explains the roles and handoffs, then follows the process through review and publication. Treat its specific tools and workflow as that author's account, not as universal requirements for every article. Make distinctions between AI assistance and human responsibility clear when relevant. Ask the writer to verify factual and time-sensitive claims against reliable sources and to distinguish evidence from interpretation.

Keep the prompt scoped to the requested page. Do not create the final article unless asked. When writing Japanese prompts or localized content, follow the terminology and link-spacing guidance in the repository's root `AGENTS.md`.

## Image-generation prompts

Place English image-generation prompts in an `imagen/` subfolder under the matching prompt directory, and Japanese versions in `imagen.ja/`. Keep the image brief self-contained: the image model must be able to determine the intended message, composition, labels, relationships, and style from that prompt alone. Do not make a source article, diagram, reference image, or other file necessary to interpret it.

Use these five sections, in this order:

1. **Concept** — State the central message and the idea, comparison, process, relationship, or model the image should clarify.
2. **Layout** — Specify the aspect ratio and spatial arrangement, hierarchy, grouping, and reading direction. State how elements connect and where they belong. When structural fidelity matters, include a compact text or ASCII layout and explicitly identify required and forbidden connections, branches, and groupings.
3. **Visual cues** — Name the labels that must appear exactly, along with the shapes, symbols, arrows, contrasts, and other cues that map to the concepts. Specify which elements are alternatives, sequences, or converging paths. Do not rely on decorative imagery to explain relationships.
4. **Style** — Describe the intended visual character, typography, palette, contrast, density, and background. State practical legibility needs for the image's intended use.

5. **Restrictions** — Always include this section. State forbidden content and failure conditions explicitly, even when the brief seems straightforward. Tailor the list to the image; examples include extra stages, invented labels, misleading connections, product logos, unsupported metrics, tiny text, or decorative filler. If there are no additional topic-specific prohibitions, say so and retain any applicable baseline restrictions. Do not leave important prohibitions implicit.

Always state the required aspect ratio (such as 16:9 or 4:3). Pixel dimensions are approximate guidance only for tools that require them; the aspect ratio and composition take precedence. Give an exact image title when text must appear, and state required output format or intended use when relevant. Keep title, dimensions guidance, labels, terminology, layout, and relationships consistent across language variants unless the brief explicitly requires a difference.

Prefer one clear message per image. For a process, make sequence and direction unambiguous. For a comparison, show the comparison basis. For alternatives, distinguish them without implying that all are required. For diagrams with precise structure, define every required connection and any prohibited shortcut or branch; an image-generation prompt must not substitute visual approximation for an exact diagram when structural accuracy is essential.

## Review before saving

- Confirm the prompt names its deliverable and destination and follows nearby conventions.
- Check that audience, purpose, scope, structure, tone, and constraints are clear enough for independent execution.
- For image prompts, verify all five sections appear in the required order and that the brief is self-contained.
- Check all required labels, aspect ratio, approximate pixel guidance, relationships, and restrictions for consistency.
- Keep changes focused on the requested prompt and do not refer to contributor-specific paths or files outside the repository.
