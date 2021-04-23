from pathlib import Path
from xml.etree import ElementTree


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


"""import json
failures = parse(Path("./output"))
print(json.dumps(failures, indent = 4))
import print_failures
print_failures.print_failures(failures, 1, 1, 4)"""
