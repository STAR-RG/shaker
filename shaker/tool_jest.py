from pathlib import Path
from base_tool import BaseTool
from util import subprocess_run

import os

class Jest(BaseTool):

    def add_report_lib(self):
        command = f"yarn add jest-junit"
        stdout_ = open(self.output_folder /
                       "exec_setup.out", "a")
        stderr_ = open(self.output_folder / "exec_setup.err", "a")
        subprocess_run(command, cwd=str(self.directory),
                       stdout=stdout_, stderr=stderr_)

    def setup(self):
        self.add_report_lib()
        arguments = " --force"
        command = f"yarn install{arguments}"
        stdout_ = open(self.output_folder /
                       "exec_setup.out", "a")
        stderr_ = open(self.output_folder / "exec_setup.err", "a")
        subprocess_run(command, cwd=str(self.directory),
                       stdout=stdout_, stderr=stderr_)

    def run_tests(self, report_folder, tests_command):
        string_report = str(report_folder).split('output/')[1]
        string_report = './output/' + string_report[0:len(string_report)]
        env = os.environ.copy()
        env["JEST_JUNIT_UNIQUE_OUTPUT_NAME"] = "true"
        env["JEST_JUNIT_OUTPUT_DIR"] = string_report

        if tests_command == None:
            tests_command = "yarn test"
        command = (
            f"{tests_command} {self.tests_path} --reporters=default --reporters=jest-junit"
            if self.tests_path else f"{tests_command} --reporters=default --reporters=jest-junit"
        )
        stdout_ = open(self.output_folder /
                       "exec_setup.out", "a")
        stderr_ = open(self.output_folder / "exec_setup.err", "a")
        
        subprocess_run(command, stderr=stderr_, stdout=stdout_, cwd=str(self.directory), env=env)
