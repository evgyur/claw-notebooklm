# claw-notebook-llm

OpenClaw skill for operating [NotebookLM](https://notebooklm.google.com/) through the `notebooklm` CLI, with a practical auth bridge from the built-in **Browser Relay**.

## What this gives you

- create and manage NotebookLM notebooks
- add URLs, PDFs, files, and YouTube sources
- ask questions against notebook-only context
- generate reports, quizzes, flashcards, mind maps, audio, and more
- reuse the Google account already logged into your Browser Relay browser

This repo contains:
- a public OpenClaw skill: `/claw-notebook-llm`
- install script for local runtime setup
- auth bridge that exports NotebookLM auth from Browser Relay into `~/.notebooklm/storage_state.json`
- upstream `notebooklm-py` pinned as a git submodule

## Install the skill

Clone this repo into your OpenClaw skills workspace. Example:

```bash
git clone --recurse-submodules https://github.com/evgyur/claw-notebook-llm.git ~/openclaw/skills/claw-notebook-llm
cd ~/openclaw/skills/claw-notebook-llm
bash scripts/install.sh
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Install the runtime

The install script creates a local venv in this repo, installs `notebooklm-py[browser]`, installs Playwright Chromium, and links a wrapper command:

```bash
claw-notebook-llm
```

You can also call the wrapper directly:

```bash
bash scripts/claw-notebook-llm.sh status
```

## Auth via Browser Relay

This is the main convenience feature.

If your Google account is already logged into the browser attached through OpenClaw Browser Relay, you can export that session into NotebookLM auth automatically:

```bash
claw-notebook-llm auth-relay
```

By default it connects to:

```text
http://127.0.0.1:18800
```

Override if needed:

```bash
OPENCLAW_BROWSER_RELAY_URL=http://127.0.0.1:18800 claw-notebook-llm auth-relay
```

What it does:
1. connects to Browser Relay over CDP
2. opens NotebookLM in the existing logged-in browser session
3. exports browser storage state to `~/.notebooklm/storage_state.json`
4. runs `notebooklm auth check --test`

If Browser Relay is already using your Google account, this is effectively a one-command login.

## Alternative auth

If you prefer the standard interactive flow:

```bash
claw-notebook-llm login
```

## Usage examples

```bash
claw-notebook-llm status
claw-notebook-llm raw list
claw-notebook-llm raw create "OpenClaw enterprise research"
claw-notebook-llm raw source add "https://www.youtube.com/watch?v=..."
claw-notebook-llm raw ask -n <notebook_id> "Summarize the main points"
```

## Skill triggers

Primary:
- `/claw-notebook-llm`

Compatibility:
- `/notebook-llm`
- `/notebooklm`

## Privacy / secrets

This repo does **not** include your auth state, browser profile, tokens, or secrets.

Ignored locally:
- `.venv/`
- `.notebooklm/`
- `storage_state.json`
- browser profiles and caches

Your exported NotebookLM auth stays on your machine under `~/.notebooklm/` unless you move it yourself.

## Repo layout

- `SKILL.md` — OpenClaw router skill
- `references/` — command recipes, auth, workflows, compatibility notes, and route ideas from real public usage
- `research-public-usage-notes.md` — raw public research notes used to derive route ideas
- `scripts/install.sh` — local runtime installer
- `scripts/claw-notebook-llm.sh` — wrapper command
- `scripts/auth_via_browser_relay.py` — Browser Relay auth export
- `references/notebooklm-py/` — pinned upstream submodule

## Route ideas from real users

Based on public research, the strongest NotebookLM routes are:
- topic-specific knowledge bases
- interview prep notebooks
- study packs from PDFs + lectures + YouTube
- language-learning notebooks
- long-book / long-doc to audio overview
- work knowledge bases by domain
- performance review evidence packs
- mixed-media research dossiers

See:
- `references/routes-from-the-wild.md`
- `research-public-usage-notes.md`

## Quick sanity check

```bash
claw-notebook-llm status
claw-notebook-llm auth-relay
claw-notebook-llm raw list
```
