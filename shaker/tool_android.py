import logging
from shutil import copy

from base_tool import BaseTool
from util import subprocess_run
from util import subprocess_adb


class Android(BaseTool):
    def setup(self):
        # TODO
        # check if `adb shell getprop sys.boot_completed` not return "error: no devices/emulators found"
        return 0

    def run_tests(self, report_folder):
        file_input = open("../inputs/test_run.txt")

        stdout_ = open(self.output_folder / "exec.out", "w")
        stderr_ = open(self.output_folder / "exec.err", "w")

        # for each command
        for command in file_input.readlines():
            print(f"--Using test command: {command}")

            ''' subprocess_adb(
                "adb shell settings put global transition_animation_scale 1")
            subprocess_adb(
                "adb shell settings put global window_animation_scale 1")
             subprocess_adb(
               "adb shell settings put global animator_duration_scale 1")
            '''
            subprocess_run(command, cwd=str(self.directory),
                           stdout=stdout_, stderr=stderr_)

    def post_tests(self, report_folder):
        # Copy reports
        report_folder.mkdir(parents=True, exist_ok=True)

        copy(self.output_folder / "exec.out", report_folder)
