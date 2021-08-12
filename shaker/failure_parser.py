from pathlib import Path
from xml.etree import ElementTree
showln = True


def order(entry):
    # Sort by configuration then run number
    if entry["config"] == "no-stress":
        return (-1, int(entry["run_number"]))
    else:
        return (int(entry["config"]), int(entry["run_number"]))


# Parses all xml files in the project folder
def parse(dir):
    failures = dict()

    for sub_directory in dir.iterdir():
        if not sub_directory.is_dir():
            continue

        # report.configuration.run_number
        config = sub_directory.name.split(".")[1].strip()
        run_number = sub_directory.name.split(".")[2].strip()

        xml_files = sub_directory.glob("*.xml")

        for xml_file in xml_files:
            root = ElementTree.parse(xml_file).getroot()

            testcases = root.findall("testcase")

            if testcases == []:
                testcases = root.findall("testsuite/testcase")

            for testcase in testcases:
                attributes = testcase.attrib

                class_name = attributes["classname"].strip()
                name = attributes["name"].strip()

                for failure in testcase.findall("failure"):
                    description = failure.text.strip()

                    key = class_name
                    key2 = name
                    value = [
                        {
                            "config": config,
                            "run_number": run_number,
                            "description": description,
                        }
                    ]

                    if key not in failures:
                        failures[key] = dict()
                        failures[key][key2] = value
                    else:
                        if key2 not in failures[key]:
                            failures[key][key2] = value
                        else:
                            failures[key][key2].extend(value)

    for key in failures:
        for key2 in failures[key]:
            failures[key][key2].sort(key=order)

    return failures


def parse_android(dir):
    # print("end")
    # exit(0)

    for sub_directory in dir.iterdir():
        if not sub_directory.is_dir():
            continue

        # report.configuration.run_number
        failures = dict()
        testsFails = dict()
        config = sub_directory.name.split(".")[1].strip()
        run_number = sub_directory.name.split(".")[2].strip()

        out_txt_files = sub_directory.glob(f"exec.out")

        for out_txt_file in out_txt_files:
            with open(out_txt_file, "r") as reader:
                ln = 0
                for line in reader:
                    lastName = ''
                    ln = ln + 1
                    stripped_line = line.strip()
                    if stripped_line == 'INSTRUMENTATION_RESULT: stream=':
                        print(f'linha {ln}')  # if is log for tests fails
                        count = 1
                        for line in reader:
                            ln = ln + 1
                            stripped_line = line.strip()
                            if stripped_line.startswith('INS'):
                                break  # leaves the inner loop
                            failLine = f'{count}) '
                            if stripped_line.startswith(failLine):
                                count += 1
                                if showln:
                                    print('line %d -> fail: %s' %
                                          (ln, stripped_line))
                                test = line[3:]  # retire the '1) '
                                test = test.strip()  # for cases '10) '
                                position = test.index('(')
                                # remove the package for test name
                                test = test[:position]
                                try:
                                    testsFails[test] += 1
                                except KeyError as _:
                                    testsFails[test] = 1

        with open(sub_directory / "___results.csv", 'w') as f:
            n = len(testsFails.keys()) / 42
            f.write(f"{n}")
    return testsFails


"""import json
failures = parse(Path("./output"))
print(json.dumps(failures, indent = 4))
import print_failures
print_failures.print_failures(failures, 1, 1, 4)"""
