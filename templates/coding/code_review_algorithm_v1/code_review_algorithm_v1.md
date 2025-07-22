# {PROJECT_NAME} Code Review Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged in `{review_results_file}` before proceeding.

## Review Scope and Type

Review Scope: `{review_scope}`
Review Type: `{review_type}`
Coding Standards: `{coding_standards}`

---

### **Step 1: Initial Setup**

**1.1** Verify access to all required files/components:

- Source code in review scope
- Test files
- Documentation
- Build scripts

**1.2** Set up review environment:

- Configure linting tools
- Set up security scanning tools (if applicable)
- Prepare review documentation

---

### **Step 2: Static Analysis**

**2.1** Run linting checks:

```bash
{lint_script}
```

**2.2** Document findings for:

- Code style violations
- Potential bugs
- Complexity issues
- Dead code
- Code duplication

**2.3** Run security checks (if applicable):

```bash
{security_checks}
```

- **If critical issues found:**

  - Document in `{review_results_file}`
  - Flag for immediate attention
  - Continue to Step 3

- **If minor/no issues:**
  - Document status
  - Continue to Step 3

---

### **Step 3: Code Quality Review**

**3.1** Review code organization:

- File structure
- Module organization
- Component boundaries
- Dependency management

**3.2** Review code quality aspects:

- Naming conventions
- Function/method length
- Class/module cohesion
- Code complexity
- Error handling
- Memory management
- Resource cleanup

**3.3** Review documentation:

- Inline comments
- Function/class documentation
- API documentation
- README files
- Architecture documents

---

### **Step 4: Functional Review**

**4.1** Run test suite:

```bash
{test_script}
```

**4.2** Review test coverage:

- Unit tests
- Integration tests
- Edge cases
- Error scenarios

**4.3** Verify business logic:

- Requirements compliance
- Edge case handling
- Error scenarios
- Performance considerations

---

### **Step 5: Security Review**

_(If security review is part of `{review_type}`)_

**5.1** Check for security vulnerabilities:

- Input validation
- Authentication/Authorization
- Data encryption
- Secret management
- SQL injection risks
- XSS vulnerabilities
- CSRF protection

**5.2** Review security best practices:

- Password handling
- Session management
- API security
- Data protection
- Logging practices

---

### **Step 6: Performance Review**

_(If performance review is part of `{review_type}`)_

**6.1** Review performance aspects:

- Algorithm efficiency
- Resource usage
- Database queries
- Caching strategy
- Network calls
- Memory management

**6.2** Identify optimization opportunities:

- Algorithmic improvements
- Caching opportunities
- Query optimizations
- Resource pooling

---

### **Step 7: Documentation & Reporting**

**7.1** Compile findings in `{documentation_folder}`:

- Summary of review
- Critical issues
- Recommendations
- Best practices observed
- Areas for improvement

**7.2** Categorize issues:

- Critical (must fix)
- Major (should fix)
- Minor (nice to fix)
- Recommendations

**7.3** Verify against acceptance criteria:

```
{acceptance_criteria}
```

---

## **Error Handling and Halts**

- At **any step**, if:

  - Critical security vulnerability found
  - Major functional issue discovered
  - Access to required files/tools lost
  - System becomes unstable

  **THEN:**

  - Log finding in `{review_results_file}`
  - Flag for immediate attention
  - Continue review if possible, else halt

---

## **Example Review Log Entry**

```json
{
  "review_id": "REV_12",
  "timestamp": "2024-03-21T14:30:00Z",
  "component": "AuthService",
  "review_type": "security",
  "findings": [
    {
      "severity": "critical",
      "category": "security",
      "description": "Plaintext password storage in User model",
      "file": "models/user.py",
      "line": 45,
      "recommendation": "Use password hashing with salt"
    }
  ],
  "status": "needs_immediate_attention",
  "next_steps": "Escalate to security team"
}
```
