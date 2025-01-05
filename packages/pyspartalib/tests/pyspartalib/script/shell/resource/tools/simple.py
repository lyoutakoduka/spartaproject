#!/usr/bin/env python

"""Module for test to execute specific script in Python."""

from pyspartalib.script.stdout.logger import show_log


def _main() -> None:
    show_log("simple")


if __name__ == "__main__":
    _main()
