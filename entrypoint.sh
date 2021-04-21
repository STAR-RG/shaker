#!/bin/sh

git clone --depth 1 https://github.com/marcellocordeiro/stress-script.git ./__stress_script
python3 "./__stress_script/shaker.py" $INPUT_TESTING_TOOL "." -o "./__stress_output" -nsr $INPUT_NO_STRESS_RUNS -sr $INPUT_STRESS_RUNS
