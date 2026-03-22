# Example route workflows

## 1) Research dossier
```bash
claw-notebook-llm route-init research-dossier "AI market map" \
  https://example.com/report-1.pdf \
  https://example.com/report-2.pdf \
  https://www.youtube.com/watch?v=abc123

claw-notebook-llm route-ask research-dossier <notebook_id> map
claw-notebook-llm route-ask research-dossier <notebook_id> summary
claw-notebook-llm route-ask research-dossier <notebook_id> extract
```

## 2) Interview prep
```bash
claw-notebook-llm route-init interview-prep "Acme PM interview" \
  ./resume.pdf \
  ./job-description.pdf \
  https://acme.com/about \
  https://acme.com/product

claw-notebook-llm route-ask interview-prep <notebook_id> summary
claw-notebook-llm route-ask interview-prep <notebook_id> extract
```

## 3) Study pack
```bash
claw-notebook-llm route-init study-pack "Operating Systems exam" \
  ./lecture-1.pdf \
  ./lecture-2.pdf \
  https://www.youtube.com/watch?v=lecture123

claw-notebook-llm route-ask study-pack <notebook_id> map
claw-notebook-llm route-ask study-pack <notebook_id> summary
claw-notebook-llm route-ask study-pack <notebook_id> extract
# then optionally use notebooklm generate flashcards / quiz / audio
```

## 4) Domain knowledge base
```bash
claw-notebook-llm route-init domain-kb "Compliance: ISO 27001" \
  ./policy.pdf \
  ./sop.pdf \
  https://example.com/standard

claw-notebook-llm route-ask domain-kb <notebook_id> summary
claw-notebook-llm route-ask domain-kb <notebook_id> extract
```
