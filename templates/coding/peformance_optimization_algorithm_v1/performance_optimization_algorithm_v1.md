# {PROJECT_NAME} Performance Optimization Algorithm

> **STRICT EXECUTION REQUIRED:**
> All steps must be executed in order. No step may be skipped or merged.
> At every checkpoint, if the result is not as expected, follow the explicit branch.
> Every step and branch must be logged as a cycle in `{iteration_results_file}` before proceeding.

## Performance Optimization Requirements

Target Component: `{target_component}`
Current Performance Metrics: `{baseline_benchmarks}`
Target Improvements: `{target_improvements}`

---

### **Step 1: Environment Setup & Baseline**

**1.1** Set up profiling environment:

- Install required profiling tools: `{profiling_tools}`
- Configure environment variables and settings

**1.2** Run baseline benchmarks:

```bash
{benchmark_script}
```

**1.3** Record baseline metrics in `{benchmark_results_file}`:

- Current performance numbers
- System specifications
- Test conditions

---

### **Step 2: Performance Analysis**

**2.1** Run profiling tools on target component
**2.2** Analyze hotspots and bottlenecks
**2.3** Document findings in `{iteration_results_file}`:

- CPU usage patterns
- Memory allocation/deallocation
- I/O operations
- Network calls
- Database queries

- **If clear bottlenecks found:**

  - Go to Step 3

- **If no clear bottlenecks:**
  - Expand profiling scope
  - Return to 2.1 with wider scope

---

### **Step 3: Optimization Planning**

**3.1** For each identified bottleneck:

- Estimate improvement potential
- List possible optimization strategies
- Assess implementation complexity
- Calculate risk factors

**3.2** Prioritize optimizations based on:

- Impact vs. effort ratio
- Risk level
- Dependencies

**3.3** Document optimization plan in `{iteration_results_file}`

---

### **Step 4: Implementation Loop**

_(Repeat for each optimization)_

**4.1** Implement optimization

- Make minimal required changes
- Add performance logging if needed
- Document changes

**4.2** Run test suite:

```bash
{test_script}
```

- **If tests PASS:**

  - Continue to 4.3

- **If tests FAIL:**
  - Rollback changes
  - Revise optimization approach
  - Return to 4.1

**4.3** Run benchmarks:

```bash
{benchmark_script}
```

**4.4** Compare with baseline:

- **If improved:**

  - Document gains in `{benchmark_results_file}`
  - Continue to next optimization

- **If degraded or no change:**
  - Rollback changes
  - Document findings
  - Try next optimization strategy

---

### **Step 5: Validation**

**5.1** Run final benchmark suite
**5.2** Compare against target metrics:

```
Current: {baseline_benchmarks}
Target:  {target_improvements}
```

- **If targets met:**

  - Document final results
  - Go to Step 6

- **If targets not met:**
  - Identify remaining gaps
  - Return to Step 2 for next iteration

---

### **Step 6: Documentation & Delivery**

**6.1** Update documentation in `{documentation_folder}`:

- Performance improvements achieved
- Optimization strategies used
- Before/after benchmarks
- Known limitations

**6.2** Verify all acceptance criteria:

```
{acceptance_criteria}
```

**6.3** Create final report with:

- Summary of improvements
- Benchmark comparisons
- Future recommendations

---

## **Error Handling and Halts**

- At **any step**, if:

  - A benchmark/test fails unexpectedly
  - System becomes unstable
  - Performance degrades significantly
  - Required tools/permissions unavailable

  **THEN:**

  - Log full state and error in `{iteration_results_file}`
  - Revert any recent changes
  - Halt and wait for user intervention

---

## **Example Iteration Log Entry**

```json
{
  "cycle_id": "opt_7",
  "timestamp": "2024-03-21T15:22:01Z",
  "step": "optimize_memory_allocation",
  "component": "data_processor",
  "baseline_metric": "Memory: 1.2GB, Latency: 250ms",
  "optimized_metric": "Memory: 0.8GB, Latency: 220ms",
  "changes": ["Implemented object pooling", "Reduced temporary allocations"],
  "test_status": "pass",
  "benchmark_status": "improved",
  "next_step": "Continue to next optimization"
}
```
