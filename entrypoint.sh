#!/bin/sh

cp -r "/__shaker" "./"
python3 "./__shaker/shaker.py" $INPUT_TESTING_TOOL "." -o "./__shaker_output" -nsr $INPUT_NO_STRESS_RUNS -sr $INPUT_STRESS_RUNS
python3 "./__shaker/analytics.py" $GITHUB_REPOSITORY $GITHUB_SHA 1 $INPUT_NO_STRESS_RUNS $INPUT_STRESS_RUNS
