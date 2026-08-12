---
type: docs
path: /docs/ai/context-engineering/agent-skills
---

# Task: Write a Notes with AI topic page on Agent Skills, SKILL.md, and Agent Plugins

Create a public-facing technical topic page for the **Notes with AI** documentation site.

The topic should explain the emerging standards and conventions for packaging reusable capabilities for AI agents, focusing on:

- **Agent Skills**
- **`SKILL.md`**
- **Agent Plugins**
- their relationship with **MCP (Model Context Protocol)**

The article should help a technically experienced reader understand not only what these concepts are, but **why they exist, how they fit together, and when to use each one**.

## Editorial goal

Treat this as a conceptual and architectural topic page, not merely a tutorial.

The central question should be:

> How do we package agent knowledge, workflows, tools, and supporting resources so that they can be reused and increasingly moved across agent environments?

Build the article around the idea that agent extensibility has several distinct layers:

1. **Instructions and procedural knowledge** — Agent Skills
2. **Skill definition and activation metadata** — `SKILL.md`
3. **Runtime tools and contextual connections** — MCP
4. **Portable packaging and composition** — Agent Plugins
5. **Discovery and distribution** — catalogs, registries, marketplaces, or client-specific mechanisms
6. **Trust and execution policy** — permissions, provenance, sandboxing, approval, and client policy

Make clear that these layers are complementary rather than competing abstractions.

---

# 1. Start with the problem

Begin with a concrete explanation of why agent capabilities need packaging.

A capable foundation model is not enough for reliable real-world work. Agents need reusable knowledge such as:

- organization-specific procedures;
- coding conventions;
- deployment workflows;
- document-generation rules;
- domain expertise;
- scripts;
- templates;
- reference documents;
- access to external systems.

Historically, much of this has been encoded in system prompts, project instructions, tool definitions, scripts, or vendor-specific extension mechanisms.

Explain the resulting problems:

- large prompts and context consumption;
- duplicated instructions;
- inconsistent execution;
- difficulty versioning procedural knowledge;
- vendor-specific packaging;
- poor portability between agent clients;
- difficulty combining instructions with executable capabilities.

Then introduce Agent Skills and Agent Plugins as attempts to establish reusable boundaries around these capabilities.

---

# 2. Agent Skills

Explain **Agent Skills** as an open format for packaging reusable procedural knowledge and supporting resources for AI agents.

Use the official Agent Skills specification as the primary source:

[https://agentskills.io/home](https://agentskills.io/home)

Cover:

- what an Agent Skill is;
- why a skill is represented as a directory rather than just a prompt;
- how skills make procedural knowledge reusable and versionable;
- how scripts, references, templates, and assets can accompany instructions;
- how skills differ from ordinary prompt files;
- why skills are useful for repeatable agent workflows.

Show a representative structure such as:

```text
my-skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Explain that `SKILL.md` is required while the supporting directories are optional.

## Progressive disclosure

Give special attention to the **progressive disclosure** model.

Explain the lifecycle:

```text
Discovery
   ↓
Activation
   ↓
Execution
```

Describe the distinction:

- during **discovery**, an agent can inspect lightweight metadata such as the skill name and description;
- during **activation**, the full `SKILL.md` instructions are loaded when the skill becomes relevant;
- during **execution**, additional scripts, references, or assets can be loaded or executed as required.

Explain why this matters for **context engineering**.

A system can expose many potential capabilities without loading every instruction and reference document into the model context at startup.

Connect this explicitly to concepts such as:

- context budgeting;
- lazy loading;
- capability discovery;
- task-specific context assembly.

---

# 3. Understanding `SKILL.md`

Create a dedicated section explaining `SKILL.md`.

Do not describe it simply as "a Markdown prompt."

Explain that it combines:

- metadata used for discovering and selecting the skill;
- instructions describing how the agent should perform the task;
- references to supporting resources.

Show a small illustrative example.

For example:

```markdown
---
name: deploy-service
description: Deploy a service safely and verify its health.
---

# Deploy Service

Follow the organization's deployment procedure.

1. Verify the current build.
2. Check deployment prerequisites.
3. Deploy the service.
4. Run health checks.
5. Roll back if validation fails.
```

Clearly mark examples as illustrative and ensure actual required fields and semantics match the current specification.

Discuss what belongs in `SKILL.md` versus what should live in:

- `references/`;
- `scripts/`;
- `assets/`.

Explain the design principle:

> Keep the operational instructions understandable to the agent while moving large, specialized, or executable material into supporting resources that can be loaded when needed.

Include practical guidance for writing good skills:

- define a narrow capability;
- write a description that makes activation conditions clear;
- specify expected inputs and outputs where useful;
- make procedures explicit;
- document failure paths and validation;
- avoid unnecessary context;
- prefer deterministic scripts for operations that should not depend on model improvisation;
- keep reference material separate when it is large;
- make the skill independently understandable.

---

# 4. Skills versus tools

Explain an important distinction:

**A skill tells an agent how to perform a task. A tool gives the agent an operation it can invoke.**

Use a concrete example.

For a deployment agent:

**Skill**

```text
Check deployment prerequisites
→ deploy
→ inspect health
→ decide whether rollback is necessary
```

**Tools**

```text
getDeploymentStatus()
deployService()
getHealthChecks()
rollbackDeployment()
```

Explain that skills encode **procedural knowledge and orchestration**, whereas tools expose **runtime capabilities**.

Also explain that the boundary is not absolute: a skill can contain scripts, but the architectural distinction remains useful.

---

# 5. Relationship with MCP

Introduce MCP only to establish the architecture.

Explain MCP as a runtime interoperability layer through which agents or AI applications can connect to external tools and contextual data.

Avoid turning this page into a full MCP tutorial.

Use a simple conceptual comparison:

| Layer         | Primary question                                                              |
| ------------- | ----------------------------------------------------------------------------- |
| Agent Skills  | What reusable instructions and procedural knowledge does the agent have?      |
| MCP           | What external tools and contextual resources can the agent access at runtime? |
| Agent Plugins | How can portable extension components be packaged together?                   |

Explain how a skill can instruct an agent to use capabilities supplied through an MCP server.

Example:

```text
Agent Skill
"How our organization deploys applications"
        │
        ▼
Agent
        │
        ▼
MCP
        │
        ▼
Deployment platform
```

---

# 6. Agent Plugins

Use these sources as primary references:

[https://agent-plugins.org/](https://agent-plugins.org/)

[https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins](https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins)

Explain the packaging problem that Agent Plugins addresses.

An organization may already have:

- one or more Agent Skills;
- MCP server configuration;
- scripts and supporting resources;
- client-specific integrations.

Without a common package boundary, distributing these capabilities between agent clients can require rearranging directories, rewriting manifests, or maintaining client-specific packages.

Explain **Agent Plugins 1.0** as a vendor-neutral package format intended to provide a predictable structure for portable agent extensions.

Make very clear:

> Agent Plugins does not replace Agent Skills or MCP.

Instead:

```text
Agent Skills
      │
      ├──────────┐
      │          │
      ▼          ▼
procedures    resources

MCP
 │
 ▼
runtime tools + context

        │
        ▼

Agent Plugin
┌─────────────────────────┐
│ plugin.json             │
│                         │
│ skills/                 │
│   └── .../SKILL.md      │
│                         │
│ mcp.json                │
│                         │
│ client-specific/        │
│ extensions              │
└─────────────────────────┘
```

Use the current Agent Plugins specification to verify the exact directory structure and terminology before publishing.

Show a representative plugin structure similar to:

```text
deployment-assistant/
├── plugin.json
├── skills/
│   └── deploy-service/
│       ├── SKILL.md
│       ├── scripts/
│       └── references/
├── mcp.json
└── <client-namespace>/
    └── ...
```

Explain the role of:

- `plugin.json`;
- `skills/`;
- `mcp.json`;
- namespaced client-specific extensions.

---

# 7. What Agent Plugins 1.0 deliberately does NOT standardize

This distinction is important.

Explain that a portable package format does not automatically solve the entire extension ecosystem.

Discuss areas intentionally outside or beyond the portable 1.0 contract, based on the current specification:

- installation experience;
- marketplaces and registries;
- permissions;
- approval flows;
- sandboxing;
- publisher identity;
- provenance;
- signatures;
- organizational trust policy;
- user interface;
- some client-specific extension types.

Explain why keeping the interoperability floor small can be beneficial.

Avoid implying that Agent Plugins makes all agent clients behave identically.

---

# 8. Architecture: how the pieces fit together

Create a compact architecture model.

Use a diagram, preferably Mermaid if compatible with the existing Notes with AI site.

Suggested conceptual structure:

```text
┌─────────────────────────────────────┐
│            Agent Client             │
│                                     │
│  ┌───────────────┐                  │
│  │ Agent Plugin  │                  │
│  │               │                  │
│  │ ┌───────────┐ │                  │
│  │ │   Skill   │ │                  │
│  │ │ SKILL.md  │ │                  │
│  │ └───────────┘ │                  │
│  │               │                  │
│  │ MCP config ──────────┐           │
│  └───────────────┘      │           │
│                         │           │
└─────────────────────────│───────────┘
                          │
                          ▼
                    ┌───────────┐
                    │MCP Server │
                    └─────┬─────┘
                          │
                          ▼
                    External System
```

Explain the responsibility of each boundary.

---

# 9. Use a running example

Use one consistent example throughout the article:

**Deployment Assistant**

The assistant needs to know:

- the organization's release procedure;
- prerequisite checks;
- validation requirements;
- rollback rules.

Those belong naturally in an Agent Skill.

It also needs live operations such as:

- query deployment status;
- deploy a version;
- inspect health;
- roll back.

Those can be provided through MCP.

Then package the Skill and MCP configuration as an Agent Plugin.

Use this example to make the progression intuitive:

```text
Knowledge
    ↓
Skill
    ↓
SKILL.md + resources

Runtime capability
    ↓
MCP

Portable distribution
    ↓
Agent Plugin
```

---

# 10. Compare the concepts

Include a concise comparison table with columns such as:

| Concept             | Purpose                               | Typical artifact            | Loaded/used when       | Portability role                |
| ------------------- | ------------------------------------- | --------------------------- | ---------------------- | ------------------------------- |
| Prompt/instructions | Immediate model guidance              | Markdown/text               | Context construction   | Usually application-specific    |
| Agent Skill         | Reusable procedural capability        | Skill directory             | When relevant          | Portable skill format           |
| `SKILL.md`          | Skill metadata + instructions         | Markdown file               | Discovery/activation   | Core Agent Skill artifact       |
| MCP                 | Runtime tools/context connectivity    | MCP server/config           | Runtime                | Protocol-level interoperability |
| Agent Plugin        | Package reusable extension components | Plugin directory + manifest | Installation/discovery | Package-level interoperability  |

Verify terminology against current specifications rather than blindly copying this table.

---

# 11. Explain the broader interoperability stack

End the architectural discussion with a layered model:

```text
┌─────────────────────────────┐
│ Discovery                   │
│ catalogs / registries       │
├─────────────────────────────┤
│ Packaging                   │
│ Agent Plugins               │
├─────────────────────────────┤
│ Procedural knowledge        │
│ Agent Skills / SKILL.md     │
├─────────────────────────────┤
│ Runtime interoperability    │
│ MCP                         │
├─────────────────────────────┤
│ External systems            │
│ APIs / DBs / SaaS / tools   │
└─────────────────────────────┘
```

Treat **trust and execution policy** as a cross-cutting concern rather than forcing it into one layer.

Explain that agent interoperability is not a single problem.

Different standards address different questions:

- How do we describe reusable procedures?
- How do we expose runtime tools?
- How do we package extensions?
- How do we discover packages?
- How do we decide what is trusted and allowed to execute?

This distinction should be one of the main takeaways of the article.

---

# 12. Portability and ecosystem

Discuss why these standards matter beyond individual implementations.

Cover:

- version-controlled agent capabilities;
- reusable organizational knowledge;
- portability across compatible agent clients;
- separation between procedure and runtime integration;
- composability;
- open specifications versus proprietary extension mechanisms.

Mention concrete products or clients only when their current support can be verified from authoritative documentation.

Because this ecosystem is evolving quickly, distinguish carefully between:

- standardized behavior;
- proposed behavior;
- experimental implementations;
- client-specific extensions.

Add dates or specification versions when doing so prevents ambiguity.

---

# 13. Security considerations

Include a short but meaningful security section.

Skills and plugins should not automatically be considered trustworthy merely because they follow an open format.

Discuss risks such as:

- malicious instructions;
- prompt injection embedded in references;
- executable scripts;
- MCP servers with powerful operations;
- excessive permissions;
- supply-chain attacks;
- untrusted plugin publishers.

Explain the separation between:

```text
Packaging ≠ Trust ≠ Permission ≠ Execution safety
```

Clients and organizations still need appropriate policies for approval, provenance, sandboxing, and runtime authorization.

---

# 14. Practical guidance

Provide a short decision guide.

Use a format such as:

**Use an Agent Skill when...**

You want to package reusable instructions, domain knowledge, workflows, scripts, references, or templates for an agent.

**Use MCP when...**

The agent needs standardized runtime access to external systems, tools, or contextual data.

**Use an Agent Plugin when...**

You want to distribute Skills and/or MCP configuration together through a predictable portable package boundary.

**Use client-specific extensions when...**

The required behavior is outside the current portable specification and intentionally depends on a particular agent environment.

---

# 15. Relationship to Notes with AI

Position this page within the broader documentation hierarchy.

Suggested relationships:

```text
AI
└── AI Agents
    ├── Agent Architecture
    ├── Context Engineering
    ├── Agent Skills        ← this topic
    ├── Tool Use
    │   └── MCP
    ├── Agent Interoperability
    └── Agent Security
```

Treat Agent Skills as both:

- an **agent capability** topic;
- a **context engineering** mechanism;
- part of the emerging **agent interoperability** ecosystem.

Add appropriate cross-links if those pages already exist in the repository. Do not invent links to pages that do not exist.

---

# Writing style

Follow the existing **Notes with AI** style and repository conventions.

The article should be:

- technically precise;
- architecture-oriented;
- vendor-neutral;
- explanatory rather than promotional;
- accessible to software architects and experienced developers who may be new to agent standards;
- concise enough to serve as a topic page rather than an exhaustive specification.

Prefer diagrams, small examples, and comparison tables over long prose when they communicate the idea more effectively.

Define terminology before using it heavily.

Avoid hype such as "revolutionary," "game-changing," or claims that a standard has become universal unless there is evidence.

---

# Research requirements

Before writing, inspect the latest versions of these sources:

1. Agent Skills
   [https://agentskills.io/home](https://agentskills.io/home)

2. Agent Plugins
   [https://agent-plugins.org/](https://agent-plugins.org/)

3. AAIF — From Skills and Tools to Portable Agent Plugins
   [https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins](https://aaif.io/blog/from-skills-and-tools-to-portable-agent-plugins)

Also consult authoritative documentation for MCP and relevant agent clients when necessary.

Prefer:

1. specifications;
2. official project documentation;
3. official implementation documentation;
4. project announcements.

Use secondary sources only for context.

Because Agent Plugins is new and evolving, verify all statements about version numbers, supported components, compatible clients, directory layouts, and interoperability immediately before writing.

---

# Implementation instructions for Codex

Before editing:

1. Inspect the Notes with AI repository structure.
2. Find existing AI-agent, context-engineering, MCP, or related pages.
3. Determine the appropriate location for this topic.
4. Inspect nearby Markdown files to infer front matter, headings, shortcodes, diagram conventions, citations, and cross-link style.
5. Reuse existing conventions rather than introducing a new documentation pattern.

Then:

1. create or update the appropriate topic page;
2. add useful cross-links to existing related topics;
3. add the architecture diagram;
4. ensure examples render correctly under Hugo;
5. run the site's available formatting/build/link checks;
6. fix issues introduced by the change.

Do not broadly reorganize the documentation tree as part of this task.

If the repository already has a taxonomy or metadata mechanism for multidimensional navigation, add appropriate metadata for concepts such as:

- AI Agents
- Context Engineering
- Agent Interoperability
- Agent Skills
- MCP

Keep the physical file hierarchy simple; use metadata and cross-links for these secondary relationships where supported.

---

# Desired reader takeaway

After reading the page, the reader should be able to explain the following model:

> **Agent Skills package reusable procedural knowledge. `SKILL.md` is the core artifact that describes and instructs the skill. MCP provides standardized runtime access to tools and context. Agent Plugins provide a portable package boundary that can carry Skills and MCP configuration together.**

The reader should also understand that **discovery, distribution, trust, permissions, and runtime policy are related but separate problems**, and should not assume that Agent Plugins solves all of them.
