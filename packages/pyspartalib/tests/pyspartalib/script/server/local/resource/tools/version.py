#!/usr/bin/env python

"""Script to execute Python module to get Python version on server."""

from sys import version

from pyspartalib.script.stdout.logger import show_log


def _main() -> None:
    show_log(version)


if __name__ == "__main__":
    _main()
