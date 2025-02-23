#!/usr/bin/env python

"""Script to execute Python module to get Python version on server."""

from sys import version


def _main() -> None:
    print(version)  # noqa: T201


if __name__ == "__main__":
    _main()
