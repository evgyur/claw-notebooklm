# Install

## 1) Clone the skill repo

```bash
git clone --recurse-submodules https://github.com/evgyur/claw-notebooklm.git ~/openclaw/skills/claw-notebooklm
cd ~/openclaw/skills/claw-notebooklm
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

## 2) Install the runtime

```bash
bash scripts/install.sh
```

This does the following:
- creates `.venv/` in this repo
- installs `notebooklm-py[browser]` from the pinned `references/notebooklm-py` submodule when present; falls back to PyPI only if the submodule is unavailable
- installs Playwright Chromium
- links `claw-notebooklm` into `~/.local/bin/`

## 3) Authenticate

### Preferred: Browser Relay bootstrap

If your Google account is already logged into the browser attached via OpenClaw Browser Relay:

```bash
claw-notebooklm auth-relay
```

Override the Browser Relay URL if needed:

```bash
OPENCLAW_BROWSER_RELAY_URL=http://127.0.0.1:18800 claw-notebooklm auth-relay
```

### Fallback: interactive login

```bash
claw-notebooklm login
```

## 4) Verify

```bash
claw-notebooklm status
claw-notebooklm raw list
```
