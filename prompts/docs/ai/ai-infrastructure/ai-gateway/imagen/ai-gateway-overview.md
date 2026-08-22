---
type: image
path: /docs/ai/ai-infrastructure/ai-gateway
description: Conceptual overview of the AI Gateway as an infrastructure boundary across applications, models, tools, data, and agents.
---

# AI Gateway — Cover Image Generation Brief

## Purpose

Create a clean **editorial technical illustration** for the Notes with AI topic page **AI Gateway**.

The image should communicate that an AI Gateway is **not simply the next step in a linear progression**:

> API Gateway → LLM Gateway → AI Gateway

Instead, show the AI Gateway as an **expanding infrastructure boundary** that brings together concerns from traditional API traffic, LLM/model traffic, and emerging agentic communication.

The central idea is:

> **AI Gateway = a programmable connectivity, policy, routing, and observability boundary across APIs, models, tools, and agents.**

## Primary Visual Concept

Place a large **AI Gateway** element at the center.

Arrange four major infrastructure domains around it:

- **Applications & APIs** — left
- **Models** — upper right
- **Tools & Data** — lower right
- **Agents** — top

Connect each domain to the central AI Gateway.

The composition should feel **multi-directional and network-like**, not like a left-to-right timeline.

Conceptually:

```text
                         AGENTS
                           │
                          A2A
                           │
                           ▼
                   ┌──────────────┐
                   │              │
APPLICATIONS ─────▶│  AI GATEWAY  │────▶ MODELS
& APIs             │              │
 HTTP / gRPC       └──────┬───────┘
                          │
                         MCP
                          │
                          ▼
                    TOOLS & DATA
```

This is conceptual guidance, not a requirement to reproduce the diagram literally.

## Show Expanding Scope

Around or behind the central gateway, subtly communicate **overlapping areas of responsibility**:

### API gateway concerns

- HTTP/API traffic
- authentication
- rate limiting
- routing

### LLM gateway concerns

- model routing
- tokens and cost
- fallback
- model policies

### Agentic gateway concerns

- MCP
- A2A
- tools
- agent authorization

Do **not** depict these as three boxes connected sequentially by arrows.

Instead, use overlapping zones, arcs, layers, or subtle visual groupings to suggest that these concerns **converge at the gateway**.

The image should convey:

**expanding scope, not replacement.**

## Central Gateway Responsibilities

Associate the central AI Gateway with four concise concepts:

**Connectivity · Policy · Routing · Observability**

These can appear as small labels inside or immediately around the gateway.

Do not overload the image with feature lists.

## Protocol Semantics

Be architecturally precise about protocols.

Use:

- **HTTP / gRPC** on connections involving conventional applications and APIs
- **MCP** primarily between the gateway and tools/data
- **A2A** on agent-to-agent or agent-oriented communication
- model/inference connections may be shown without forcing a protocol label

MCP and A2A should visually appear as **communication protocols**, not as infrastructure destinations equivalent to Models, Agents, or Tools.

## Visual Hierarchy

The viewer should perceive, in this order:

1. **AI Gateway**
2. four connected domains: Applications/APIs, Models, Tools/Data, Agents
3. Connectivity / Policy / Routing / Observability
4. HTTP/gRPC, MCP, and A2A protocol labels
5. subtle indication of API-gateway, LLM-gateway, and agentic-gateway concerns

Avoid making every label equally prominent.

## Suggested Heading

Use:

# AI Gateway

Optional small subtitle:

**The expanding boundary of AI infrastructure**

Do **not** use “Evolution of the Gateway,” because that reinforces a chronological interpretation.

## Visual Style

Match a modern technical-documentation aesthetic:

- clean editorial infographic
- architectural rather than futuristic
- light background
- restrained palette
- thin, precise connector lines
- geometric shapes
- generous whitespace
- crisp sans-serif typography
- subtle depth only where useful
- visually balanced
- professional cloud/platform architecture feel

The image should feel appropriate for an engineering documentation hub rather than a marketing landing page.

## Avoid

Do not include:

- a linear `API Gateway → LLM Gateway → AI Gateway` progression
- robots or humanoid AI imagery
- glowing brains
- generic neural-network imagery
- excessive cloud icons
- 3D server racks
- cyberpunk aesthetics
- decorative circuitry
- giant feature lists
- vendor logos
- product names
- a visually dominant MCP logo
- arrows that imply all traffic flows in only one direction

Do not imply that an AI Gateway completely replaces API gateways or service meshes.

## Composition

Prefer a **wide landscape composition**, suitable as a documentation article cover.

Keep important content away from the extreme edges to allow responsive cropping.

The central AI Gateway should occupy roughly **25–30% of the visual emphasis**, with the surrounding domains creating a balanced topology around it.

The result should remain understandable when displayed at relatively small size.

## Core Message

A reader should understand the image even without reading the article:

> **AI Gateway is the infrastructure boundary where API, model, tool, and agent communication increasingly converge — expanding the gateway's scope rather than simply replacing previous gateway generations.**
