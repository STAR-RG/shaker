import json
import time
from argparse import ArgumentParser
from requests import get, patch, post, put

# repoUrl = "http://localhost:3000/repos"
# flakiesUrl = "http://localhost:3000/flakies"

repoUrl = "https://my-new-app-denini.herokuapp.com/repos"
flakiesUrl = "https://my-new-app-denini.herokuapp.com/flakies"

parser = ArgumentParser()
parser.add_argument("repo", help="repository")
parser.add_argument("ref", help="repository ref")
parser.add_argument("numtests", type=int, help="number of tests")
parser.add_argument("nsr", type=int, help="specify number of no-stress runs")
parser.add_argument("sr", type=int, help="specify number of stress runs")
args = parser.parse_args()

total_runs = args.nsr + (args.sr * 4)

repoInfo = {"id": args.repo, "ref": args.ref, "numTests": args.numtests}
repoJson = json.loads(json.dumps(repoInfo))
post(repoUrl, json=repoJson)

with open("__results.json") as f:
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

        flake = {
            "repo": repoInfo["id"],
            "module": module,
            "functionName": testCaseName,
            "datetimeEpoch": int(time.time()),
            "ratio": ratio,
        }
        flakeJson = json.loads(json.dumps(flake))
        post(flakiesUrl, json=flakeJson)

if len(module):
    exit(1)
else:
    exit(0)

# / == %2F
