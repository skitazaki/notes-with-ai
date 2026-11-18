---
type: image
path: /docs/swe/ai-as-software-engineering-tool/harness-engineering
description: Three-column harness-engineering cover showing task inputs entering a central harness, evidence reaching human review, and review feedback returning to the harness.
---

# Image Prompt — Harness Engineering

## Concept

Create a clear editorial cover diagram titled **Harness Engineering**. Explain the harness at a glance as the controlled system between incoming engineering context and human review. The central harness prepares information for a model, governs the model's tool use, and contains execution. Evidence goes to a person; the person's review feeds the next iteration.

## Layout

Use a **16:9** landscape composition, approximately 1536 × 864 pixels. Organize the canvas into three broad vertical columns, read from left to right:

1. **Inputs** — a compact card with three clearly separated rows: **Task**, **References**, **Skill library**.
2. **Harness** — the widest and visually dominant center column, enclosed by one clear boundary. Inside, show a compact path: **Prepared instructions / context / skills** → **Model** → **Governed tool access** → **Bounded runtime**. Keep the prepared information as one grouped component with three separated rows, not three boxes. Keep tool access and runtime as distinct boxes.
3. **Human review** — a compact right column containing **Evidence** and a person reviewing it.

Connect the columns and show one feedback cycle:

- Inputs → Harness: the arrow from the input card terminates at the Harness boundary. Do not aim it at the prepared-information component.
- Inside Harness: prepared instructions/context/skills → Model → Governed tool access → Bounded runtime.
- Harness → Evidence → Human review: the output arrow leaves from the Harness boundary, not directly from an interior box.
- Human review → Harness: one curved return arrow runs beneath the three columns and enters the Harness boundary, showing that review informs the next iteration. Label this return path **Feedback**.

Use distinct, well-spaced boundary connection points for incoming context, outgoing evidence, and returning feedback. Keep every connector clear of the title, boxes, and other arrows. The feedback arc should be visually easy to follow without enclosing or crossing the main diagram.

## Visual cues

- Exact visible title: **Harness Engineering**. Use no subtitle.
- Use only these labels: **Inputs**, **Task**, **References**, **Skill library**, **Harness**, **Prepared instructions**, **Context**, **Skills**, **Model**, **Governed tool access**, **Bounded runtime**, **Evidence**, **Human review**, **Feedback**.
- In the input card, place Task, References, and Skill library on separate rows with thin horizontal dividers. In the prepared-information component, place Prepared instructions, Context, and Skills on separate rows with the same divider treatment. Use one shared outer card for each group; do not enclose rows separately.
- Show Skills as reusable instructions and resources that guide the Model. Do not depict them as executable tools or as permission grants.
- Use a visible outer frame to identify the Harness as the center system. The frame should make the three boundary connections legible: input enters, evidence exits, and human feedback returns.
- Keep **Governed tool access** distinct from **Bounded runtime**: the first controls which operations the model may request; the second defines where their effects occur.
- Make Human review the output point and the source of the return feedback loop.

## Style

Use a restrained editorial infographic style for a professional engineering documentation site. Use a warm light background, dark navy typography and lines, with restrained teal and amber accents. Keep the center column dominant, the side columns compact, the outer boundary clear, and the labels readable at article width. Use simple icons only as secondary cues; let grouping and arrows explain the architecture.

## Restrictions

- Do not add boxes or labels beyond the list above.
- Do not create a process waterfall: the three columns are input, controlled system, and review, with one feedback return.
- Do not connect the input arrow directly to Prepared instructions, Context, or Skills; it connects to the Harness boundary.
- Do not route evidence directly from an interior component to Human review; the output leaves from the Harness boundary.
- Do not omit or redirect the Human review → Feedback → Harness return cycle.
- Do not merge Governed tool access with Bounded runtime.
- Do not depict unrestricted filesystem, network, credential, or production access.
- No vendor names, logos, metrics, fake code, watermark, decorative circuitry, or extra workflow stages.
- Preserve the 16:9 ratio and maintain generous whitespace.
