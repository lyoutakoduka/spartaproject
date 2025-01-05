#!/usr/bin/env python

"""Module for test to execute Python on all platform."""

from platform import uname

from pyspartalib.script.stdout.logger import show_log


def _get_platform() -> str:
    return uname().system.lower()


def _main() -> None:
    show_log(_get_platform())


if __name__ == "__main__":
    _main()
