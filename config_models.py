from pydantic import BaseModel, Field


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
        ..., description="Project requirements and specifications"
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


class PerfOptConfig(BaseModel):
    project_name: str = Field(..., description="Project name")
    project_codebase: str = Field(..., description="Codebase name (folder/repo)")
    target_component: str = Field(..., description="Component/module to optimize")
    performance_metrics: str = Field(
        ..., description="Key performance metrics to improve"
    )
    baseline_benchmarks: str = Field(..., description="Current performance numbers")
    target_improvements: str = Field(..., description="Target performance improvements")
    profiling_tools: str = Field(..., description="Tools to use for profiling")
    benchmark_script: str = Field(..., description="Script/command to benchmark")
    test_script: str = Field(..., description="Script to run tests")
    environment_setup: str = Field(..., description="Environment setup requirements")
    documentation_folder: str = Field(..., description="Folder for documentation")
    iteration_results_file: str = Field(..., description="Log file for iterations")
    benchmark_results_file: str = Field(..., description="File for benchmark results")
    acceptance_criteria: str = Field(..., description="Performance acceptance criteria")


class CodeReviewConfig(BaseModel):
    project_name: str = Field(..., description="Project name")
    review_scope: str = Field(..., description="Files/components to review")
    review_type: str = Field(
        ..., description="Type of review (security/performance/style)"
    )
    coding_standards: str = Field(..., description="Coding standards to check against")
    lint_script: str = Field(..., description="Script/command to lint")
    test_script: str = Field(..., description="Script to run tests")
    security_checks: str = Field(..., description="Security checks to perform")
    documentation_folder: str = Field(..., description="Folder for documentation")
    review_results_file: str = Field(..., description="File for review results")
    acceptance_criteria: str = Field(..., description="Review acceptance criteria")


class RefactorConfig(BaseModel):
    project_name: str = Field(..., description="Project name")
    refactor_scope: str = Field(..., description="Code scope to refactor")
    current_architecture: str = Field(
        ..., description="Current architecture description"
    )
    target_architecture: str = Field(..., description="Target architecture")
    programming_language: str = Field(..., description="Programming language")
    test_script: str = Field(..., description="Script to run tests")
    lint_script: str = Field(..., description="Script/command to lint")
    format_script: str = Field(..., description="Script/command to autoformat")
    documentation_folder: str = Field(..., description="Folder for documentation")
    iteration_results_file: str = Field(..., description="Log file for iterations")
    acceptance_criteria: str = Field(..., description="Refactoring acceptance criteria")


class TestGenConfig(BaseModel):
    project_name: str = Field(..., description="Project name")
    test_scope: str = Field(..., description="Components to test")
    test_framework: str = Field(..., description="Testing framework to use")
    test_types: str = Field(..., description="Types of tests to generate")
    coverage_targets: str = Field(..., description="Target code coverage")
    test_script: str = Field(..., description="Script to run tests")
    lint_script: str = Field(..., description="Script/command to lint")
    documentation_folder: str = Field(..., description="Folder for documentation")
    test_results_file: str = Field(..., description="File for test results")
    coverage_report_file: str = Field(..., description="File for coverage report")
    acceptance_criteria: str = Field(..., description="Testing acceptance criteria")


# Map template IDs to their config models
CONFIG_MODEL_MAP = {
    "dev-algo-v1": DevConfig,
    "perf-opt-v1": PerfOptConfig,
    "code-review-v1": CodeReviewConfig,
    "refactor-v1": RefactorConfig,
    "test-gen-v1": TestGenConfig,
}
