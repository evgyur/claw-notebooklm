# Routes from the wild

Real-world NotebookLM usage patterns gathered from public web research (mainly Reddit threads and search snippets), then normalized into product ideas for this skill.

## What people actually do with NotebookLM

### 1) Topic-specific knowledge bases
**Observed pattern:** people keep one notebook per distinct subject and load it with ebooks, manuals, forms, docs, and reference material.

**Why it works:** NotebookLM becomes a bounded retrieval space instead of a generic chat memory dump.

**Good skill route:**
- create notebook by topic/project
- add PDFs, docs, and URLs
- ask source-grounded questions with citations
- export briefing/study guide/report

**Command shape:**
```bash
claw-notebook-llm raw create "Compliance: ISO 27001"
claw-notebook-llm raw source add ./manual.pdf
claw-notebook-llm raw source add https://example.com/policy
claw-notebook-llm raw ask -n <id> "Summarize the control gaps"
```

---

### 2) Interview prep notebooks
**Observed pattern:** people prepare for interviews by loading job descriptions, company materials, resumes, notes, and then asking for likely questions, talking points, and drills.

**Why it works:** the notebook becomes a private prep room with all context in one place.

**Good skill route:**
- create per-company interview notebook
- load JD, resume, company site, product docs, and notes
- ask for likely interview questions, gaps, stories, objections, role fit
- generate speaking notes / mock interview prompts

**High-value extension:** a canned workflow like `interview-prep` would be worth adding later.

---

### 3) Exam and study workflows
**Observed pattern:** students and self-learners upload lecture slides, PDFs, notes, and recordings; then generate summaries, FAQs, flashcards, and study guides.

**Why it works:** this is the cleanest source-grounded use case NotebookLM supports.

**Good skill route:**
- `sources -> ask -> study guide -> flashcards -> quiz`
- great fit for PDFs + YouTube lectures in one notebook

**Good default output stack:**
1. briefing doc
2. study guide
3. flashcards
4. quiz
5. audio overview

---

### 4) Language learning via comprehensible input
**Observed pattern:** people use NotebookLM audio outputs on topics they already like, but in their target language.

**Why it works:** the content is personally relevant, source-bounded, and repeatable.

**Good skill route:**
- load texts or videos in the target language
- ask for simplified explanations and vocabulary extraction
- generate audio overviews for listening repetition
- export flashcards / vocab tables

**High-value extension:** a `language-learning` recipe with prompts for glossary, examples, and listening drills.

---

### 5) Long-book / long-document compression into audio
**Observed pattern:** users throw a long book or dense material into NotebookLM, then generate audio to absorb it faster.

**Why it works:** audio overview is an easier way to traverse a long corpus before deep reading.

**Good skill route:**
- upload long PDF/book/docs
- ask for chapter map and key claims
- generate audio overview
- export notes + key questions for deeper reading

**Product insight:** audio is not just a gimmick; it is often the first-pass compression layer.

---

### 6) Work knowledge base by function
**Observed pattern:** at work, people create notebooks for a function or domain: legal, ops, product, support, compliance, finance, etc.

**Why it works:** each notebook acts like a scoped assistant on one domain instead of a messy all-company memory.

**Good skill route:**
- per-domain notebooks
- standard folder/source import pattern
- reusable prompts: summarize policy, answer from sources only, compare documents, extract action items

**Important caution:** many public users explicitly warn against uploading sensitive internal documents without policy approval.

---

### 7) Performance review / evidence notebook
**Observed pattern:** one public productivity suggestion was to keep evidence for performance reviews: notes, wins, feedback, project artifacts, and periodic summaries.

**Why it works:** NotebookLM is good at turning scattered evidence into a coherent narrative.

**Good skill route:**
- create notebook per quarter / review cycle
- load notes, docs, feedback snippets, project outputs
- ask for impact summary, themes, examples, and draft self-review bullets

---

### 8) Personal maintenance / checklist memory
**Observed pattern:** people use it for ongoing reminder contexts like what to ask a mechanic at the next service, based on past notes and docs.

**Why it works:** this is basically a scoped "decision support notebook".

**Good skill route:**
- create notebook for a recurring domain
- load invoices, notes, previous recommendations, manuals
- ask for checklist before next appointment or next decision

---

### 9) Source-grounded synthesis across mixed media
**Observed pattern:** people mix PDFs, websites, notes, and YouTube videos in one notebook, then use it for synthesis instead of per-source summarization.

**Why it works:** mixed media is where NotebookLM beats a plain transcript tool.

**Good skill route:**
- add docs + URLs + YouTube to one notebook
- wait until all sources are ready
- ask for cross-source synthesis, contradictions, unknowns, and action plan

**This should be one of the headline workflows of this skill.**

---

### 10) Staged workflows beat one-shot prompts
**Observed pattern:** public users say one-shot output is possible, but results improve when they work through stages and manually inspect outputs.

**Why it matters:** this is a workflow design principle, not just a use case.

**Recommended route design:**
1. ingest sources
2. ask for map / inventory
3. ask for summary
4. ask for extraction / comparison / open questions
5. generate artifact only after the notebook looks clean

**Conclusion:** the skill should encourage staged flows over magic one-liners.

## High-value routes worth encoding later

If we productize the best public patterns, these are the best route candidates:

1. `research-dossier`
   - mixed sources -> synthesis -> briefing doc
2. `interview-prep`
   - JD + resume + company docs -> likely questions + stories + drill notes
3. `study-pack`
   - slides + papers + lectures -> study guide + flashcards + quiz + audio
4. `domain-kb`
   - one topic/domain -> reusable bounded knowledge notebook
5. `review-pack`
   - quarterly notes + artifacts -> performance review / self-review draft
6. `language-learning`
   - target-language sources -> simplified notes + glossary + audio
7. `book-to-audio`
   - long document -> chapter map + audio overview + key questions

## Anti-patterns from the wild

### 1) Treating NotebookLM as a general company memory sink
Bad idea. Users get value when notebooks are bounded by topic, project, or purpose.

### 2) Uploading sensitive work docs casually
Public concern around privacy and data handling is real. This must stay explicit in docs.

### 3) Expecting one-shot perfection
The better public workflows are staged and inspected.

### 4) Using one notebook for everything
This usually weakens retrieval quality and makes outputs less trustworthy.

## What we should add to this repo because of this research

### Priority 1
- documented route library based on real public usage
- interview prep workflow example
- study pack workflow example
- mixed-media research dossier workflow example
- work/privacy warning for internal docs

### Priority 2
- reusable prompt packs per route
- helper script examples
- naming conventions: one notebook per topic / project / review cycle

### Priority 3
- wrappers for staged execution instead of one-shot generation
- optional templates for export naming and artifact download
