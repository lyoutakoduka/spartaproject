#!/usr/bin/env python

"""Script to execute Python module from file tree on server."""

from pyspartalib.script.stdout.logger import show_log


def _main() -> None:
    for i in range(3):
        show_log("file" + str(i))


if __name__ == "__main__":
    _main()
