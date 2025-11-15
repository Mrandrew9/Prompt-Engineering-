# 🤖 Prompt Engineering CI/CD

Lightweight CI/CD for prompts using GitHub Actions.

**Workflows**
- `prompt-ci.yml` — Lint, tests, schema validation, offline evals, uploads `eval_report.md`.
- `prompt-evals-pages.yml` — Manual/scheduled eval + publish to **GitHub Pages**.

**Local run**
```bash
pip install -r requirements.txt
python scripts/validate_schema.py
pytest
python scripts/eval_prompts.py
