# {PROJECT_NAME} Refactoring Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged in `{iteration_results_file}` before proceeding.

## Refactoring Scope

Target Scope: `{refactor_scope}`
Current Architecture: `{current_architecture}`
Target Architecture: `{target_architecture}`
Programming Language: `{programming_language}`

---

### **Step 1: Analysis & Planning**

**1.1** Document current state:

- Code structure
- Dependencies
- Technical debt
- Known issues

**1.2** Create refactoring plan:

- Identify components to refactor
- Define migration strategy
- List potential risks
- Set up success metrics

**1.3** Set up test baseline:

```bash
{test_script}
```

- Record test coverage and results
- Document performance metrics
- Note any failing tests

---

### **Step 2: Environment Setup**

**2.1** Create refactoring branch
**2.2** Set up development environment:

- Install required tools
- Configure linters
- Set up automated tests

**2.3** Create backup/rollback points

---

### **Step 3: Incremental Refactoring Loop**

_(Repeat for each component)_

**3.1** Select next component to refactor:

- Start with least dependent components
- Follow dependency order
- Document component boundaries

**3.2** Apply refactoring patterns:

- Extract methods/classes
- Improve naming
- Reduce complexity
- Update interfaces
- Migrate to target architecture

**3.3** Run tests:

```bash
{test_script}
```

- **If tests PASS:**

  - Run linter:

  ```bash
  {lint_script}
  ```

  - If linter passes, continue to 3.4
  - If linter fails, fix and repeat 3.3

- **If tests FAIL:**
  - Document failures
  - Rollback changes
  - Revise approach
  - Return to 3.2

**3.4** Run formatter:

```bash
{format_script}
```

**3.5** Document changes in `{iteration_results_file}`:

- What was refactored
- Patterns applied
- Test results
- Known impacts

---

### **Step 4: Integration Testing**

**4.1** Run full test suite:

```bash
{test_script}
```

**4.2** Verify integration points:

- API compatibility
- Data flow
- Event handling
- Error scenarios

**4.3** Performance testing:

- Response times
- Resource usage
- Scalability checks

- **If all tests PASS:**

  - Continue to Step 5

- **If any tests FAIL:**
  - Document issues
  - Return to Step 3 for affected components

---

### **Step 5: Documentation Update**

**5.1** Update technical documentation in `{documentation_folder}`:

- Architecture changes
- API changes
- Migration guides
- Known issues

**5.2** Update:

- README files
- API documentation
- Configuration guides
- Deployment instructions

---

### **Step 6: Validation & Acceptance**

**6.1** Verify acceptance criteria:

```
{acceptance_criteria}
```

**6.2** Final validation:

- Code quality metrics
- Test coverage
- Performance metrics
- Documentation completeness

- **If criteria met:**

  - Prepare for merge
  - Document completion

- **If criteria not met:**
  - Document gaps
  - Return to appropriate step

---

## **Error Handling and Halts**

- At **any step**, if:

  - Critical functionality breaks
  - Tests cannot be fixed
  - Integration issues found
  - Performance degrades significantly

  **THEN:**

  - Log state in `{iteration_results_file}`
  - Rollback to last stable point
  - Reassess approach
  - Halt for review if needed

---

## **Example Iteration Log Entry**

```json
{
  "refactor_id": "REF_23",
  "timestamp": "2024-03-21T16:45:00Z",
  "component": "PaymentProcessor",
  "changes": [
    "Extracted payment validation to separate class",
    "Implemented Strategy pattern for payment methods",
    "Reduced cyclomatic complexity from 15 to 8"
  ],
  "test_results": {
    "total": 127,
    "passed": 127,
    "coverage": "94%"
  },
  "status": "completed",
  "next_component": "OrderService"
}
```
