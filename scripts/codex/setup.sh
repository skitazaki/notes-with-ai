#!/bin/sh

set -eu

ROOT=$(git rev-parse --show-toplevel)
mkdir -p "$ROOT/.codex-runtime"

cd "$ROOT"
CI=true pnpm install --frozen-lockfile
exec "$ROOT/scripts/codex/server.sh"
