# Command recipes

## Wrapper commands
```bash
claw-notebook-llm status
claw-notebook-llm install
claw-notebook-llm auth-relay
claw-notebook-llm login
claw-notebook-llm routes
claw-notebook-llm route-info research-dossier
claw-notebook-llm route-prompt study-pack summary
claw-notebook-llm route-init research-dossier "AI market map" https://example.com/a.pdf https://example.com/b
claw-notebook-llm route-ask research-dossier <notebook_id> summary
claw-notebook-llm raw list
```

## Health
```bash
notebooklm --version
notebooklm status --paths
notebooklm auth check
notebooklm auth check --test
```

## Notebook basics
```bash
notebooklm list
notebooklm create "Research: Topic"
notebooklm use <notebook_id>
notebooklm status
```

## Sources
```bash
notebooklm source add "https://example.com"
notebooklm source add ./paper.pdf
notebooklm source add "https://youtube.com/watch?v=..."
notebooklm source list
notebooklm source wait <source_id>
notebooklm source fulltext <source_id> --json
```

## Research
```bash
notebooklm source add-research "openclaw notebooklm" --mode fast
notebooklm source add-research "openclaw notebooklm" --mode deep --no-wait
notebooklm research status
notebooklm research wait --import-all
```

## Ask
```bash
notebooklm ask "What are the key points?"
notebooklm ask "Summarize only these sources" -s <source_id_1> -s <source_id_2>
notebooklm ask "Answer with citations" --json
```

## Generate
```bash
notebooklm generate audio "Make it engaging"
notebooklm generate video "Short explainer"
notebooklm generate report --format study-guide
notebooklm generate quiz --difficulty hard
notebooklm generate flashcards --quantity more
notebooklm generate mind-map
notebooklm generate data-table "compare the core ideas"
```

## Download
```bash
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
notebooklm download report ./report.md
notebooklm download quiz --format markdown ./quiz.md
notebooklm download flashcards --format json ./cards.json
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./table.csv
```
