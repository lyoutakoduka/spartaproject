#!/usr/bin/env python

"""Module to show Python system paths."""

from sys import path

from pyspartalib.script.stdout.send_stdout import send_stdout


def _main() -> None:
    for text in path:
        send_stdout(text)


if __name__ == "__main__":
    _main()
