#!/usr/bin/env python

"""Script to execute Python module to get Python version on server."""

from sys import version

from pyspartalib.script.stdout.send_stdout import send_stdout


def _main() -> None:
    send_stdout(version)


if __name__ == "__main__":
    _main()
