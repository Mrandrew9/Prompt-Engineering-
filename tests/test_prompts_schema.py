import pathlib, yaml

def test_prompts_have_required_fields():
    for pf in pathlib.Path("prompts").glob("*.y*ml"):
        data = yaml.safe_load(pf.read_text(encoding="utf-8"))
        assert data.get("name"), f"{pf} missing name"
        assert data.get("template"), f"{pf} missing template"
