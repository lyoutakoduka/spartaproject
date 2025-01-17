#!/usr/bin/env python

"""Module for test to execute Python on all platform."""

from platform import uname

from pyspartalib.script.stdout.send_stdout import send_stdout


def _get_platform() -> str:
    return uname().system.lower()


def _main() -> None:
    send_stdout(_get_platform())


if __name__ == "__main__":
    _main()
