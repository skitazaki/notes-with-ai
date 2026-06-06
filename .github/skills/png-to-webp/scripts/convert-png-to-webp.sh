#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <source.png> [destination.webp]" >&2
  exit 1
fi

src="$1"

if [[ ! -f "$src" ]]; then
  echo "Source file not found: $src" >&2
  exit 1
fi

ext="${src##*.}"
if [[ "${ext,,}" != "png" ]]; then
  echo "Source file must be a .png: $src" >&2
  exit 1
fi

if [[ $# -eq 2 ]]; then
  dest="$2"
  if [[ "${dest##*.}" != "webp" ]]; then
    echo "Destination file must be a .webp: $dest" >&2
    exit 1
  fi
else
  dest="${src%.*}.webp"
fi

dest_dir="$(dirname "$dest")"

if [[ ! -d "$dest_dir" ]]; then
  echo "Destination directory not found: $dest_dir" >&2
  exit 1
fi

if command -v magick >/dev/null 2>&1; then
  magick "$src" "$dest"
elif command -v cwebp >/dev/null 2>&1; then
  cwebp -quiet "$src" -o "$dest"
elif command -v ffmpeg >/dev/null 2>&1; then
  ffmpeg -y -i "$src" "$dest" >/dev/null 2>&1
elif command -v pnpm >/dev/null 2>&1; then
  pnpm dlx sharp-cli -i "$src" -o "$dest" --format webp
else
  echo "No supported PNG to WebP converter found. Install ImageMagick, cwebp, ffmpeg, or pnpm." >&2
  exit 1
fi

if [[ ! -f "$dest" ]]; then
  echo "Conversion did not produce output: $dest" >&2
  exit 1
fi

echo "Created $dest"