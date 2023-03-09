# shaker-standalone

Shaker is a script that detects flakiness in codebases by introducing noise and load to the execution environment. It currently supports pytest and Maven. For each stress run, it will run the tests once for each one of the 4 stress configurations.

## Usage

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
  -tp TESTS_PATH, --tests-path TESTS_PATH
                        specify the path of the test(s) Shaker will execute
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



### Jest Example

./shaker-js/shaker/shaker.py --stress-runs 1 --no-stress-runs 1 jest "react-styleguidist" --tests-command "yarn test:jest"