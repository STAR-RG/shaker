# shaker-action

This action uses [shaker](shaker) in your GitHub workflow to detect flakiness. If the job ends in failure, flakes were detected and errors will be reported.

Shaker supports projects using `maven` or `pytest`.

## Usage

Add the following code to your GitHub Actions workflow configuration

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
    testing_tool: "maven"

    # Pass extra arguments to the tool
    # Optional
    # Example: extra_arguments: -DModule.skip.tests=true
    extra_arguments: ""

    # Number of stress runs
    # Optional, default: 3
    # Example: stress_runs: "3"
    stress_runs: "3"
```

## Inputs

| Input | Description |
| --- | --- |
| `testing_tool` | Specifies the tool required to run the tests. Currently supported: `maven` and `pytest`. |
| `extra_arguments` | Passes extra arguments to the testing tool. For example, you can pass `-DModule.skip.tests=true` to tell Maven to skip a certain module. |
| `stress_runs` | Specifies how many sets of stress runs to be executed. |

## Planned features

- [ ] Android support
- [ ] Gradle support
