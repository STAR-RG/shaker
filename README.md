# shaker-action

This action uses [shaker](shaker) in your GitHub workflow to detect flakiness. If the job ends in failure, flakes were detected and errors will be reported.

# Usage

```yaml
# Checks-out your repository under $GITHUB_WORKSPACE so Shaker can access it
- uses: actions/checkout@v2.3.4
- name: Shaker
  uses: STAR-RG/shaker-action@main
  with:
    # Testing tool
    # Currently supported tools: pytest, maven
    # Required
    # Example: testing_tool: maven
    testing_tool: ""

    # Extra arguments
    # Optional
    # Example: extra_arguments: -q
    extra_arguments: ""

    # Number of no-stress runs
    # Optional, default: 1
    # Example: no_stress_runs: "1"
    no_stress_runs: ""

    # Number of stress runs
    # Optional, default: 3
    # Example: stress_runs: "3"
    stress_runs: ""
```
