#!/bin/sh

git clone --depth 1 https://github.com/marcellocordeiro/shaker-standalone.git ./__shaker
python3 "./__shaker/shaker.py" $INPUT_TESTING_TOOL "." -o "./__shaker_output" -nsr $INPUT_NO_STRESS_RUNS -sr $INPUT_STRESS_RUNS
