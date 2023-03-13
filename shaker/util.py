from shlex import split
from subprocess import DEVNULL, Popen, run


def subprocess_run(command, stdout=DEVNULL, stderr=DEVNULL, cwd=None, env=None):
    args = split(command)

    return run(args, stdout=stdout, stderr=stderr,  cwd=cwd, env=env)


def subprocess_Popen(command, stdout=DEVNULL, stderr=DEVNULL, cwd=None):
    args = split(command)

    return Popen(args, stdout=stdout, stderr=stderr, cwd=cwd)
