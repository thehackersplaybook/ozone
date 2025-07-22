# Ozone Usage Examples

This document provides practical examples to test different templates and workflows in Ozone, including example outputs.

## Setup

1. Make sure you have Python 3.8+ installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your-api-key" > .env
   ```

## Test Case 1: Development Algorithm

### Scenario: Create a Simple REST API

```bash
python generate_prompt.py --template-id dev-algo-v1 --start-prompt "Create a FastAPI-based REST API for a todo list application with the following features:
- CRUD operations for todos
- User authentication
- SQLite database
- Basic input validation
- Error handling
- Unit tests with pytest" --output todo_api_dev.md
```

### Example Output (todo_api_dev.md):

```markdown
# Todo List API Development Algorithm

## Project Requirements

Project Name: Todo List API
Programming Language: Python
Framework: FastAPI
Database: SQLite
Test Framework: pytest

### Features Required:

- CRUD operations for todos
- User authentication
- Basic input validation
- Error handling
- Unit tests

## Step 1: Project Scaffold

...

## Step 2: Database Setup

...

## Step 3: User Authentication

...

[Full algorithm continues...]
```

## Test Case 2: Performance Optimization

### Scenario: Optimize Database Queries

```bash
python generate_prompt.py --template-id perf-opt-v1 --start-prompt "The user service in our e-commerce application is experiencing slow response times. Database queries need optimization:
- Current response time: 2-3 seconds
- Target response time: <500ms
- Using PostgreSQL database
- Main bottleneck in user search and filter operations
- Need to maintain existing functionality" --output db_optimization.md
```

### Example Output (db_optimization.md):

```markdown
# Database Optimization Algorithm

## Performance Requirements

Target Component: User Service
Current Performance: 2-3 seconds response time
Target Performance: <500ms response time
Database: PostgreSQL

## Step 1: Environment Setup & Baseline

...

## Step 2: Performance Analysis

...

[Full algorithm continues...]
```

## Test Case 3: Code Review

### Scenario: Security Review of Authentication Module

```bash
python generate_prompt.py --template-id code-review-v1 --start-prompt "Review the authentication module of our Node.js application:
- JWT-based authentication
- Password hashing with bcrypt
- Session management
- Focus on security best practices
- Check for common vulnerabilities (OWASP Top 10)
- Review error handling and logging" --output auth_security_review.md
```

### Example Output (auth_security_review.md):

```markdown
# Authentication Module Security Review

## Review Scope

Component: Authentication Module
Type: Security Review
Framework: Node.js

## Step 1: Initial Setup

...

## Step 2: Security Analysis

...

[Full algorithm continues...]
```

## Test Case 4: Refactoring

### Scenario: Modernize Legacy Code

```bash
python generate_prompt.py --template-id refactor-v1 --start-prompt "Refactor a legacy PHP application to modern standards:
- Current: PHP 5.6 with mixed procedural/OOP code
- Target: PHP 8.1 with proper OOP design
- Implement dependency injection
- Add proper error handling
- Maintain existing functionality
- Must have 90% test coverage" --output php_modernization.md
```

### Example Output (php_modernization.md):

```markdown
# PHP Application Modernization Algorithm

## Refactoring Scope

Current Architecture: PHP 5.6 (mixed procedural/OOP)
Target Architecture: PHP 8.1 (OOP with DI)
Test Coverage Target: 90%

## Step 1: Analysis & Planning

...

## Step 2: Environment Setup

...

[Full algorithm continues...]
```

## Test Case 5: Test Generation

### Scenario: Generate Test Suite for Payment Module

```bash
python generate_prompt.py --template-id test-gen-v1 --start-prompt "Create a comprehensive test suite for the payment processing module:
- Stripe integration
- Multiple payment methods (credit card, PayPal)
- Error handling scenarios
- Transaction rollback tests
- Mock external API calls
- Target: 95% code coverage
- Using Jest for testing" --output payment_tests.md
```

### Example Output (payment_tests.md):

```markdown
# Payment Module Test Generation Algorithm

## Test Requirements

Component: Payment Processing Module
Framework: Jest
Coverage Target: 95%
Integration: Stripe API

## Step 1: Analysis & Planning

...

## Step 2: Test Environment Setup

...

[Full algorithm continues...]
```

## Template Management Examples

### List Available Templates

```bash
python template_manager.py list
```

Example Output:

```
Available Templates:
-------------------

dev-algo-v1:
  Description: Development algorithm for new projects or features
  Path: templates/coding/development_algorithm_v1

perf-opt-v1:
  Description: Performance optimization algorithm
  Path: templates/coding/peformance_optimization_algorithm_v1

[Other templates...]
```

### Create Custom Template

```bash
python template_manager.py create deployment-v1 "Deployment and CI/CD Template" deployment_algorithm_v1
```

Example Output:

```
✅ Created template 'deployment-v1' in templates/coding/deployment_algorithm_v1
```

## Working with Generated Files

1. **File Organization**

   ```bash
   mkdir -p projects/todo_api
   python generate_prompt.py --template-id dev-algo-v1 --start-prompt "..." --output projects/todo_api/development.md
   python generate_prompt.py --template-id test-gen-v1 --start-prompt "..." --output projects/todo_api/tests.md
   ```

2. **Iterative Development**

   ```bash
   # Initial development
   python generate_prompt.py --template-id dev-algo-v1 --start-prompt "..." --output todo_api_v1.md

   # After implementation, optimize
   python generate_prompt.py --template-id perf-opt-v1 --start-prompt "..." --output todo_api_optimization.md

   # Finally, security review
   python generate_prompt.py --template-id code-review-v1 --start-prompt "..." --output todo_api_security.md
   ```

## Best Practices

1. **Output File Naming**

   - Use descriptive names: `user_auth_dev.md`, `payment_perf_opt.md`
   - Include version numbers if iterating: `api_v1.md`, `api_v2.md`
   - Group related files in directories

2. **Output Organization**

   ```
   project/
   ├── development/
   │   ├── api_dev.md
   │   └── frontend_dev.md
   ├── testing/
   │   ├── api_tests.md
   │   └── e2e_tests.md
   └── optimization/
       └── perf_opt.md
   ```

3. **Version Control**
   - Commit generated files with meaningful messages
   - Keep iterations in separate branches
   - Tag significant versions

## Troubleshooting

1. If template generation fails:

   - Check OpenAI API key in .env
   - Verify template ID exists (use `--list`)
   - Make sure prompt is detailed enough

2. If output file issues:

   - Verify write permissions
   - Check if directory exists
   - Use absolute paths if needed

3. If configuration fails:
   - Check template configuration in config_models.py
   - Verify all required fields are provided in prompt
