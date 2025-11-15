import sys, pathlib, yaml, jsonschema

PROMPT_SCHEMA = {
    "type": "object",
    "required": ["name", "template"],
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "input_schema": {"type": "object"},
        "template": {"type": "string"},
        "tests": {"type": "array"},
    },
    "additionalProperties": True,
}

def main():
    root = pathlib.Path("prompts")
    errors = 0
    for f in root.glob("*.y*ml"):
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
            jsonschema.validate(data, PROMPT_SCHEMA)
        except Exception as e:
            print(f"❌ {f}: {e}")
            errors += 1
        else:
            print(f"✅ {f} validated")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
