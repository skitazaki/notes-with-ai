---
name: png-to-webp
description: "Convert PNG images to WebP format for documentation and web pages. Use when creating smaller image assets, replacing PNG references, or generating colocated .webp files from existing .png files in this repository."
argument-hint: "source PNG path and optional destination WebP path"
user-invocable: true
---

# PNG to WebP

Convert a PNG image to WebP and keep the result beside the source file or at an explicitly provided destination.

## When to Use

- A page or document should reference a `.webp` image instead of a `.png`
- A colocated WebP asset is needed for a Hugo content page
- A smaller web-friendly image format is needed without manually testing tools

## Procedure

1. Confirm the source `.png` file exists.
2. Choose the destination path.
3. Run the helper script: [convert-png-to-webp.sh](./scripts/convert-png-to-webp.sh)
4. Prefer colocating the `.webp` beside the source image unless the task requires another path.
5. If the page already references the `.png`, update the Markdown to point to the `.webp` file.
6. Validate the result by confirming the output file exists and, when relevant, by running a focused Hugo build.

## Notes

- The helper script tries local conversion tools in a practical order.
- It prefers `magick`, then `cwebp`, then `ffmpeg`, then a temporary `pnpm dlx sharp-cli` fallback.
- On this repository's macOS environment, `sips` can read WebP metadata but may not be able to write WebP output, so it is not used as a primary conversion path.

## Examples

Convert beside the source file:

```bash
bash ./.github/skills/png-to-webp/scripts/convert-png-to-webp.sh content/docs/data/management/data-quality-dimensions/data-quality-dimensions-ChatGPT.png
```

Convert to an explicit destination:

```bash
bash ./.github/skills/png-to-webp/scripts/convert-png-to-webp.sh source/image.png output/image.webp
```
