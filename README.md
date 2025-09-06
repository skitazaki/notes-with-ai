# Notes with AI

_My Personal Notes on Software Engineering, Data, and AI, Enhanced by Artificial Intelligence_

**Notes with AI** is a collection of personal notes focused on **software engineering**, **data**, and **artificial
intelligence**, co-created with the help of artificial intelligence. Each note is a collaboration between human
curiosity and AI's capacity to organize, extend, and refine learnings, explorations, and experiments. This repository
serves as an open, evolving notebook — a space for reflection, sharing, and continuous learning.

**Purpose of Notes with AI**

- To organize and share knowledge in software engineering, data, and AI.
- To document personal growth and exploration in these fields.
- To create a living resource which evolves over time.

**Topics Covered**

- Software Architecture, Development Practices, Engineering Principles, and System Design
- Data Engineering, Analytics, Data Systems, and best practices for managing and leveraging data
- Machine Learning, Deep Learning, Generative AI, and applications of AI techniques

**How to Read These Notes**

They are not final answers, but starting points — prompts for further thinking, discussion, and creation. Each note is a
window into a moment of curiosity, made richer by technology but rooted in human perspective. Notes are collaboratively
created between human-driven exploration and AI assistance.

## Writers Guide

Run `hugo` development server on a local machine.

```bash
hugo server --minify --buildDrafts
```

Go to `http://localhost:1313/` with your web browser.

### Create a new page

Create a documentation page.

```bash
hugo new content/docs/data-analytics/data-management/index.md
```

Create a blog entry.

```bash
hugo new content/blog/webapp-directory-layout/index.md
```

Once you finish a writing, change `draft` value to `false` in front matter.

### Format Markdown files

This project uses `deno fmt` in order to format Markdown files. See
[Formatting with Deno fmt](https://docs.deno.com/examples/deno_fmt/) for getting started.

It runs `deno fmt --check` on GitHub Actions.

### Site Design

This site uses [Hextra](https://imfing.github.io/hextra/) theme. See the site to find configuration options and
shortcodes.

## Deploy on GitHub Pages

See the official document [Host on GitHub Pages](https://gohugo.io/host-and-deploy/host-on-github-pages/).
`.github/workflows/hugo.yaml` has configurations of build and deployment jobs.
