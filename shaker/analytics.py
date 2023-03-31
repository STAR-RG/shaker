import json
import time
from argparse import ArgumentParser
from requests import get, patch, post, put
from pathlib import Path

# repoUrl = "http://localhost:3000/repos"
# flakiesUrl = "http://localhost:3000/flakies"

def save_simplified_flakies():
    
    with open(Path('./output/') / "__results.json") as f:
        parser = ArgumentParser()
        parser.add_argument("output_folder", help="output folder")
        parser.add_argument("repo", help="repository")
        parser.add_argument("ref", help="repository ref")
        parser.add_argument("numtests", type=int, help="number of tests")
        parser.add_argument("nsr", type=int, help="specify number of no-stress runs")
        parser.add_argument("sr", type=int, help="specify number of stress runs")
        args = parser.parse_args()

        total_runs = args.nsr + (args.sr * 4)
        
        parser = ArgumentParser()
        parser.add_argument("output_folder", help="output folder")
        parser.add_argument("repo", help="repository")
        parser.add_argument("ref", help="repository ref")
        parser.add_argument("numtests", type=int, help="number of tests")
        parser.add_argument("nsr", type=int, help="specify number of no-stress runs")
        parser.add_argument("sr", type=int, help="specify number of stress runs")
        args = parser.parse_args()

        total_runs = args.nsr + (args.sr * 4)


        repoInfo = {"name": args.repo, "ref": args.ref, "num_tests": args.numtests}
        repoJson = json.loads(json.dumps(repoInfo))
        failures = json.load(f)
        
        for module in failures:
            for test_case in failures[module]:
                testCaseName = test_case

                function_failures = failures[module][test_case]

                no_stress_failures = 0
                stress_failures = 0
                tests_run_configurations_type = 'plain'
                for failure in function_failures:
                    if failure["config"] == "no-stress":
                        no_stress_failures += 1
                    else:
                        tests_run_configurations_type = 'stress'
                        stress_failures += 1
                    flakyPostObject = {
                        "project_name": repoInfo["name"],
                        "project_commit": repoInfo["ref"],
                        "tests_run_configurations_type": tests_run_configurations_type,
                        "run_times": total_runs,
                        "module_name": module,
                        "test_case_name": testCaseName,
                        "created_at": int(time.time()),
                        "test_case_result": failure,
                    }
                    post("https://flakybd-97b53-default-rtdb.firebaseio.com/.json", json=flakyPostObject)
                
                #total_failures = no_stress_failures + stress_failures
                #ratio = total_failures / total_runs
                #flakyJson = json.loads(json.dumps(flaky))
                #flakyPostObject = {
                ##    "repoInfos": repoJson,
                ##    "flakyJson": flakyJson,
                #}

def default_post():
    repoUrl = "https://my-new-app-denini.herokuapp.com/repos"
    flakiesUrl = "https://my-new-app-denini.herokuapp.com/flakies"

    parser = ArgumentParser()
    parser.add_argument("output_folder", help="output folder")
    parser.add_argument("repo", help="repository")
    parser.add_argument("ref", help="repository ref")
    parser.add_argument("numtests", type=int, help="number of tests")
    parser.add_argument("nsr", type=int, help="specify number of no-stress runs")
    parser.add_argument("sr", type=int, help="specify number of stress runs")
    args = parser.parse_args()

    total_runs = args.nsr + (args.sr * 4)

    repoInfo = {"name": args.repo, "ref": args.ref, "num_tests": args.numtests}
    repoJson = json.loads(json.dumps(repoInfo))
    post(repoUrl, json=repoJson)

    with open(Path(args.output_folder) / "__results.json") as f:
        failures = json.load(f)

    # python analytics.py "testing/repo" "1.2" 346 1 2

    for module in failures:
        moduleName = module

        for test_case in failures[module]:
            testCaseName = test_case

            function_failures = failures[module][test_case]

            no_stress_failures = 0
            stress_failures = 0

            for failure in function_failures:
                if failure["config"] == "no-stress":
                    no_stress_failures += 1
                else:
                    stress_failures += 1

            total_failures = no_stress_failures + stress_failures
            ratio = total_failures / total_runs

            flaky = {
                "repo": repoInfo["name"],
                "module": module,
                "function_name": testCaseName,
                "datetime_epoch": int(time.time()),
                "ratio": ratio,
            }
            flakyJson = json.loads(json.dumps(flaky))
            post(flakiesUrl, json=flakyJson)

save_simplified_flakies()
# / == %2F