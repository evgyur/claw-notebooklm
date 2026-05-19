# claw-notebooklm

OpenClaw skill for operating [NotebookLM](https://notebooklm.google.com/) through the `notebooklm` CLI, with a practical auth bridge from the built-in **Browser Relay**.

## What this gives you

- create and manage NotebookLM notebooks
- add URLs, PDFs, files, YouTube, Google Drive sources, and research imports
- ask source-grounded questions against notebook-only context
- generate reports, quizzes, flashcards, mind maps, data tables, audio, video, slide decks, infographics, and more
- download generated artifacts as MP3/MP4/PDF/PPTX/PNG/CSV/JSON/Markdown/HTML where supported
- manage sharing: public links, view level, and user permissions
- reuse the Google account already logged into your Browser Relay browser

This repo contains:
- a public OpenClaw skill: `/claw-notebooklm`
- install script for local runtime setup
- auth bridge that exports NotebookLM auth from Browser Relay into `~/.notebooklm/storage_state.json`
- upstream `notebooklm-py` pinned as a git submodule (`v0.4.1`)

## Architecture

`claw-notebooklm` is the OpenClaw/Hermes UX layer. It should stay thin:

- upstream engine: `teng-lin/notebooklm-py`
- OpenClaw UX: wrapper commands, Browser Relay auth bootstrap, route presets, guardrails
- local runtime: repo-local `.venv` plus `claw-notebooklm` wrapper

Do not fork NotebookLM API logic into this repo unless it is OpenClaw-specific. Prefer updating the pinned upstream submodule and command references.

## Install the skill

Clone this repo into your OpenClaw skills workspace. Example:

```bash
git clone --recurse-submodules https://github.com/evgyur/claw-notebooklm.git ~/openclaw/skills/claw-notebooklm
cd ~/openclaw/skills/claw-notebooklm
bash scripts/install.sh
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

## Install the runtime

The install script creates a local venv in this repo, installs `notebooklm-py[browser]`, installs Playwright Chromium, and links a wrapper command:

```bash
claw-notebooklm
```

You can also call the wrapper directly:

```bash
bash scripts/claw-notebooklm.sh status
```

The installer removes a broken/incomplete `.venv` automatically before recreating it.

## Auth via Browser Relay

This is the main convenience feature.

If your Google account is already logged into the browser attached through OpenClaw Browser Relay, you can export that session into NotebookLM auth automatically:

```bash
claw-notebooklm auth-relay
```

By default it connects to:

```text
http://127.0.0.1:18800
```

Override if needed:

```bash
OPENCLAW_BROWSER_RELAY_URL=http://127.0.0.1:18800 claw-notebooklm auth-relay
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
claw-notebooklm login
```

For long-lived/headless setups, upstream also supports a one-shot keepalive:

```bash
claw-notebooklm raw auth refresh
claw-notebooklm raw auth refresh --quiet
```

## Usage examples

```bash
claw-notebooklm status
claw-notebooklm raw list
claw-notebooklm raw create "OpenClaw enterprise research"
claw-notebooklm raw source add "https://www.youtube.com/watch?v=..."
claw-notebooklm raw ask -n <notebook_id> "Summarize the main points" --json
claw-notebooklm raw generate slide-deck "Board-ready story" --wait
claw-notebooklm raw download slide-deck ./slides.pptx --format pptx
claw-notebooklm raw share status
```

Full recipes live in `references/commands.md`.

## Route presets

The repo exposes first-class route helpers so people can access strong NotebookLM workflows instead of reading about them only.

```bash
claw-notebooklm routes
claw-notebooklm route-info research-dossier
claw-notebooklm route-prompt study-pack summary
claw-notebooklm route-init research-dossier "AI market map" https://example.com/a.pdf https://example.com/b
claw-notebooklm route-ask research-dossier <notebook_id> summary
```

Available route IDs:
- `research-dossier`
- `interview-prep`
- `study-pack`
- `domain-kb`
- `review-pack`
- `language-learning`
- `book-to-audio`

## Skill triggers

Primary:
- `/claw-notebooklm`

Compatibility:
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
- `references/` — command recipes, auth, workflows, compatibility notes, route ideas, and preset docs
- `routes/routes.json` — machine-readable route preset catalog
- `research-public-usage-notes.md` — raw public research notes used to derive route ideas
- `examples.md` — exact example workflows with commands
- `scripts/install.sh` — local runtime installer
- `scripts/claw-notebooklm.sh` — wrapper command
- `scripts/auth_via_browser_relay.py` — Browser Relay auth export
- `scripts/route_tools.py` — route discovery/init/ask helper
- `references/notebooklm-py/` — pinned upstream submodule

## Route ideas from real users

Based on public research plus a Perplexity cross-check, the strongest NotebookLM routes are:
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
- `references/route-presets.md`
- `research-public-usage-notes.md`
- `examples.md`
- `presentations/claw-notebooklm-overview-ru.html`

## Practical rules from public usage

- one notebook should usually map to one topic, workflow, or cycle of work
- staged workflows beat one-shot prompting
- validate important outputs against citations
- audio overviews are great as a first pass, not as a final truth source
- for work usage, be explicit about privacy and internal-doc policy
- use explicit notebook IDs in multi-agent runs; avoid shared `notebooklm use` context unless isolated by profile/home

## Quick sanity check

```bash
claw-notebooklm status
claw-notebooklm auth-relay
claw-notebooklm routes
claw-notebooklm route-info research-dossier
claw-notebooklm raw list
```
