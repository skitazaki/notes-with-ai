---
type: image
description: A delegated-authorization flow for an AI agent, distinguishing the executing principal from the delegated subject, with enforcement, policy decisions, bounded authority, and audit evidence.
---

# Image Generation Prompt — AI Agents & Autonomous Authorization

Create a polished 1536 × 1024 pixel technical illustration titled **AI Agents & Autonomous Authorization**.

## Purpose

Create a self-contained technical illustration that explains delegated authorization for an AI agent. It must stand on its own without relying on another image, document, system diagram, or source material. Show that an AI agent is an executing principal with constrained delegated authority, not a user interface with the user's unrestricted permissions. Clearly distinguish the agent's live identity from the human or business subject whose delegation and entitlements are evaluated.

## Mandatory layout

Follow this layout exactly. Use one main vertical decision path; do not interpret it as a collection of independent actor cards.

```text
User / Delegator
       │
       ▼
AI Agent
       │
       ▼
Policy Enforcement Point (PEP)
       │
       ▼
┌────────────────────────────────────────────────────┐
│ Policy Decision Point (PDP)                          │
│                                                      │
│ Authorization input panel:                           │
│ Principal: agent identity                            │
│ Subject: delegating user or business owner           │
│ Task scope                                           │
│ Resource & action                                    │
│                                                      │
│ [Execution Context]       [Delegation Context]       │
│                                                      │
│ Policy, approvals, expiry, tool scope                │
└────────────────────────────────────────────────────┘
       │
       ▼
   ◇ Allow? ◇
      │       │
   Allow     Deny
      │       │
      ▼       ▼
Tool /     Deny and log
Target System    │
      │          │
      └────┬─────┘
           ▼
       Audit Log
```

At the top, **User / Delegator** grants **Bounded delegation** to **AI Agent**. Represent task scope, expiry, and approved tools only with compact visual cues inside the delegation token; do not add labels for those concepts.

The agent requests a tool action with its own credential. **Policy Enforcement Point (PEP) is not a policy-decision node.** It does not decide Allow or Deny. It only intercepts the request, forwards it to the PDP, and enforces the PDP result. Draw no deny icon, deny label, deny branch, or other side path from the PEP.

Make the PDP the central focal point. Put Principal, Subject, Task scope, and Resource & action together as four separate rows in one shared **authorization input panel** inside the PDP. Principal and Subject are distinct authorization attributes, not separate actor cards. Do not duplicate Task scope or Resource & action in any other card.

Place **Execution Context** and **Delegation Context** as two small supporting cards inside the PDP beneath the single authorization input panel. Visually associate Execution Context with Principal and Delegation Context with Subject, but do not draw them as independent inputs flowing into the PDP.

The only Allow/Deny split begins at **Allow?**, after the PDP. Deny must go directly and only to **Deny and log**. Allow must go directly to **Tool / Target System**. Both outcomes then converge at **Audit Log**.

The phrase “authorization input panel” is a layout instruction only; do not render it as text in the image.

## Visual hierarchy and style

- Treat the PDP and the principal-versus-subject distinction as the central insight.
- Use a clean flat-vector editorial style, not a user-interface screenshot.
- Use a warm off-white background, dark navy typography and outlines, restrained blue and teal surfaces, and one muted amber or coral accent only for the decision state.
- Use consistent rounded cards, solid connectors, uniform line weight, minimal supporting icons, and ample whitespace.
- Make bounded delegation visually clear without turning the image into a cryptography diagram.
- Keep all labels legible at standard reading size; arrows must be easy to trace and must not cross.
- Keep the visual vendor-neutral: no logos, cloud-provider branding, product interfaces, or named standards.
- Output 1536 × 1024 pixels, 3:2 landscape, as a high-quality raster suitable for conversion to WebP.

## Required text

Use only these exact labels:

- **AI Agents & Autonomous Authorization**
- **User / Delegator**
- **AI Agent**
- **Bounded delegation**
- **Policy Enforcement Point (PEP)**
- **Policy Decision Point (PDP)**
- **Principal: agent identity**
- **Subject: delegating user or business owner**
- **Execution Context**
- **Delegation Context**
- **Task scope**
- **Resource & action**
- **Policy, approvals, expiry, tool scope**
- **Allow?**
- **Allow**
- **Deny**
- **Tool / Target System**
- **Deny and log**
- **Audit Log**

Do not add a subtitle, explanatory paragraph, acronym expansion beyond these labels, product name, standard name, or other text.

## Do not

- Do not imply that the AI agent is identical to the user or inherits unrestricted user permissions.
- Do not show Principal and Subject as two independent actor cards or as two separate input panels; keep them as separate rows within one authorization input panel.
- Do not draw a direct AI-agent-to-tool path that bypasses the PEP and PDP.
- Do not draw an Allow or Deny decision, a deny icon, or a deny branch from the PEP.
- Do not make only allowed actions auditable; denied actions must also reach the audit log.
- Do not turn this into a threat catalog, approval workflow, role matrix, system architecture map, or multi-agent orchestration diagram.
- Do not use tiny text, long captions, crossed connectors, dotted lines, excessive arrows, glossy 3D, photorealistic people, cyberpunk styling, logos, watermarks, or interface screenshots.
