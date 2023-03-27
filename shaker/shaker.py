#!/usr/bin/env python3

import json
import logging
from argparse import ArgumentParser
from pathlib import Path
from time import sleep

import failure_parser
from print_failures import print_failures
# tools
from tool_maven import Maven
from tool_pytest import Pytest
from tool_jest import Jest
from tool_karma import Karma

def main(args):
    tools = {"pytest": Pytest, "maven": Maven , "jest": Jest, "karma": Karma }

    # Environment setup
    directory = Path(args.directory)
    extra_arguments = args.extra_arguments
    output_folder = Path(
        args.output_folder if args.output_folder else "./output")
    no_stress_runs = args.no_stress_runs
    stress_runs = args.stress_runs
    config_file = Path(__file__).parent / "stressConfigurations.json"
    tests_path = args.tests_path

    with open(config_file) as json_file:
        configs = json.load(json_file)

    # Construct tool object and set it up
    tool = tools[args.tool](directory, extra_arguments, configs, output_folder, tests_path)

    logging.basicConfig(level=logging.DEBUG)
    logging.info(
        f"Running {args.tool} with {no_stress_runs} no-stress runs and {stress_runs} stress runs..."
    )

    sleep(2)

    tests_command = args.tests_command

    # Run tests
    for i in range(0, no_stress_runs):
        tool.no_stress(i, tests_command)

    for i in range(0, stress_runs):
        tool.stress(i, tests_command)

    # Show results
    failures = failure_parser.parse(output_folder)
    with open(output_folder / "__results.json", "w") as f:
        json.dump(failures, f)

    if len(failures) != 0:
        print_failures(failures, no_stress_runs, stress_runs, 4)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "tool", choices=["pytest", "maven", "jest", "karma"], help="specify testing tool"
    )
    parser.add_argument("directory", help="specify directory")
    parser.add_argument("-e", "--extra-arguments",
                        help="specify extra arguments")
    parser.add_argument("-o", "--output-folder", help="specify output folder")
    parser.add_argument(
        "-sr",
        "--stress-runs",
        type=int,
        default=3,
        help="specify number of stress runs",
    )
    parser.add_argument(
        "-nsr",
        "--no-stress-runs",
        type=int,
        default=0,
        help="specify number of no-stress runs",
    )

    parser.add_argument(
        "-tp",
        "--tests-path",
        help="specify the path of the test you want Shaker to run",
    )

    parser.add_argument(
        "-tc",
        "--tests-command",
        default="yarn test",
        type=str,
        help="specify the command to tun tests you want Flaky Forcer to run",
    )

    args = parser.parse_args()

    main(args)
