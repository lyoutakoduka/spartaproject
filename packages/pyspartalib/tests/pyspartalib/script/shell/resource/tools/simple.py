#!/usr/bin/env python

"""Module for test to execute specific script in Python."""

from pyspartalib.script.stdout.send_stdout import send_stdout


def _main() -> None:
    send_stdout("simple")


if __name__ == "__main__":
    _main()
