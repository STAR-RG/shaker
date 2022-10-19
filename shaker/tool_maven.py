import logging
from shutil import copy

from base_tool import BaseTool
from util import subprocess_run


class Maven(BaseTool):
    def setup(self):
        arguments = "--batch-mode --update-snapshots --fail-never  -DskipTests"
        command = f"mvn {arguments} clean install"
        stdout_ = open(self.output_folder /
                       "exec_setup.out", "a")
        stderr_ = open(self.output_folder / "exec_setup.err", "a")
        # print(f"> {command}")
        subprocess_run(command, cwd=str(self.directory),
                       stdout=stdout_, stderr=stderr_)

    def run_tests(self, report_folder):
        if self.tests_path:
            # TODO: Allow users to specify test(s) to run.
            print("Can't specify tests using Maven. Execution will run all tests.")

        command = f"mvn test --fail-never --batch-mode"
        # print(f"> {command}")

        stdout_ = open(self.output_folder /
                       "exec_stress.out", "a")
        stderr_ = open(self.output_folder / "exec_stress.err", "a")

        subprocess_run(command, cwd=str(self.directory),
                       stdout=stdout_, stderr=stderr_)

    def post_tests(self, report_folder):
        # Copy reports
        report_folder.mkdir(parents=True, exist_ok=True)

        reports = self.directory.rglob("TEST-*.xml")

        for report in reports:
            dest = report_folder / report.name
            if report != dest:
                copy(report, dest)
