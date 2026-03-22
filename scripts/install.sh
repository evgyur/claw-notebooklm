#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${CLAW_NOTEBOOKLM_VENV:-$ROOT_DIR/.venv}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
LOCAL_BIN_DIR="${LOCAL_BIN_DIR:-$HOME/.local/bin}"

mkdir -p "$LOCAL_BIN_DIR"

"$PYTHON_BIN" -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel
"$VENV_DIR/bin/python" -m pip install "notebooklm-py[browser]"
"$VENV_DIR/bin/python" -m playwright install chromium

ln -sf "$ROOT_DIR/scripts/claw-notebook-llm.sh" "$LOCAL_BIN_DIR/claw-notebook-llm"

cat <<EOF
Install complete.

Wrapper command:
  claw-notebook-llm

If '$LOCAL_BIN_DIR' is not in PATH, add this line to your shell profile:
  export PATH="$LOCAL_BIN_DIR:\$PATH"

Next steps:
  claw-notebook-llm status
  claw-notebook-llm auth-relay
EOF
