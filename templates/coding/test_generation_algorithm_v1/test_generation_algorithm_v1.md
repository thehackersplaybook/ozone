# {PROJECT_NAME} Test Generation Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged in `{test_results_file}` before proceeding.

## Test Generation Scope

Test Scope: `{test_scope}`
Test Framework: `{test_framework}`
Test Types: `{test_types}`
Coverage Targets: `{coverage_targets}`

---

### **Step 1: Analysis & Planning**

**1.1** Analyze test requirements:

- Components to test
- Test types needed
- Coverage requirements
- Performance criteria

**1.2** Review existing tests:

- Current coverage
- Test patterns
- Known gaps
- Test quality

**1.3** Create test plan:

- Test hierarchy
- Test categories
- Mocking strategy
- Data requirements

---

### **Step 2: Environment Setup**

**2.1** Configure test environment:

- Install test framework
- Set up test runners
- Configure coverage tools
- Set up mocking framework

**2.2** Create test structure:

- Test directories
- Helper modules
- Fixtures
- Mock data

---

### **Step 3: Test Generation Loop**

_(Repeat for each component)_

**3.1** Generate unit tests:

- Function/method tests
- Class tests
- Edge cases
- Error scenarios

**3.2** Generate integration tests:

- Component interaction
- API contracts
- Data flow
- Error handling

**3.3** Generate end-to-end tests:

- User workflows
- System integration
- Performance scenarios

**3.4** Run test suite:

```bash
{test_script}
```

- **If tests PASS:**

  - Run linter:

  ```bash
  {lint_script}
  ```

  - If linter passes, continue to 3.5
  - If linter fails, fix and repeat 3.4

- **If tests FAIL:**
  - Debug failures
  - Fix test issues
  - Return to relevant test generation step

**3.5** Document in `{test_results_file}`:

- Tests added
- Coverage metrics
- Known limitations
- TODOs

---

### **Step 4: Coverage Analysis**

**4.1** Generate coverage report:

- Line coverage
- Branch coverage
- Function coverage
- Complexity coverage

**4.2** Compare with targets:

```
Required: {coverage_targets}
```

**4.3** Document in `{coverage_report_file}`:

- Coverage metrics
- Uncovered areas
- Risk assessment
- Recommendations

- **If targets met:**

  - Continue to Step 5

- **If targets not met:**
  - Identify gaps
  - Return to Step 3 for missing coverage

---

### **Step 5: Test Quality Review**

**5.1** Review test quality:

- Test readability
- Maintainability
- Performance
- Reliability

**5.2** Verify test characteristics:

- Independence
- Repeatability
- Self-validation
- Timeliness
- Isolation

**5.3** Optimize test suite:

- Remove redundant tests
- Combine similar tests
- Improve test speed
- Enhance readability

---

### **Step 6: Documentation**

**6.1** Update test documentation in `{documentation_folder}`:

- Test strategy
- Test patterns
- Setup instructions
- Maintenance guide

**6.2** Document in test files:

- Test purpose
- Test data
- Assumptions
- Known limitations

**6.3** Verify acceptance criteria:

```
{acceptance_criteria}
```

---

## **Error Handling and Halts**

- At **any step**, if:

  - Test framework fails
  - Coverage tools error
  - System under test unavailable
  - Critical test failures

  **THEN:**

  - Log state in `{test_results_file}`
  - Document error conditions
  - Halt for review if needed

---

## **Example Test Results Entry**

```json
{
  "test_suite_id": "TS_45",
  "timestamp": "2024-03-21T17:15:00Z",
  "component": "OrderService",
  "test_stats": {
    "total_tests": 89,
    "passed": 89,
    "coverage": {
      "lines": "92%",
      "branches": "87%",
      "functions": "95%"
    }
  },
  "new_tests_added": [
    "test_order_validation_edge_cases",
    "test_concurrent_order_processing",
    "test_order_rollback_scenarios"
  ],
  "status": "completed",
  "next_component": "InventoryService"
}
```
