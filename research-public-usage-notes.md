# Public usage notes for NotebookLM

Research intent: identify how real people are using NotebookLM in practice, then translate that into route ideas for `claw-notebook-llm`.

## Source fragments used

### Reddit / search-result evidence
1. `https://www.reddit.com/r/notebooklm/comments/1oi1yy5/whats_you_favorite_use_cases_for_notebooklm/`
   - snippet seen in search: language learning through comprehensible input audio on favorite topics; also exam study
2. `https://www.reddit.com/r/notebooklm/comments/1hh4xbg/please_explain_use_cases_for_this_app/`
   - snippet seen in search: student workflow with lecture notes, research papers, and news articles
3. `https://www.reddit.com/r/notebooklm/comments/1lipiq4/usecases_ideas_how_to_use_notebook_lm/`
   - snippet seen in search: throw an entire book in, then generate audio
4. `https://www.reddit.com/r/notebooklm/comments/1lsheh4/what_are_some_cools_things_you_guys_are_using/`
   - snippet seen in search: use case around tracking what to ask a mechanic next time; broader learning uses
5. `https://www.reddit.com/r/notebooklm/comments/1m41lnu/how_to_use_notebook_lm_at_work/`
   - snippet seen in search: separate notebook per distinct subject matter; use as a knowledge base with ebooks/manuals/forms
6. `https://www.reddit.com/r/notebooklm/comments/1ngo162/what_use_cases_do_you_solve_with_notebookllm_at/`
   - snippet seen in search: work use cases in law/legal context; mixed practical enthusiasm and limits
7. `https://www.reddit.com/r/notebooklm/comments/1qr1tju/are_there_any_usecases_for_notebooklm_for/`
   - snippet seen in search: better results when users work through stages rather than one-shot everything
8. `https://www.reddit.com/r/notebooklm/comments/1opvmav/anyone_else_love_notebooklm_but_feel_iffy_using/`
   - snippet seen in search: privacy concerns for internal company docs

### Google AI Overview / search synthesis fragments
Observed summary themes in search results:
- sources -> study guide is a dominant workflow
- PDFs + YouTube + docs in one notebook is common
- users value source-grounded Q&A with citations
- audio overview is used as a first-pass compression layer, not only as a novelty

## Distilled signals

### Strong signals
- bounded notebooks outperform giant catch-all notebooks
- mixed-media synthesis is a key differentiator
- study/exam workflow is one of the most stable use cases
- work knowledge base by domain is common
- staged workflows produce better outputs than one-shot prompts
- privacy concern is a real blocker for enterprise/work usage

### Weak/noisy signals
- generic "productivity" claims without a specific source set
- trying to use one notebook for every domain
- unsafely uploading internal docs without policy guardrails

## Translation into repo changes
- add route ideas doc
- bias examples toward bounded notebooks
- explicitly document privacy caution for internal/work docs
- promote staged route patterns instead of magical one-liners
