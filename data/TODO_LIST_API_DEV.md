# Todo List REST API Development Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged as a cycle in `logs/iteration_results.txt` before proceeding.

## Project Requirements.

`FastAPI-based REST API with CRUD for todos, JWT authentication, SQLite DB, Pydantic validation, error handling, API docs, and unit tests.`

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

**2.1** Scaffold the project using `Python` LTS.
**2.2** Create a `scripts/` folder and add `build.sh`, `clean.sh`, `lint.sh`, `test.sh`.
**2.3** Add minimal boilerplate to enable a “Hello World” build.
**2.4** Run `pytest tests/`.
**2.5** Create all scripts specified in the config mainly build, lint, test and validate if they are not present in the scripts folder or root folder.

- **If PASS:**

  - Log success (step, status, files changed, test status) in `logs/iteration_results.txt`.
  - **Halt execution,** prompt user to commit changes, then on next run start at Step 3.

- **If FAIL:**

  - Log failure (step, files changed, error message) in `logs/iteration_results.txt`.
  - **Halt execution and wait for user to resolve**.

---

### **Step 3: Specification Intake**

**3.1** Parse `spec.md` and `- CRUD endpoints for todos
- JWT user authentication
- SQLite via SQLAlchemy or databases
- Input validation with Pydantic models
- Custom error handling and status codes
- Unit tests with pytest
- Automatic Swagger docs`.
**3.2** Summarize understanding and log in `logs/iteration_results.txt`.
**3.3** Check that all required fields are present and non-empty.

- **If all OK:**

  - Go to Step 4.

- **If missing fields/spec:**

  - Log missing data, halt and wait for user.

---

### **Step 4: Environment Setup**

**4.1** Set up local environment as per `Python 3.10+, pip install -r requirements.txt, set environment variables for JWT secret, FastAPI, SQLAlchemy, Pydantic, pytest.`.
**4.2** Log all actions and file changes.
**4.3** Verify environment by running `pytest tests/` and `flake8 todo_api` (if defined).

- **If both PASS:**

  - Go to Step 5.

- **If any FAIL:**

  - Log failure (step, error), halt and wait for user fix.

---

### **Step 5: Project Structure Validation**

**5.1** Confirm that project structure matches `todo_api/
  main.py
  models.py
  schemas.py
  db.py
  crud.py
  auth.py
  deps.py
  api/
    __init__.py
    endpoints/
      __init__.py
      todos.py
      users.py
tests/
  test_auth.py
  test_todos.py
requirements.txt
spec.md
README.md` (folders, main files, scripts).

- **If matches:**

  - Go to Step 6.

- **If not:**

  - Log missing or extra files/folders, halt for user intervention.

---

### **Step 6: Milestone Loop (Repeat for Each `{milestone}`)**

#### _(Do steps 6.1–6.7 for each milestone in order)_

**6.1** Design the API/interface and key data structures.

- Log the design to `logs/iteration_results.txt`.

**6.2** Implement minimal viable feature for this milestone.

- Log code and files changed.

**6.3** Run `pytest tests/`.

- **If PASS:**

  - Proceed to 6.4.

- **If FAIL:**

  - Log failure, revert last change if possible, go back to 6.2.

**6.4** Run `flake8 todo_api` and/or `black todo_api` if defined.

- **If PASS:**

  - Proceed to 6.5.

- **If FAIL:**

  - Log failure, fix issues, and repeat 6.4.

**6.5** If `` exists for this milestone, run it.

- Log results in `logs/benchmark_results.txt`.
- **If benchmarks meet or exceed requirements:**

  - Proceed to 6.6.

- **If not:**

  - Log failure, optimize, and repeat from 6.2 for this milestone.

**6.6** Add or update documentation in `docs` for new features.

- Log files changed.

**6.7** Mark milestone as complete in `logs/iteration_results.txt` (step, milestone name, status: success, etc.).

- If more milestones, repeat 6.1–6.7 for next milestone.
- If last milestone, go to Step 7.

---

### **Step 7: Test Suite & Final Validation**

**7.1** Run complete `pytest tests/` (all tests, all milestones).

- **If PASS:**

  - Proceed to 7.2.

- **If FAIL:**

  - Log which tests failed, revert last change if needed, and return to last relevant 6.x step.

**7.2** Run `flake8 todo_api` and `black todo_api` for entire project.

- **If PASS:**

  - Proceed to Step 8.

- **If FAIL:**

  - Fix formatting/lint issues, rerun 7.2.

---

### **Step 8: Final Review & Delivery**

**8.1** Confirm all `API exposes correct CRUD endpoints, uses JWT auth, validates data, handles errors properly, persists data in SQLite, tests pass, and Swagger docs available.` are met.

- **If YES:**

  - Package output to `Complete codebase with docs, requirements.txt, and passing unit tests`.
  - Log summary, all key changes, and final status in `logs/iteration_results.txt`.
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

  - Log the full state, error, and attempted action in `logs/iteration_results.txt` (with `"status": "halted"`).
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
- Keep a backup file with `logs/iteration_results.txt_{session_id}` at all times. Generate the session ID at the start of the session and don't use session IDs for iteration results files that are already present. You can start with `session_id` as `0` and then increment.
