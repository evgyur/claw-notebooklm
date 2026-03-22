# Auth and isolation

## Installed runtime

Defaults used by this repo:
- local venv: `./.venv`
- wrapper command: `claw-notebook-llm`
- NotebookLM home: `~/.notebooklm`
- auth file: `~/.notebooklm/storage_state.json`
- Browser Relay URL: `http://127.0.0.1:18800` unless overridden by `OPENCLAW_BROWSER_RELAY_URL`

## Auth rules

1. Do not claim readiness until `notebooklm auth check` or `notebooklm list` succeeds.
2. Preferred auth path in OpenClaw environments:
   - use Browser Relay if the user's Google account is already logged into the attached browser
   - export Browser Relay session into NotebookLM auth state
3. Fallback auth path:
   - run `claw-notebook-llm login`
4. This repo does not require a custom `/relay` skill.
   - built-in OpenClaw Browser Relay is enough
5. For CI/CD or ephemeral runs, `NOTEBOOKLM_AUTH_JSON` can be used instead of a file.

## Browser Relay auth flow

Recommended command:

```bash
claw-notebook-llm auth-relay
```

What it does:
- connects to Browser Relay over CDP
- opens `https://notebooklm.google.com/`
- exports browser storage state to `~/.notebooklm/storage_state.json`
- verifies auth with `notebooklm auth check --test`

If the attached browser is already using the right Google account, this avoids re-login.

## Parallel safety

NotebookLM CLI stores current context in one shared file:
- `~/.notebooklm/context.json`

This means concurrent agents can overwrite each other's active notebook.

### Safe patterns

1. **Explicit IDs**
   - use `--notebook <id>` where supported
   - use `-n <id>` / `-a <artifact_id>` for wait/download commands
2. **Per-agent home isolation**
   ```bash
   export NOTEBOOKLM_HOME=/tmp/notebooklm-agent-123
   notebooklm list
   ```
3. **Avoid `use` in parallel**
   - `notebooklm use <id>` is fine only in a single-agent flow

## Work/privacy note

Public user feedback consistently shows a real concern: people love NotebookLM for work, but become uneasy when uploading internal company documents without explicit policy approval.

Practical rule:
- do not treat NotebookLM as the default sink for sensitive internal documents
- prefer public, low-risk, or explicitly approved sources unless the user's policy context is clear
- in enterprise contexts, call this risk out directly
- always validate important outputs against citations instead of trusting the first summary blindly

## Failure wording

Prefer:
- `NotebookLM CLI is installed, but auth is missing.`
- `Browser Relay is reachable, but the attached browser is not authenticated for NotebookLM yet.`
- `NotebookLM auth exists, but the notebook context is not set.`
- `Generation started; artifact is still processing.`

Avoid:
- `NotebookLM is ready` without a real check
- `it generated` before `artifact wait` or verified listing
- `downloaded` before checking the file on disk
