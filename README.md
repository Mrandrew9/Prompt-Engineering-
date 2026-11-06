# 🤖 Prompt Engineering CI/CD

![prompt-ci](https://github.com/Mrandrew9/Prompt-Engineering-/actions/workflows/prompt-ci.yml/badge.svg)

Treat LLM prompts like code: version them, validate them against a schema, test them, and evaluate them on every pull request with GitHub Actions.

## Why

Prompts that drive IT automation (ticket summaries, triage, Slack replies) break quietly when someone edits them. This repo shows a lightweight pipeline that catches broken or drifting prompts before they reach production.

## How it works

```
prompts/*.yaml ──► schema validation ──► pytest ──► offline eval ──► eval_report.md
                                                                     └─► GitHub Pages (scheduled)
```

Each prompt is a YAML file with a name, an input schema, a Jinja2 template, and test cases:

```yaml
name: summarizer
input_schema:
  required: [body, tone]
template: |
  Use a {{ tone }} tone. Summarize this text in 3 bullet points: {{ body }}
tests:
  - id: test1
    input: { body: "User cannot login after reset.", tone: "friendly" }
```

## Workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `prompt-ci.yml` | push, PR | Ruff + Black, schema validation, pytest, offline eval, uploads `eval_report.md` |
| `prompt-evals-pages.yml` | manual / scheduled | Runs evals and publishes the report to GitHub Pages |

## Run locally

```bash
pip install -r requirements.txt
python scripts/validate_schema.py
pytest
python scripts/eval_prompts.py   # writes eval_report.md
```

## Add a prompt

1. Create `prompts/<name>.yaml` with `name`, `template`, and at least one entry under `tests`.
2. Open a pull request; CI validates and evaluates it automatically.

## Tech

Python 3.11 · Jinja2 · JSON Schema · pytest · Ruff · Black · GitHub Actions · GitHub Pages

## License

MIT
