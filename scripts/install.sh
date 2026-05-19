#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${CLAW_NOTEBOOKLM_VENV:-$ROOT_DIR/.venv}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
LOCAL_BIN_DIR="${LOCAL_BIN_DIR:-$HOME/.local/bin}"

mkdir -p "$LOCAL_BIN_DIR"

if [[ -e "$VENV_DIR" && ! -x "$VENV_DIR/bin/python" ]]; then
  echo "Removing broken virtualenv at $VENV_DIR"
  rm -rf "$VENV_DIR"
fi

"$PYTHON_BIN" -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel

UPSTREAM_DIR="$ROOT_DIR/references/notebooklm-py"
if [[ -f "$UPSTREAM_DIR/pyproject.toml" ]]; then
  "$VENV_DIR/bin/python" -m pip install -e "$UPSTREAM_DIR[browser]"
else
  "$VENV_DIR/bin/python" -m pip install "notebooklm-py[browser]"
fi

"$VENV_DIR/bin/python" -m playwright install chromium

ln -sf "$ROOT_DIR/scripts/claw-notebooklm.sh" "$LOCAL_BIN_DIR/claw-notebooklm"

cat <<EOF
Install complete.

Wrapper command:
  claw-notebooklm

If '$LOCAL_BIN_DIR' is not in PATH, add this line to your shell profile:
  export PATH="$LOCAL_BIN_DIR:\$PATH"

Next steps:
  claw-notebooklm status
  claw-notebooklm auth-relay
EOF
