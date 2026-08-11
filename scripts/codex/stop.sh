#!/bin/sh

set -eu

ROOT=$(git rev-parse --show-toplevel)
RUNTIME="$ROOT/.codex-runtime"
PID_FILE="$RUNTIME/hugo.pid"
PORT_FILE="$RUNTIME/hugo.port"

if [ ! -f "$PID_FILE" ] || [ ! -f "$PORT_FILE" ]; then
  printf 'No Hugo server is recorded for this worktree.\n'
  exit 0
fi

pid=$(cat "$PID_FILE")
port=$(cat "$PORT_FILE")
command=$(ps -p "$pid" -o command= 2>/dev/null || true)

case "$command" in
  *hugo*server*"--port $port"*"--source $ROOT"*)
    kill "$pid"
    attempts=0
    while kill -0 "$pid" 2>/dev/null && [ "$attempts" -lt 20 ]; do
      sleep 0.25
      attempts=$((attempts + 1))
    done
    if kill -0 "$pid" 2>/dev/null; then
      printf 'Hugo server %s did not stop; leaving its runtime files intact.\n' "$pid" >&2
      exit 1
    fi
    rm -f "$PID_FILE"
    printf 'Stopped Hugo server on http://127.0.0.1:%s/.\n' "$port"
    ;;
  *)
    rm -f "$PID_FILE"
    printf 'Removed a stale PID file; no matching server was stopped.\n'
    ;;
esac
