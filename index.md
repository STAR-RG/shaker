# Shaker

Shaker is a script that detects flakiness in codebases by introducing noise and load to the execution environment. It currently supports pytest and Maven. For each stress run, it will run the tests once for each one of the 4 stress configurations.

# GitHub Action

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
    # Tool
    # Currently supported tools: maven, pytest
    # Required
    # Example: testing_tool: maven
    tool: "maven"

    # Pass extra arguments to the tool
    # Optional
    # Example: extra_arguments: -DModule.skip.tests=true
    extra_arguments: ""

    # Number of Shaker runs
    # Optional, default: 3
    # Example: runs: "3"
    runs: "3"
```

## Inputs

| Input | Description |
| --- | --- |
| `tool` | Specifies the tool required to run the tests. Currently supported: `maven` and `pytest`. |
| `extra_arguments` | Optional. Passes extra arguments to the testing tool. For example, you can pass `-DModule.skip.tests=true` to tell Maven to skip a certain module. |
| `runs` | Optional, default: 3. Specifies how many times Shaker will run. |


# CLI Usage
If you want to run a shaker in your environment, just do this:

## Usage
```bash
git clone https://github.com/STAR-RG/shaker
cd shaker # entering the project
cd shaker # entering the CLI
```

```
usage: shaker.py [-h] [-e EXTRA_ARGUMENTS] [-o OUTPUT_FOLDER] [-sr STRESS_RUNS] [-nsr NO_STRESS_RUNS] {pytest,maven} directory

positional arguments:
  {pytest,maven}        specify testing tool
  directory             specify directory

optional arguments:
  -h, --help            show this help message and exit
  -e EXTRA_ARGUMENTS, --extra-arguments EXTRA_ARGUMENTS
                        specify extra arguments
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        specify output folder
  -sr STRESS_RUNS, --stress-runs STRESS_RUNS
                        specify number of stress runs
  -nsr NO_STRESS_RUNS, --no-stress-runs NO_STRESS_RUNS
                        specify number of no-stress runs
```

## Example

In this example, Shaker ran the tests 17 times: 1 no-stress runs and 4 (* 4 configurations) stress runs. The following test passed all no-stress runs but failed 4 stress runs, corresponding to 23.53% out of the 17 runs due to an assertion error. If the same test failed with different issues, the errors will be reported as well.

```
$ ./shaker.py --no-stress-runs 1 --stress-runs 4 maven "project/path"

==== Failure in module com.project.MyModule ====
     > at testExample
       No stress failures: 0 (0.00%)
       Stress failures: 4 (23.53%)

       > Descriptions: 
         java.lang.AssertionError: null
         	at org.testng.Assert.fail(Assert.java:89)
         	at org.testng.Assert.assertNotEquals(Assert.java:739)
         	at org.testng.Assert.assertNotEquals(Assert.java:744)
         	at com.project.MyModule.testExample(MyModule.java:100)
```
