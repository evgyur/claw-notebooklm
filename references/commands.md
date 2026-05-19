# Command recipes

## Wrapper commands
```bash
claw-notebooklm status
claw-notebooklm install
claw-notebooklm auth-relay
claw-notebooklm login
claw-notebooklm routes
claw-notebooklm route-info research-dossier
claw-notebooklm route-prompt study-pack summary
claw-notebooklm route-init research-dossier "AI market map" https://example.com/a.pdf https://example.com/b
claw-notebooklm route-ask research-dossier <notebook_id> summary
claw-notebooklm raw list
```

## Health and auth
```bash
notebooklm --version
notebooklm status --paths
notebooklm auth check
notebooklm auth check --test
notebooklm auth check --json
notebooklm auth refresh          # one-shot cookie keepalive for cron/systemd
notebooklm auth refresh --quiet
notebooklm doctor
notebooklm doctor --fix
```

## Profiles and isolation
```bash
notebooklm profile list
notebooklm profile create work
notebooklm profile switch work
notebooklm -p work status
NOTEBOOKLM_HOME=/tmp/notebooklm-agent-1 notebooklm list
NOTEBOOKLM_AUTH_JSON="$STORAGE_STATE_JSON" notebooklm list
```

## Notebook basics
```bash
notebooklm list
notebooklm create "Research: Topic"
notebooklm use <notebook_id>          # single-agent convenience only
notebooklm status --json
notebooklm rename "New Title"
notebooklm delete <notebook_id>       # destructive; ask first
```

## Sources
```bash
notebooklm source add "https://example.com"
notebooklm source add ./paper.pdf
notebooklm source add "https://youtube.com/watch?v=..."
notebooklm source add-drive <drive_file_id> "Drive doc title"
notebooklm source add-research "openclaw notebooklm" --mode fast
notebooklm source add-research "openclaw notebooklm" --mode deep --from web --no-wait
notebooklm source list
notebooklm source get <source_id>
notebooklm source guide <source_id> --json
notebooklm source fulltext <source_id> --json
notebooklm source fulltext <source_id> -o source.txt
notebooklm source refresh <source_id>
notebooklm source wait <source_id> --timeout 600 --interval 5
notebooklm source rename <source_id> "Better title"
notebooklm source delete <source_id>          # destructive; ask first
notebooklm source delete-by-title "Exact title"
```

## Research
```bash
notebooklm research status --json
notebooklm research wait --import-all --json
```

## Ask and chat history
```bash
notebooklm ask "What are the key points?"
notebooklm ask "Summarize only these sources" -s <source_id_1> -s <source_id_2>
notebooklm ask "Answer with citations" --json
notebooklm ask "Turn this into an action plan" --save-as-note --note-title "Action plan"
notebooklm configure --mode learning-guide
notebooklm history --show-all
notebooklm history --save --note-title "Conversation summary"
notebooklm history --clear
```

## Generate
```bash
notebooklm generate audio "Make it engaging" --format deep-dive --length default --wait
notebooklm generate video "Short explainer" --format explainer --style whiteboard --wait
notebooklm generate cinematic-video "Documentary-style overview" --wait
notebooklm generate slide-deck "Board-ready narrative" --format presenter --length short --wait
notebooklm generate revise-slide "Move title up" --artifact <artifact_id> --slide 0 --wait
notebooklm generate report --format study-guide --append "Include a glossary" --wait
notebooklm generate quiz --difficulty hard --quantity more --wait
notebooklm generate flashcards --difficulty medium --quantity standard --wait
notebooklm generate infographic "Explain visually" --orientation portrait --detail detailed --style professional --wait
notebooklm generate mind-map
notebooklm generate data-table "compare the core ideas" --wait
```

## Artifacts
```bash
notebooklm artifact list
notebooklm artifact list --type audio
notebooklm artifact get <artifact_id>
notebooklm artifact rename <artifact_id> "Clean title"
notebooklm artifact export <artifact_id> --type docs --title "Exported report"
notebooklm artifact export <artifact_id> --type sheets --title "Exported table"
notebooklm artifact poll <task_id>
notebooklm artifact wait <artifact_id> --timeout 1800 --interval 10
notebooklm artifact suggestions --json
notebooklm artifact delete <artifact_id>      # destructive; ask first
```

## Download
```bash
notebooklm download audio ./podcast.mp3
notebooklm download audio --all ./downloads/audio
notebooklm download video --latest ./overview.mp4
notebooklm download cinematic-video ./cinematic.mp4
notebooklm download slide-deck ./slides.pdf --format pdf
notebooklm download slide-deck ./slides.pptx --format pptx
notebooklm download infographic ./infographic.png
notebooklm download report ./report.md
notebooklm download quiz --format markdown ./quiz.md
notebooklm download quiz --format json ./quiz.json
notebooklm download flashcards --format html ./cards.html
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./table.csv
```

## Notes
```bash
notebooklm note list
notebooklm note create "Manual note body"
notebooklm note get <note_id>
notebooklm note save <note_id> --title "Updated title" --content "Updated body"
notebooklm note rename <note_id> "New note title"
notebooklm note delete <note_id>              # destructive; ask first
```

## Sharing
```bash
notebooklm share status
notebooklm share public --enable
notebooklm share public --disable
notebooklm share view-level full      # full notebook: chat, sources, notes
notebooklm share view-level chat      # chat interface only
notebooklm share add user@example.com --permission viewer
notebooklm share add user@example.com --permission editor -m "Check this out"
notebooklm share add user@example.com --no-notify
notebooklm share update user@example.com --permission editor
notebooklm share remove user@example.com -y
```

## Language
```bash
notebooklm language list
notebooklm language get
notebooklm language set ru
notebooklm language set en --local
```

## Metadata and agent skill
```bash
notebooklm metadata --json
notebooklm metadata -n <notebook_id> --json
notebooklm skill install --target all
```

## Multi-agent safe mode
Prefer explicit notebook IDs and JSON output in agents:

```bash
notebooklm ask -n <notebook_id> "Question" --json
notebooklm source add -n <notebook_id> ./paper.pdf
notebooklm artifact list -n <notebook_id> --json
```

Avoid `notebooklm use` in parallel agents unless each agent has its own `NOTEBOOKLM_PROFILE` or `NOTEBOOKLM_HOME`.
