from pathlib import Path

from base_tool import BaseTool
from util import subprocess_run
from shutil import copy

class Pytest(BaseTool):
    def setup(self):
        requirements_file = Path(self.directory / "requirements.txt")

        if requirements_file.exists():
            command = "pip install -r requirements.txt"
            # print(f"> {command}")
            subprocess_run(command, cwd=str(requirements_file.parent))

    def run_tests(self, report_folder):
        report_file = report_folder / "TEST-pytest.xml"

        command = (
            f"pytest {self.tests_path} --junitxml {report_file.absolute()}"
            if self.tests_path else f"pytest --junitxml {report_file.absolute()}"
        )
        # print(f"> {command}")
        subprocess_run(command, cwd=str(self.directory))

    def post_tests(self, report_folder):
        # Copy reports
        report_folder.mkdir(parents=True, exist_ok=True)

        reports = self.directory.rglob("TEST-*.xml")

        for report in reports:
            dest = report_folder / report.name
            if report != dest:
                copy(report, dest)
