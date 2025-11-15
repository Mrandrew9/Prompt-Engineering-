import pathlib, yaml, jinja2
from tabulate import tabulate

PROMPTS = pathlib.Path("prompts")
REPORT = pathlib.Path("eval_report.md")

def render(template: str, ctx: dict):
    env = jinja2.Environment(autoescape=False, undefined=jinja2.StrictUndefined)
    return env.from_string(template).render(**ctx)

def main():
    rows = []
    for pf in PROMPTS.glob("*.y*ml"):
        data = yaml.safe_load(pf.read_text(encoding="utf-8"))
        name = data.get("name", pf.stem)
        template = data["template"]

        # Minimal offline test
        sample = {"body": "Example input text for evaluation", "tone": "neutral"}
        output = render(template, sample)
        passed = len(output.split()) >= 10
        rows.append([name, len(output.split()), "PASS" if passed else "FAIL"])

    table = tabulate(rows, headers=["Prompt", "WordCount", "Result"], tablefmt="github")
    REPORT.write_text(f"# Prompt Evaluation Report\n\n{table}\n", encoding="utf-8")
    print(table)

if __name__ == "__main__":
    main()
