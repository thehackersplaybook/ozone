import argparse
import json
import os
from pathlib import Path

import openai
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import re

load_dotenv(dotenv_path=".env")

# Set your OpenAI API key in the environment or here.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


ai = openai.OpenAI(api_key=OPENAI_API_KEY)

TEMPLATE_PATH = Path(
    "templates/coding/development_algorithm_v1/development_algorithm_v1.md"
)
CONFIG_SCHEMA_PATH = Path(
    "templates/coding/development_algorithm_v1/development_algorithm_v1.config.json"
)


class DevConfig(BaseModel):
    project_name: str = Field(..., description="Project name")
    project_codebase: str = Field(..., description="Codebase name (folder/repo)")
    library_name: str = Field(..., description="Main library/module/package name")
    component_type: str = Field(
        ..., description="e.g. 'library', 'service', 'CLI tool', etc."
    )
    programming_language: str = Field(..., description="Programming language")
    test_script: str = Field(..., description="Script or command to run tests")
    lint_script: str = Field(..., description="Script/command to lint")
    format_script: str = Field(..., description="Script/command to autoformat")
    benchmark_script: str = Field(..., description="Script/command to benchmark")
    environment_setup: str = Field(
        ..., description="Environment setup steps/requirements"
    )
    project_requirements: str = Field(
        ...,
        description="Project requirements, specifications, or inline freeform description - includes functional and non-functional requirements. Ideally markdown formatted. Should be explicit and detailed.",
    )
    project_spec: str = Field(..., description="Project specification file or section")
    requirements: str = Field(..., description="Requirements/feature list")
    scaffold_spec: str = Field(..., description="Expected project scaffold structure")
    documentation_folder: str = Field(..., description="Folder for docs")
    iteration_results_file: str = Field(..., description="Log file for iterations")
    benchmark_results_file: str = Field(..., description="File for benchmark results")
    iteration_report_file: str = Field(..., description="Development log/report file")
    log_folder: str = Field(..., description="Folder for agent logs, diffs, etc.")
    tests_folder: str = Field(..., description="Folder containing tests")
    acceptance_criteria: str = Field(
        ..., description="Summary of final acceptance criteria"
    )
    deliverable: str = Field(
        ..., description="What to deliver at end (artifact/bundle)"
    )


def ask_openai_structured(start_prompt):
    # You can adjust the system message to your taste.
    SYSTEM_PROMPT = (
        "You are an expert software architect and prompt engineer. "
        "Given a user request for a project, fill out the following config fields as a JSON object. "
        "Be concise but accurate. Respond with valid JSON. Use the following fields: "
        + ", ".join(DevConfig.model_json_schema()["properties"].keys())
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
        text_format=DevConfig,
    )
    return response.output_parsed


def substitute_template(config, template_path: Path):
    # Map config keys to both lower/upper for compatibility
    values = {k.lower(): str(v) for k, v in config.model_dump().items()}
    with open(template_path, "r") as f:
        text = f.read()

    def replacer(match):
        key = match.group(1)
        return values.get(key.lower(), match.group(0))  # fallback: no replace

    # Substitute all {KEY} (case-insensitive)
    return re.sub(r"\{([A-Za-z0-9_]+)\}", replacer, text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start-prompt",
        type=str,
        required=True,
        help="Your project prompt (natural language)",
    )
    parser.add_argument(
        "--output", type=str, default="filled_development_prompt.md", help="Output file"
    )
    args = parser.parse_args()

    print("🔎 Generating project config from OpenAI...")
    config = ask_openai_structured(args.start_prompt)
    print("✅ Config generated:\n", json.dumps(config.model_dump(), indent=2))

    print("📄 Filling template...")
    filled_prompt = substitute_template(config, TEMPLATE_PATH)

    with open(args.output, "w") as f:
        f.write(filled_prompt)
    print(f"🎉 Prompt written to {args.output}")


if __name__ == "__main__":
    main()
