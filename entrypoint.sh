#!/bin/sh

cp -r "/__shaker" "./"
python3 "./__shaker/shaker.py" $INPUT_TESTING_TOOL "." -o "./__shaker_output" -nsr $INPUT_NO_STRESS_RUNS -sr $INPUT_STRESS_RUNS

#counting the tests
collection=$(find . -type d -name 'surefire-reports')
tests=0
for i in $collection;
do
	for j in $(ls "$i"/*.txt 2> /dev/null);
	do
		h=$(grep -e "Tests run: [0-9]*" "$j" | awk '{print $3}' | sed 's/.$//')
        tests=$(($tests + $h))
    done
done

python3 "./__shaker/analytics.py" $GITHUB_REPOSITORY $GITHUB_SHA $tests $INPUT_NO_STRESS_RUNS $INPUT_STRESS_RUNS
