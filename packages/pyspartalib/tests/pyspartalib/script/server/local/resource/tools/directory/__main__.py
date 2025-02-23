#!/usr/bin/env python

"""Script to execute Python module from directory tree on server."""

from send_stdout import send_stdout


def _main() -> None:
    for i in range(3):
        send_stdout("directory" + str(i))


if __name__ == "__main__":
    _main()
