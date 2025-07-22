import argparse
import json
import os
from pathlib import Path

import openai
from dotenv import load_dotenv
import re

from config_models import CONFIG_MODEL_MAP

load_dotenv(dotenv_path=".env")

# Set your OpenAI API key in the environment or here.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ai = openai.OpenAI(api_key=OPENAI_API_KEY)


def load_template_registry():
    with open("templates/template_registry.json", "r") as f:
        return json.load(f)


def list_templates():
    registry = load_template_registry()
    print("\nAvailable Templates:")
    print("-------------------")
    for template_id, info in registry.items():
        print(f"\n{template_id}:")
        print(f"  Description: {info['description']}")
        print(f"  Path: templates/{info['path']}")


def get_template_paths(template_id):
    registry = load_template_registry()
    if template_id not in registry:
        raise ValueError(f"Template ID '{template_id}' not found in registry")

    base_path = f"templates/{registry[template_id]['path']}"
    template_name = os.path.basename(registry[template_id]["path"])

    return {
        "template": Path(f"{base_path}/{template_name}.md"),
        "config": Path(f"{base_path}/{template_name}.config.json"),
    }


def ask_openai_structured(start_prompt, template_id):
    config_model = CONFIG_MODEL_MAP[template_id]

    SYSTEM_PROMPT = (
        "You are an expert software architect and prompt engineer. "
        "Given a user request for a project, fill out the following config fields as a JSON object. "
        "Be concise but accurate. Respond with valid JSON. Use the following fields: "
        + ", ".join(config_model.model_json_schema()["properties"].keys())
    )

    prompt = f"Given the project specification from the user, fill out the following config fields as a JSON object. User Prompt: {start_prompt}"

    response = ai.responses.parse(
        model="gpt-4.1",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": prompt,
            },
        ],
        text_format=config_model,
    )
    return response.output_parsed


def substitute_template(config, template_path: Path):
    values = {k.lower(): str(v) for k, v in config.model_dump().items()}
    with open(template_path, "r") as f:
        text = f.read()

    def replacer(match):
        key = match.group(1)
        return values.get(key.lower(), match.group(0))

    return re.sub(r"\{([A-Za-z0-9_]+)\}", replacer, text)


def main():
    parser = argparse.ArgumentParser(description="Generate prompts from templates")
    parser.add_argument(
        "--start-prompt",
        type=str,
        help="Your project prompt (natural language)",
    )
    parser.add_argument(
        "--template-id",
        type=str,
        help="Template ID to use (use --list to see available templates)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file (defaults to filled_<template_id>.md)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available templates",
    )
    args = parser.parse_args()

    if args.list:
        list_templates()
        return

    if not args.template_id:
        parser.error("--template-id is required unless --list is specified")

    if not args.start_prompt:
        parser.error("--start-prompt is required unless --list is specified")

    try:
        paths = get_template_paths(args.template_id)
    except ValueError as e:
        parser.error(str(e))

    print("🔎 Generating project config from OpenAI...")
    config = ask_openai_structured(args.start_prompt, args.template_id)
    print("✅ Config generated:\n", json.dumps(config.model_dump(), indent=2))

    print("📄 Filling template...")
    filled_prompt = substitute_template(config, paths["template"])

    output_file = args.output or f"filled_{args.template_id}.md"
    with open(output_file, "w") as f:
        f.write(filled_prompt)
    print(f"🎉 Prompt written to {output_file}")


if __name__ == "__main__":
    main()
