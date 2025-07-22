import argparse
import json
import os
import shutil
from pathlib import Path


def load_template_registry():
    registry_path = "templates/template_registry.json"
    if not os.path.exists(registry_path):
        return {}
    with open(registry_path, "r") as f:
        return json.load(f)


def save_template_registry(registry):
    with open("templates/template_registry.json", "w") as f:
        json.dump(registry, f, indent=2)


def create_template(template_id, description, path):
    registry = load_template_registry()

    if template_id in registry:
        raise ValueError(f"Template ID '{template_id}' already exists")

    template_path = f"templates/coding/{path}"
    os.makedirs(template_path, exist_ok=True)

    # Create template files
    template_name = os.path.basename(path)
    with open(f"{template_path}/{template_name}.md", "w") as f:
        f.write(f"# {description}\n\n[Template content goes here]")

    with open(f"{template_path}/{template_name}.config.json", "w") as f:
        f.write("{}\n")

    # Update registry
    registry[template_id] = {
        "path": f"coding/{path}",
        "description": description,
        "config_model": "BaseConfig",  # Default config model
    }
    save_template_registry(registry)

    print(f"✅ Created template '{template_id}' in {template_path}")


def delete_template(template_id):
    registry = load_template_registry()

    if template_id not in registry:
        raise ValueError(f"Template ID '{template_id}' not found")

    template_path = f"templates/{registry[template_id]['path']}"
    if os.path.exists(template_path):
        shutil.rmtree(template_path)

    del registry[template_id]
    save_template_registry(registry)

    print(f"✅ Deleted template '{template_id}'")


def list_templates():
    registry = load_template_registry()
    print("\nAvailable Templates:")
    print("-------------------")
    for template_id, info in registry.items():
        print(f"\n{template_id}:")
        print(f"  Description: {info['description']}")
        print(f"  Path: templates/{info['path']}")
        print(f"  Config Model: {info['config_model']}")


def update_template_config(template_id, config_model):
    registry = load_template_registry()

    if template_id not in registry:
        raise ValueError(f"Template ID '{template_id}' not found")

    registry[template_id]["config_model"] = config_model
    save_template_registry(registry)

    print(f"✅ Updated config model for '{template_id}' to {config_model}")


def main():
    parser = argparse.ArgumentParser(description="Manage prompt templates")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Create template
    create_parser = subparsers.add_parser("create", help="Create a new template")
    create_parser.add_argument("template_id", help="Short ID for the template")
    create_parser.add_argument("description", help="Description of the template")
    create_parser.add_argument("path", help="Path under templates/coding/")

    # Delete template
    delete_parser = subparsers.add_parser("delete", help="Delete a template")
    delete_parser.add_argument("template_id", help="ID of template to delete")

    # List templates
    subparsers.add_parser("list", help="List all templates")

    # Update config model
    update_parser = subparsers.add_parser(
        "update-config", help="Update template config model"
    )
    update_parser.add_argument("template_id", help="ID of template to update")
    update_parser.add_argument("config_model", help="New config model name")

    args = parser.parse_args()

    try:
        if args.command == "create":
            create_template(args.template_id, args.description, args.path)
        elif args.command == "delete":
            delete_template(args.template_id)
        elif args.command == "list":
            list_templates()
        elif args.command == "update-config":
            update_template_config(args.template_id, args.config_model)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
