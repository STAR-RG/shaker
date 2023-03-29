from pathlib import Path
from base_tool import BaseTool
from util import subprocess_run

class Karma(BaseTool):

    def add_report_lib(self):
        command = f"yarn add karma-junit-reporter"
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
    
        #out_put = '\\output\\'
        #string_report = str(report_folder).split(out_put)[1]
        #string_report = string_report[0:len(string_report)] + '.xml'
        #env_ = os.environ.copy()
        #env_["JEST_JUNIT_UNIQUE_OUTPUT_NAME"] = "true"
        #env_["JEST_JUNIT_OUTPUT_DIR"] = string_report

        command = (
            f"{tests_command} {self.tests_path} --reporters=default --reporters=junit --outputFile=${string_report} --outputDir='./logs'"
            if self.tests_path else f"{tests_command} --reporters=default --reporters=junit --outputFile=${string_report} --outputDir='./logs'"
        )
        stdout_ = open(self.output_folder /
                       "exec_setup.out", "a")
        stderr_ = open(self.output_folder / "exec_setup.err", "a")
        
        subprocess_run(command, stderr=stderr_, stdout=stdout_, cwd=str(self.directory), env=None)
