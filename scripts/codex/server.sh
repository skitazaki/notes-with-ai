#!/bin/sh

set -eu

ROOT=$(git rev-parse --show-toplevel)
RUNTIME="$ROOT/.codex-runtime"
PID_FILE="$RUNTIME/hugo.pid"
PORT_FILE="$RUNTIME/hugo.port"
LOG_FILE="$RUNTIME/hugo.log"
MIN_PORT=14100
MAX_PORT=14999

mkdir -p "$RUNTIME"

is_our_server() {
  pid=$1
  port=$2

  kill -0 "$pid" 2>/dev/null || return 1
  command=$(ps -p "$pid" -o command= 2>/dev/null || true)
  case "$command" in
    *hugo*server*"--port $port"*"--source $ROOT"*) return 0 ;;
    *) return 1 ;;
  esac
}

is_ready() {
  curl --fail --silent --show-error --max-time 2 \
    "http://127.0.0.1:$1/" >/dev/null 2>&1
}

if [ -f "$PID_FILE" ] && [ -f "$PORT_FILE" ]; then
  pid=$(cat "$PID_FILE")
  port=$(cat "$PORT_FILE")
  if is_our_server "$pid" "$port" && is_ready "$port"; then
    printf 'Hugo server is already running at http://127.0.0.1:%s/\n' "$port"
    exit 0
  fi
fi

rm -f "$PID_FILE"
preferred_port=""
if [ -f "$PORT_FILE" ]; then
  preferred_port=$(cat "$PORT_FILE")
fi

port=$MIN_PORT
while [ "$port" -le "$MAX_PORT" ]; do
  candidate=$port
  if [ -n "$preferred_port" ]; then
    candidate=$preferred_port
    preferred_port=""
    case "$candidate" in
      ''|*[!0-9]*) candidate=$port ;;
    esac
    if [ "$candidate" -lt "$MIN_PORT" ] || [ "$candidate" -gt "$MAX_PORT" ]; then
      candidate=$port
    fi
    port=$((candidate + 1))
  else
    port=$((port + 1))
  fi

  : >"$LOG_FILE"
  (
    cd "$ROOT"
    exec nohup hugo server --minify \
      --bind 127.0.0.1 \
      --port "$candidate" \
      --baseURL "http://127.0.0.1:$candidate/" \
      --source "$ROOT"
  ) >>"$LOG_FILE" 2>&1 &
  pid=$!

  attempts=0
  while [ "$attempts" -lt 60 ]; do
    if ! kill -0 "$pid" 2>/dev/null; then
      break
    fi
    if is_ready "$candidate" && kill -0 "$pid" 2>/dev/null; then
      printf '%s\n' "$pid" >"$PID_FILE.tmp"
      printf '%s\n' "$candidate" >"$PORT_FILE.tmp"
      mv "$PID_FILE.tmp" "$PID_FILE"
      mv "$PORT_FILE.tmp" "$PORT_FILE"
      printf 'Hugo server started at http://127.0.0.1:%s/\n' "$candidate"
      exit 0
    fi
    sleep 0.25
    attempts=$((attempts + 1))
  done

  if kill -0 "$pid" 2>/dev/null; then
    kill "$pid" 2>/dev/null || true
    wait "$pid" 2>/dev/null || true
    printf 'Hugo did not become ready on port %s; see %s\n' "$candidate" "$LOG_FILE" >&2
    exit 1
  fi

  wait "$pid" 2>/dev/null || true
done

printf 'No available port in range %s-%s.\n' "$MIN_PORT" "$MAX_PORT" >&2
exit 1
