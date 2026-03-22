# Route presets

`claw-notebook-llm` exposes first-class route helpers so users can discover and use the strongest NotebookLM workflows quickly.

## Commands

```bash
claw-notebook-llm routes
claw-notebook-llm route-info research-dossier
claw-notebook-llm route-prompt research-dossier summary
claw-notebook-llm route-init research-dossier "AI market map" https://example.com/a.pdf https://example.com/b
claw-notebook-llm route-ask research-dossier <notebook_id> summary
```

## Available route IDs
- `research-dossier`
- `interview-prep`
- `study-pack`
- `domain-kb`
- `review-pack`
- `language-learning`
- `book-to-audio`

## What route-init does
1. creates a notebook
2. adds the provided sources
3. waits until they are ready by default
4. prints the next recommended prompts for that route

## What route-ask does
Runs the route’s built-in prompt for one phase:
- `map`
- `summary`
- `extract`

## Design intent
These routes are intentionally staged.

The workflow is:
1. bounded source set
2. map the notebook
3. summarize
4. extract outputs
5. only then generate artifacts like quiz/flashcards/audio when useful

This mirrors the strongest public usage patterns and avoids the common one-shot anti-pattern.
