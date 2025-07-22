# Ozone - AI-Powered Development Workflow Templates

Ozone is a powerful tool that provides structured templates and algorithms for various software development workflows, powered by OpenAI's GPT models.

## Features

- Multiple specialized templates for different development tasks
- Structured, step-by-step algorithms
- Automated configuration generation
- Template management system
- Detailed logging and documentation

## Available Templates

1. **Development Algorithm (dev-algo-v1)**

   - For new project/feature development
   - Includes test-driven development workflow
   - Comprehensive documentation requirements

2. **Performance Optimization (perf-opt-v1)**

   - Systematic performance analysis
   - Bottleneck identification
   - Iterative optimization process

3. **Code Review (code-review-v1)**

   - Structured code review process
   - Security and performance checks
   - Best practices validation

4. **Refactoring (refactor-v1)**

   - Safe refactoring workflow
   - Architecture migration
   - Test-driven refactoring

5. **Test Generation (test-gen-v1)**
   - Comprehensive test suite generation
   - Coverage analysis
   - Test quality assurance

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your-api-key" > .env
   ```

## Usage

### Generate a Prompt

```bash
python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Your project description" --output output.md
```

Options:

- `--template-id`: Template to use (use `--list` to see available templates)
- `--start-prompt`: Your project/task description
- `--output`: Output file (optional)
- `--list`: List available templates

### Manage Templates

```bash
python template_manager.py [command] [options]
```

Commands:

- `list`: List all templates
- `create`: Create a new template
- `delete`: Delete a template
- `update-config`: Update template configuration

Example:

```bash
# List templates
python template_manager.py list

# Create template
python template_manager.py create my-template "My Custom Template" custom_template_v1

# Update config
python template_manager.py update-config my-template CustomConfig
```

## Example Use Cases

1. **New Project Development**

   ```bash
   python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Create a REST API for user management with authentication"
   ```

2. **Performance Optimization**

   ```bash
   python generate_prompt.py --template-id perf-opt-v1 --start-prompt "Optimize database query performance in user service"
   ```

3. **Code Review**

   ```bash
   python generate_prompt.py --template-id code-review-v1 --start-prompt "Review authentication module for security best practices"
   ```

4. **Refactoring**

   ```bash
   python generate_prompt.py --template-id refactor-v1 --start-prompt "Refactor monolithic app into microservices"
   ```

5. **Test Generation**
   ```bash
   python generate_prompt.py --template-id test-gen-v1 --start-prompt "Generate test suite for payment processing module"
   ```

## Template Structure

Each template consists of:

1. Markdown template file (`.md`)
2. Configuration schema (`.config.json`)
3. Entry in template registry

### Custom Templates

To create a custom template:

1. Use template manager:

   ```bash
   python template_manager.py create my-template "Description" path/to/template
   ```

2. Edit the template files:

   - `path/to/template.md`: Main template
   - `path/to/template.config.json`: Configuration schema

3. Add configuration model in `config_models.py`

4. Update template registry

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details
