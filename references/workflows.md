# Workflows

## 1) Install and auth bootstrap
1. Clone the repo with submodules.
2. Run `bash scripts/install.sh`.
3. If Browser Relay already has the target Google account logged in, run:
   ```bash
   claw-notebook-llm auth-relay
   ```
4. Verify with:
   ```bash
   claw-notebook-llm status
   claw-notebook-llm raw list
   ```

## 2) Quick status / diagnosis
1. `claw-notebook-llm status`
2. If auth fails:
   - try `claw-notebook-llm auth-relay`
   - or use `claw-notebook-llm login`
3. If auth passes → continue to notebook workflow

## 3) Research → ask
1. `notebooklm create "Research: <topic>"`
2. `notebooklm source add ...` for each source
3. `notebooklm source list`
4. `notebooklm source wait <source_id>` for pending sources
5. `notebooklm ask "<question>"`

## 4) Research → artifact
1. Confirm the user wants generation/download
2. Create/select notebook
3. Add and wait for sources
4. Run `notebooklm generate <type> ...`
5. Poll with `notebooklm artifact list` or `notebooklm artifact wait <artifact_id>`
6. Download to explicit path
7. Verify file exists and is non-empty

## 5) Source-grounded extraction
Use when the user wants answers strictly from notebook context.

Suggested pattern:
```bash
notebooklm ask "Answer only from these sources and be explicit about uncertainty" --json
```

If needed, inspect indexed text:
```bash
notebooklm source fulltext <source_id> --json
```

## 6) Multi-agent safe mode
For subagents or parallel runs:
- do not rely on shared active context
- keep notebook IDs explicit in every command
- if isolation is needed:
```bash
export NOTEBOOKLM_HOME=/tmp/notebooklm-$RUN_ID
```

## 7) Destructive path
Ask before:
- notebook deletion
- source deletion when not obviously safe
- note-saving side effects the user did not request
