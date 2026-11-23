---
type: image
path: /docs/swe/ai-as-software-engineering-tool/harness-engineering
description: Harness-engineering cover organized as a clear work path, a runtime evidence loop, and a persistent coordination record.
---

# Image Prompt — Harness Engineering

## Concept

Create a clear editorial cover diagram titled **Harness Engineering**. Show one legible engineering loop and use the six responsibilities as supporting functions within that loop, not as six equal, disconnected boxes. Task framing and authoritative context prepare the work for the model. Tool authority governs which actions the model can request, and execution isolation contains where those actions take effect. Feedback and observability carry runtime results back to guide the model's next action. State and coordination persist the plan, results, ownership, and handoff across the loop. Human review receives evidence and sends review feedback into the next iteration.

## Layout

Use a **16:9** landscape composition, approximately 1536 × 864 pixels. Make the main work path the dominant visual, read from left to right. Arrange the canvas as a compact input area, one large Harness boundary, and a human review area:

1. **Inputs** — a small card with **Task** and **References**. These are incoming material, not responsibility categories.
2. **Harness** — the dominant center area with one clear outer boundary. Inside, draw a single top-level execution path: **Task** + **References** → **Task framing** + **Authoritative context** → **Model** → **Tool authority** → **Execution isolation** + **Bounded runtime**. Put Task framing and Authoritative context together in one grouped preparation area before the Model. Put Tool authority as a gate between the Model and runtime. Put Execution isolation as the boundary around the Bounded runtime, not as another step after the runtime.
3. **Human review** — a small area to the right with **Evidence** and a person reviewing it.

Place **Feedback and observability** as a return path from Bounded runtime results to the Model, visibly separate from the forward execution arrows. Place **State and coordination** as one quiet record strip along the bottom inside the Harness boundary. Beneath its label, show one small, single-line example: **Plan · Results · Owner · Handoff**. Keep the four terms as plain text in the same strip, not as separate boxes, icons, or process steps. Use only three short dotted connectors into that strip: from task framing, runtime results, and human review feedback. This strip represents persistent working state across the loop; it is not another execution stage.

Connect the columns and show one feedback cycle:

- Inputs → Task framing + Authoritative context: one clear forward arrow enters the grouped preparation area.
- Forward work path: preparation → Model → Tool authority → Bounded runtime. Show Execution isolation as a visible enclosure around the runtime; it is a boundary, not a sequential operation.
- Runtime → Evidence → Human review: show evidence as the observed result of runtime work, then send it to the reviewer.
- Feedback and observability: one return arrow carries runtime results back to the Model. Keep it visually distinct from the forward path.
- Human review → Harness: one separate curved return arrow labeled **Human feedback** enters Task framing, showing how review informs the next iteration.
- State and coordination: the three dotted connectors terminate at the bottom record strip. Do not connect this strip into the execution path or use it as a feedback arrow.

Use distinct, well-spaced connection points. Make arrow direction and the difference between forward work, runtime feedback, human review feedback, and state recording immediately clear. Keep connectors short and direct; do not cross arrows or route them through unrelated components. Leave generous whitespace around the main path.

## Visual cues

- Exact visible title: **Harness Engineering**. Use no subtitle.
- Use only these labels: **Inputs**, **Task**, **References**, **Harness**, **Task framing**, **Authoritative context**, **Tool authority**, **Execution isolation**, **Feedback and observability**, **State and coordination**, **Plan**, **Results**, **Owner**, **Handoff**, **Model**, **Bounded runtime**, **Evidence**, **Human review**, **Human feedback**.
- In the input card, place Task and References on separate rows with thin horizontal dividers. Do not show the input list as a substitute for harness responsibilities.
- Keep the six responsibilities in three functional groups: preparation (**Task framing**, **Authoritative context**), action control (**Tool authority**, **Execution isolation**), and learning and continuity (**Feedback and observability**, **State and coordination**). Group by function and position; do not make six same-sized peer cards.
- Use shape and connectors to distinguish the four relationships: forward execution, runtime feedback to the Model, human feedback to Task framing, and dotted recording links to State and coordination.
- Draw Execution isolation as a boundary around Bounded runtime. Tool authority is a gate before that boundary. Do not imply either one performs the other's role.
- Keep State and coordination as a persistent record strip spanning the work, not as a box in the process sequence.
- Show the four compact examples **Plan · Results · Owner · Handoff** on one line inside the record strip. Keep them visually secondary to the main work path.
- Make Human review the destination for Evidence. Keep the human feedback loop separate from the runtime feedback loop.

## Style

Use a restrained editorial infographic style for a professional engineering documentation site. Use a warm light background, dark navy typography and lines, with restrained teal and amber accents. Keep the center column dominant, the side columns compact, the outer boundary clear, and the labels readable at article width. Use simple icons only as secondary cues; let grouping and arrows explain the architecture.

## Restrictions

- Do not add labels beyond the list above.
- Do not depict six equal boxes, a row of unrelated responsibilities, or one image block for each article section.
- Do not draw Execution isolation as a step after Bounded runtime; it encloses the runtime.
- Do not mix the runtime feedback-to-Model loop with the human feedback-to-Task framing loop.
- Do not route State and coordination through the execution path or use it as an arrow destination for feedback.
- Do not turn Plan, Results, Owner, or Handoff into separate cards, stages, or connectors.
- Do not use crossing connectors, ambiguous arrowheads, decorative arrows, or unlabeled cycles.
- Do not merge Tool authority with Execution isolation, or omit any of the six responsibilities.
- Do not depict unrestricted filesystem, network, credential, or production access.
- No vendor names, logos, metrics, fake code, watermark, decorative circuitry, or extra workflow stages.
- Preserve the 16:9 ratio and maintain generous whitespace.
