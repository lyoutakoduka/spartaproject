#!/usr/bin/env python

"""Script to execute Python module from file tree on server."""

from pyspartalib.script.stdout.send_stdout import send_stdout


def _main() -> None:
    for i in range(3):
        send_stdout("file" + str(i))


if __name__ == "__main__":
    _main()
