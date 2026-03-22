# Install

## 1) Clone the skill repo

```bash
git clone --recurse-submodules https://github.com/evgyur/claw-notebook-llm.git ~/openclaw/skills/claw-notebook-llm
cd ~/openclaw/skills/claw-notebook-llm
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
- installs `notebooklm-py[browser]`
- installs Playwright Chromium
- links `claw-notebook-llm` into `~/.local/bin/`

## 3) Authenticate

### Preferred: Browser Relay bootstrap

If your Google account is already logged into the browser attached via OpenClaw Browser Relay:

```bash
claw-notebook-llm auth-relay
```

Override the Browser Relay URL if needed:

```bash
OPENCLAW_BROWSER_RELAY_URL=http://127.0.0.1:18800 claw-notebook-llm auth-relay
```

### Fallback: interactive login

```bash
claw-notebook-llm login
```

## 4) Verify

```bash
claw-notebook-llm status
claw-notebook-llm raw list
```
