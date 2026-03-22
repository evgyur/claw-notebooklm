#!/usr/bin/env bash
set -euo pipefail

SOURCE_PATH="${BASH_SOURCE[0]}"
while [[ -h "$SOURCE_PATH" ]]; do
  SOURCE_DIR="$(cd -P "$(dirname "$SOURCE_PATH")" && pwd)"
  SOURCE_PATH="$(readlink "$SOURCE_PATH")"
  [[ "$SOURCE_PATH" != /* ]] && SOURCE_PATH="$SOURCE_DIR/$SOURCE_PATH"
done
ROOT_DIR="$(cd -P "$(dirname "$SOURCE_PATH")/.." && pwd)"
VENV_DIR="${CLAW_NOTEBOOKLM_VENV:-$ROOT_DIR/.venv}"
PYTHON="$VENV_DIR/bin/python"
NOTEBOOKLM="$VENV_DIR/bin/notebooklm"

cmd="${1:-status}"
shift || true

need_runtime() {
  if [[ ! -x "$NOTEBOOKLM" ]]; then
    echo "NotebookLM runtime is not installed here yet." >&2
    echo "Run: bash $ROOT_DIR/scripts/install.sh" >&2
    exit 1
  fi
}

case "$cmd" in
  install)
    exec bash "$ROOT_DIR/scripts/install.sh" "$@"
    ;;
  status)
    need_runtime
    "$NOTEBOOKLM" --version
    echo '---'
    "$NOTEBOOKLM" status --paths
    echo '---'
    "$NOTEBOOKLM" auth check || true
    ;;
  auth-relay)
    need_runtime
    exec "$PYTHON" "$ROOT_DIR/scripts/auth_via_browser_relay.py" "$@"
    ;;
  login)
    need_runtime
    exec "$NOTEBOOKLM" login "$@"
    ;;
  raw)
    need_runtime
    exec "$NOTEBOOKLM" "$@"
    ;;
  *)
    need_runtime
    exec "$NOTEBOOKLM" "$cmd" "$@"
    ;;
esac
