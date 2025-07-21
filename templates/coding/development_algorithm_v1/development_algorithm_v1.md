# {PROJECT_NAME} Development Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged as a cycle in `{iteration_results_file}` before proceeding.

## Project Requirements.

`{project_requirements}`

---

### **Step 1: Initialization**

**1.1** Check if the project folder is empty or uninitialized.

- **If YES:**

  - Go to Step 2 (“Project Scaffold”).

- **If NO:**

  - Go to Step 3 (“Spec Intake”).

---

### **Step 2: Project Scaffold**

_(Fresh Project Only)_

**2.1** Scaffold the project using `{programming_language}` LTS.
**2.2** Create a `scripts/` folder and add `build.sh`, `clean.sh`, `lint.sh`, `test.sh`.
**2.3** Add minimal boilerplate to enable a “Hello World” build.
**2.4** Run `{test_script}`.
**2.5** Create all scripts specified in the config mainly build, lint, test and validate if they are not present in the scripts folder or root folder.

- **If PASS:**

  - Log success (step, status, files changed, test status) in `{iteration_results_file}`.
  - **Halt execution,** prompt user to commit changes, then on next run start at Step 3.

- **If FAIL:**

  - Log failure (step, files changed, error message) in `{iteration_results_file}`.
  - **Halt execution and wait for user to resolve**.

---

### **Step 3: Specification Intake**

**3.1** Parse `{project_spec}` and `{requirements}`.
**3.2** Summarize understanding and log in `{iteration_results_file}`.
**3.3** Check that all required fields are present and non-empty.

- **If all OK:**

  - Go to Step 4.

- **If missing fields/spec:**

  - Log missing data, halt and wait for user.

---

### **Step 4: Environment Setup**

**4.1** Set up local environment as per `{environment_setup}`.
**4.2** Log all actions and file changes.
**4.3** Verify environment by running `{test_script}` and `{lint_script}` (if defined).

- **If both PASS:**

  - Go to Step 5.

- **If any FAIL:**

  - Log failure (step, error), halt and wait for user fix.

---

### **Step 5: Project Structure Validation**

**5.1** Confirm that project structure matches `{scaffold_spec}` (folders, main files, scripts).

- **If matches:**

  - Go to Step 6.

- **If not:**

  - Log missing or extra files/folders, halt for user intervention.

---

### **Step 6: Milestone Loop (Repeat for Each `{milestone}`)**

#### _(Do steps 6.1–6.7 for each milestone in order)_

**6.1** Design the API/interface and key data structures.

- Log the design to `{iteration_results_file}`.

**6.2** Implement minimal viable feature for this milestone.

- Log code and files changed.

**6.3** Run `{test_script}`.

- **If PASS:**

  - Proceed to 6.4.

- **If FAIL:**

  - Log failure, revert last change if possible, go back to 6.2.

**6.4** Run `{lint_script}` and/or `{format_script}` if defined.

- **If PASS:**

  - Proceed to 6.5.

- **If FAIL:**

  - Log failure, fix issues, and repeat 6.4.

**6.5** If `{benchmark_script}` exists for this milestone, run it.

- Log results in `{benchmark_results_file}`.
- **If benchmarks meet or exceed requirements:**

  - Proceed to 6.6.

- **If not:**

  - Log failure, optimize, and repeat from 6.2 for this milestone.

**6.6** Add or update documentation in `{documentation_folder}` for new features.

- Log files changed.

**6.7** Mark milestone as complete in `{iteration_results_file}` (step, milestone name, status: success, etc.).

- If more milestones, repeat 6.1–6.7 for next milestone.
- If last milestone, go to Step 7.

---

### **Step 7: Test Suite & Final Validation**

**7.1** Run complete `{test_script}` (all tests, all milestones).

- **If PASS:**

  - Proceed to 7.2.

- **If FAIL:**

  - Log which tests failed, revert last change if needed, and return to last relevant 6.x step.

**7.2** Run `{lint_script}` and `{format_script}` for entire project.

- **If PASS:**

  - Proceed to Step 8.

- **If FAIL:**

  - Fix formatting/lint issues, rerun 7.2.

---

### **Step 8: Final Review & Delivery**

**8.1** Confirm all `{acceptance_criteria}` are met.

- **If YES:**

  - Package output to `{deliverable}`.
  - Log summary, all key changes, and final status in `{iteration_results_file}`.
  - **Halt and notify user to review and commit.**

- **If NO:**

  - Log which acceptance criteria failed, return to the appropriate 6.x or 7.x step as needed.

---

## **Error Handling and Halts**

- At **any step**, if:

  - A command/script fails due to unknown reasons or you get stuck, or required file is missing,
  - Required user input/spec is missing,
  - An unexpected error occurs,

  **THEN:**

  - Log the full state, error, and attempted action in `{iteration_results_file}` (with `"status": "halted"`).
  - Halt all further steps and **wait for user**.

---

## **Example Iteration Log Entry**

```json
{
  "cycle_id": 12,
  "timestamp": "2025-07-21T18:22:01Z",
  "step": "milestone_3_implement_feature",
  "status": "fail",
  "milestone": "Add Redis backend",
  "state": "Implemented Redis adapter, but integration tests failed on reconnection logic.",
  "change": "Added redis_adapter.go, updated main.go",
  "test_status": "fail",
  "files_modified": ["internal/redis_adapter.go", "main.go"],
  "error_message": "Test 'TestRedisReconnection' failed: connection timeout",
  "next_step": "Return to 6.2 for this milestone"
}
```

---

## **Key Principles**

- All **success/failure/branching decisions** are strictly dictated by algorithm.
- **No improvisation, merging, or skipping.**
- **Every step, success, error, and recovery is logged and handled as described.**
- Keep a backup file with `{iteration_results_file}_{session_id}` at all times. Generate the session ID at the start of the session and don't use session IDs for iteration results files that are already present. You can start with `session_id` as `0` and then increment.
