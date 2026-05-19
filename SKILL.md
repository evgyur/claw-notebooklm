---
name: claw-notebooklm
description: Operates NotebookLM from OpenClaw via the `notebooklm` CLI, including install guidance, Browser Relay auth export, route presets, notebook/source management, source-grounded Q&A, and artifact generation. Use for explicit `/claw-notebooklm` requests or NotebookLM workflows like summaries, flashcards, quizzes, reports, and podcast-style outputs.
---

# Claw NotebookLM

Command: `/claw-notebooklm`

Compatibility aliases:
- `/notebooklm`

## Contract

**Primary class:** Router  
**Secondary class:** Executor

**Use when:** the user wants NotebookLM workflows: create notebooks, add URLs/PDFs/YouTube/files, ask notebook-grounded questions, use route presets, run research imports, generate artifacts, or bootstrap NotebookLM auth from Browser Relay.

**Do not use when:** a simpler local tool is enough, or NotebookLM auth/setup is missing and the user has not approved login/setup.

**Output contract:**
- selected NotebookLM workflow or exact command path
- auth state and whether Browser Relay bootstrap was used
- notebook/source/artifact IDs or proof path
- filesystem write path for downloads when relevant
- concise risk note for destructive or long-running actions

**Verification gate:** do not claim NotebookLM is ready, authenticated, generated, or downloaded without a direct `notebooklm` status/auth/list/wait/download check.

## What this skill does
- uses the installed `notebooklm` CLI from the pinned upstream runtime
- supports local install guidance
- supports auth bootstrap from built-in OpenClaw Browser Relay
- exposes route presets for the strongest real-world NotebookLM workflows
- routes NotebookLM requests through concise, verifiable workflows
- keeps auth, context, and multi-agent isolation explicit
- keeps the upstream `notebooklm-py` repo pinned as the install/runtime reference submodule

## Trigger
Use this skill when the user says:
- `/claw-notebooklm`
- `/notebooklm`
- "use NotebookLM"
- "сделай в notebooklm"
- "добавь это в NotebookLM"
- "сделай summary/flashcards/quiz/report в NotebookLM"
- "авторизуй NotebookLM через Browser Relay"

## Fast command mapping

- `/claw-notebooklm status` → binary + paths + auth check
- `/claw-notebooklm install` → local install guidance / wrapper setup
- `/claw-notebooklm auth relay` → export auth from Browser Relay into NotebookLM
- `/claw-notebooklm routes` → list route presets
- `/claw-notebooklm route-info <id>` → inspect one route preset
- `/claw-notebooklm route-prompt <id> <phase>` → print a built-in route prompt
- `/claw-notebooklm route-init <id> <title> [sources...]` → create a notebook, add sources, wait, print next prompts
- `/claw-notebooklm route-ask <id> <notebook_id> <phase>` → run one built-in route prompt against a notebook
- `/claw-notebooklm login` → interactive browser login
- `/claw-notebooklm list` → list notebooks
- `/claw-notebooklm create <title>` → create notebook
- `/claw-notebooklm use <id>` → set active notebook (single-agent only)
- `/claw-notebooklm add <url|file|youtube>` → add source
- `/claw-notebooklm ask <question>` → ask current notebook
- `/claw-notebooklm research <query>` → add research sources
- `/claw-notebooklm generate <type> ...` → create audio/video/quiz/etc.
- `/claw-notebooklm download <type> ...` → export artifacts

## Operating rules

1. Auth first: run `status` / `auth check` before promising execution.
2. Prefer Browser Relay bootstrap when the user already has Google logged into the attached browser.
3. In parallel work, avoid shared context collisions:
   - prefer explicit notebook IDs (`--notebook` / `-n` / `-a`)
   - avoid `notebooklm use` across multiple agents
   - if needed, isolate with `NOTEBOOKLM_HOME`
4. In the main conversation:
   - read-only/status/list operations can run directly
   - ask before long-running generation, downloads, or destructive actions
5. In subagents:
   - `wait`/poll operations are fine
   - always return notebook/source/artifact IDs
6. Downloads must write to explicit paths, then verify the file exists.
7. Never imply that this skill requires a custom `/relay` skill; built-in Browser Relay is enough.
8. Favor bounded notebooks and staged workflows over giant notebooks and one-shot prompting.

## Recommended references
- [Install](references/install.md)
- [Commands](references/commands.md)
- [Auth and isolation](references/auth-and-isolation.md)
- [Workflows](references/workflows.md)
- [Route presets](references/route-presets.md)
- [Routes from the wild](references/routes-from-the-wild.md)
- [Manual review checklist](references/manual-review-checklist.md)
- [Backward compatibility map](references/backward-compat-map.md)
- Upstream pinned repo: `references/notebooklm-py/`

## Output Contract
1. skill folder name: `claw-notebooklm`
2. router file: `SKILL.md`
3. references list:
   - `references/install.md`
   - `references/commands.md`
   - `references/auth-and-isolation.md`
   - `references/workflows.md`
   - `references/route-presets.md`
   - `references/routes-from-the-wild.md`
   - `references/manual-review-checklist.md`
   - `references/backward-compat-map.md`
   - `references/notebooklm-py/` (git submodule)
4. install/runtime entrypoints:
   - `scripts/install.sh`
   - `scripts/claw-notebooklm.sh`
   - `scripts/auth_via_browser_relay.py`
   - `scripts/route_tools.py`
   - `routes/routes.json`
5. public repo contract:
   - no committed auth state
   - no committed browser profiles
   - Browser Relay auth flow documented without custom `/relay` skill dependency

## Quick Test Checklist
- [ ] `bash scripts/install.sh` completes without adding secrets to git.
- [ ] `claw-notebooklm status` prints version and NotebookLM paths.
- [ ] `claw-notebooklm auth-relay` writes `~/.notebooklm/storage_state.json` and `notebooklm auth check --test` passes when Browser Relay is already logged in.
- [ ] `claw-notebooklm routes` prints the route catalog.
- [ ] `claw-notebooklm route-info research-dossier` works.
- [ ] `claw-notebooklm route-init ...` creates a notebook and waits for sources.
- [ ] `claw-notebooklm route-ask ...` returns a structured NotebookLM answer.
- [ ] `notebooklm --help` is callable from the repo venv wrapper.
- [ ] `git submodule status` shows `references/notebooklm-py`.
- [ ] All reference links in `SKILL.md` resolve.

## Done Criteria
- YAML frontmatter is valid and third-person.
- `SKILL.md` stays router-first and readable in under 1 minute.
- Critical instructions live in first-level `references/*.md`.
- No local auth state, tokens, or private paths are committed.
- Browser Relay auth flow is documented without depending on a custom relay skill.
- Upstream repo remains connected as a real git submodule.
- Wrapper script exists for install/status/auth/raw passthrough.
- Route helpers exist for discovery and execution (`routes`, `route-info`, `route-prompt`, `route-init`, `route-ask`).
