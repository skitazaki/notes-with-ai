---
type: blog
path: /blog/ai-assisted-content-workflow
---

# Writing Brief: AI-Assisted Content Creation Workflow for Notes with AI

## Assignment

Write a practical blog article explaining how Notes with AI uses ChatGPT, Codex, and GitHub Copilot to plan, write, illustrate, review, and publish content.

The article should describe the actual working model, clarify each tool's primary responsibilities, and explain how written content and visual assets move through the workflow.

Working title:

**An AI-Assisted Content Creation Workflow: From Planning to Publication**

## Writer Role

You are a senior technical writer and AI-assisted software development practitioner. Write from the perspective of someone documenting a real content-production workflow for a technical knowledge site.

Be precise about tool responsibilities, deliverables, handoffs, and quality controls. Distinguish established practices from optional approaches.

## Audience

- Software engineers and technical practitioners who maintain a personal technical blog or knowledge site.
- Writers exploring AI-assisted content creation.
- Developers who want to combine coding agents, writing assistants, and image-generation tools in a repeatable workflow.

Assume readers understand Markdown and Git at a basic level, but do not assume they already use all three AI tools.

## Purpose

Help readers understand:

1. How the three AI tools complement one another.
2. How an article moves from an initial idea to a published page.
3. How image generation and Mermaid-based diagrams fit into a workflow for figure-rich content.
4. Why clear briefs, explicit deliverables, and human review remain important when using multiple AI tools.
5. How a repository-based workflow makes content and visual assets maintainable.

The article should provide a reusable mental model for building content that is richer with diagrams and illustrations when they materially improve comprehension, rather than treating visual assets as optional decoration.

## Context: Notes with AI

Notes with AI is a knowledge site built from Markdown content and published as a static HTML site. Hugo is one example of a static site generator that converts Markdown into browsable pages, and this repository follows that pattern for technical documentation and blog posts covering software engineering, data, and AI.

The repository separates content from the prompts used to produce it:

- `prompts/blog/` contains blog-writing briefs.
- `content/blog/` contains blog posts.
- Japanese localized pages use the `.ja.md` suffix where applicable.
- Image-generation briefs follow the repository's dedicated `imagen/` and `imagen.ja/` directory conventions.
- Content and assets are maintained in Git and published through the site's existing build and deployment workflow.

Inspect the repository's `AGENTS.md`, relevant existing prompts, representative blog posts, and image instructions before writing. Follow the current repository conventions rather than assuming that every example in this brief matches the implementation exactly.

## Tool Responsibilities

Explain the following division of responsibilities. These are primary roles, not exclusive capabilities.

### ChatGPT: Planning, Review, and Image Generation

ChatGPT is primarily used for:

- Exploring and refining article ideas as part of an ongoing content cycle.
- Planning the article's scope, structure, and narrative in a way that can be revisited and adjusted as the work evolves.
- Preparing briefs and prompts for subsequent work.
- Generating images when a visual asset is needed.
- Helping decide whether an idea is best communicated through an illustration, a conceptual image, or a structured diagram.
- Reviewing changes over time, including by examining Git history and recent diffs to identify where content, structure, or clarity could be improved.
- Providing periodic improvement suggestions, such as when the repository has new commits and the content can be revisited for sharper framing, clearer logic, or better narrative flow.

Emphasize that planning is not a one-off kickoff activity but a recurring part of the workflow, and that the starting point may come from a human writer, an AI assistant, or a conversation between the two.

### Codex: Writing and Repository-Oriented Work

Codex is primarily responsible for writing the article and working with the repository's files.

Its work may include:

- Turning a brief into a structured article draft.
- Writing or revising Markdown content.
- Creating image-generation prompts and, when appropriate, generating images as part of the task.
- Preparing Mermaid diagrams when a process, architecture, or set of relationships needs to be represented precisely.
- Integrating visual assets into the article.
- Checking links, metadata, paths, and consistency with repository conventions.

This workflow is designed for content that benefits from visual explanation. Not every article needs a figure, but when an article needs a diagram, illustration, or process map, Codex can carry that work through the repository in a structured way rather than treating it as an afterthought.

### GitHub Copilot: Writing Assistance and Review

GitHub Copilot supports article writing and review.

Describe its role in terms of:

- Improving clarity, readability, structure, and wording.
- Identifying gaps, inconsistencies, and potentially confusing explanations.
- Reviewing technical claims and examples that need further verification.
- Suggesting focused revisions to a draft.

Present Copilot as a supporting writing and review tool, not as an automatic source of truth. Any substantive technical claims should be checked against reliable evidence.

Do not invent a specific integration, automation, or handoff between Copilot and Codex. Explain the collaboration at the workflow level unless the repository provides evidence of a more specific implementation.

## Scope

Cover the end-to-end process in these stages.

### 1. Idea and Editorial Planning

Explain how an initial idea is refined into a clear article purpose, intended audience, scope, and proposed structure.

Describe how ChatGPT helps turn a broad topic into a usable editorial plan and a brief that another tool can execute.

Identify the brief as an important handoff artifact between planning and implementation.

### 2. Brief-Driven Article Writing

Explain how Codex uses the brief to produce a Markdown draft in the repository.

Cover the importance of defining:

- The target reader and desired outcome.
- The article's central message.
- The section outline.
- Required examples and supporting material.
- Explicit scope boundaries and exclusions.

Explain that the brief constrains the writing task and reduces unnecessary improvisation. Codex should follow repository instructions and existing content conventions rather than treating the brief as the only source of requirements.

### 3. Visual Planning and Prompt Design

Explain why images and diagrams should be planned around the article's message instead of being added as decoration. This is a workflow for content that aims to communicate clearly through visuals, not simply a fallback for text-only posts.

Describe how an image prompt specifies the concept, composition, hierarchy, relationships, required labels, style, and output dimensions.

For image-generation prompts, follow the repository's four-part structure:

1. Concept
2. Layout
3. Visual cues
4. Style

Explain that a good prompt should be self-contained and sufficiently precise for an image-generation model to execute without guessing important relationships or text, especially when the article depends on the figure to carry part of the explanation.

### 4. Visual Production: Two Complementary Paths

Present two approaches and explain when each is useful. Frame the workflow as one that supports richly illustrated content when a concept is clearer with a visual aid, while still recognizing that the article's message is primary and the figure is a means of communicating it.

**Path A — AI-generated images**

Use an image-generation service when the article benefits from a conceptual illustration, editorial image, or visual metaphor.

ChatGPT may generate the image, or Codex may incorporate image generation into its work when appropriate.

Describe the general sequence:

1. Determine the image's purpose.
2. Create a self-contained image prompt.
3. Generate the image with a suitable AI tool.
4. Review the result for relevance, legibility, and unintended content.
5. Prepare the approved asset for the site.

**Path B — Mermaid diagrams rendered as images**

Use Mermaid when the content requires explicit, structurally accurate relationships, such as a workflow, sequence, architecture, or decision process.

Describe the general sequence:

1. Define the nodes, connections, and direction of the diagram.
2. Create the Mermaid source.
3. Validate the diagram's logic and rendering.
4. Render it to an image when the article or presentation requires a static visual.
5. Review labels, layout, and legibility before integration.

Do not suggest that image generation is a reliable substitute for a structurally precise diagram. Choose the method according to the information the visual must communicate.

### 5. Article Integration

Explain how the selected visual asset becomes part of the Markdown article.

Cover:

- Keeping assets in an appropriate repository-relative location.
- Using descriptive filenames.
- Converting display images to WebP before committing them, in accordance with repository conventions.
- Embedding images with meaningful alternative text.
- Providing concise descriptive titles where supported by the site's content model.
- Keeping image labels, titles, and alternative text consistent with the article.
- Localizing titles and alternative text for Japanese pages.

Explain that a visual asset is not complete merely because it has been generated; it must be usable, accessible, and correctly integrated into the site.

### 6. Writing Review and Revision

Explain how GitHub Copilot supports writing and review, while Codex can make repository-level revisions.

Review should consider:

- Accuracy and evidence for technical claims.
- Logical flow and completeness.
- Clear distinctions between actual practice and optional alternatives.
- Consistency between the prose, diagrams, and illustrations.
- Readability and unnecessary repetition.
- Correct Markdown, links, metadata, and asset references.

Human judgment remains responsible for accepting changes and resolving substantive questions. Avoid portraying AI review as a guarantee of correctness.

### 7. Repository Validation and Publication

Describe the repository-based lifecycle at a high level:

1. Save the article and required assets in the appropriate locations.
2. Review the changes in Git.
3. Run the checks and formatting tools prescribed by the repository.
4. Verify the rendered Hugo page, including images and links.
5. Use the repository's established branch and pull-request process.
6. Publish through the existing GitHub Actions and GitHub Pages workflow after the required checks and review.

Inspect the current repository configuration before naming exact commands or describing deployment triggers. Do not invent commands, workflows, approval gates, or automation steps.

### 8. Continuous Improvement

Conclude by explaining that the workflow is iterative.

Feedback from writing review, rendered-page inspection, and reader response can inform subsequent articles and improve future briefs.

Avoid claiming that the site currently tracks particular analytics or quality metrics unless this is verified in the repository or explicitly established by the author.

## Recommended Article Structure

1. Introduction: Why use multiple AI tools for content creation?
2. The Three Tools and Their Primary Responsibilities
3. The End-to-End Workflow
4. Planning and Brief-Driven Writing
5. Image Generation and Mermaid Diagrams
6. Review, Repository Integration, and Publication
7. What Makes the Workflow Effective
8. Conclusion: A Repeatable, Human-Directed Process

Include a concise workflow diagram if it improves the explanation. A Mermaid diagram is preferred when the objective is to show precise stages, handoffs, and optional branches.

The diagram should distinguish the main path from optional image-production paths and show where review and publication occur. Keep the diagram readable rather than trying to represent every detail.

## Tone and Style

- Practical, neutral, and technically credible.
- Clear enough for readers who are new to multi-tool AI workflows.
- Written in a first-person plural voice where appropriate, such as describing how "we use" the tools.
- Specific about responsibilities and deliverables.
- Focused on lessons learned and reusable principles rather than product promotion.
- Avoid hype, exaggerated productivity claims, and unsupported comparisons between AI products.
- Explain tool names and specialized terminology when first introduced.
- Use headings, concise paragraphs, and lists where they improve scanability.

## Constraints and Accuracy Requirements

- Treat the tool-role assignments in this brief as the author's stated working model.
- Do not imply that each tool has an exclusive capability; explain its primary role in this workflow.
- Do not invent specific prompts, integrations, API calls, automated handoffs, or internal practices.
- Do not claim that every article follows every stage or requires image generation; instead, present the workflow as a repeatable way to create figure-rich content when the subject benefits from it.
- Distinguish conceptual images from diagrams that require structural precision.
- Do not claim that generated images are automatically correct or that AI reviews guarantee factual accuracy.
- Verify repository-specific paths, scripts, build steps, and deployment details before documenting them.
- If an operational detail cannot be verified, describe it at a higher level or mark it for author confirmation rather than guessing.
- Keep the article focused on the content-production workflow, not a general comparison of ChatGPT, Codex, and GitHub Copilot.
- Do not modify unrelated content or repository configuration as part of writing this article.

## Deliverable

Create the English article at the appropriate location under `content/blog/`, following the existing Hugo content conventions.

Before writing, inspect the repository instructions and representative content. Then draft the article, prepare any necessary diagram or image prompt, and integrate the visual assets only if they materially improve the article.

Ensure the article distinguishes the primary workflow from optional visual-production branches.

Run the relevant repository checks where available and report what was verified, what remains unverified, and whether any generated assets were included.

Do not create the Japanese localized article as part of this task unless explicitly requested. A Japanese translation should be a separate stage after the English source is stable.
