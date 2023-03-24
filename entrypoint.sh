#!/bin/sh

cp -r "/__shaker" "./"
python3 "./__shaker/shaker.py" $INPUT_TOOL "." -o "$INPUT_OUTPUT_FOLDER" -nsr $INPUT_NO_STRESS_RUNS -sr $INPUT_RUNS -tc "$INPUT_TESTS_COMMAND"
ret=$?

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

fileresult="./output/__results.json"
cat $fileresult
result=$(<$fileresult)

python3 "./__shaker/analytics.py" "./__shaker_output" $GITHUB_REPOSITORY $GITHUB_SHA $tests $INPUT_NO_STRESS_RUNS $INPUT_RUNS

exit $ret