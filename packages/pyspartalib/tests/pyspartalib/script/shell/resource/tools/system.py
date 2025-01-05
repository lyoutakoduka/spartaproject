#!/usr/bin/env python

"""Module to show Python system paths."""

from sys import path

from pyspartalib.script.stdout.logger import show_log


def _main() -> None:
    for text in path:
        show_log(text)


if __name__ == "__main__":
    _main()
