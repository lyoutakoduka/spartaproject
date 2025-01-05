#!/usr/bin/env python

"""Module for test to execute Python on all platform."""

from platform import uname


def _get_platform() -> str:
    return uname().system.lower()


def _main() -> None:
    print(_get_platform())


if __name__ == "__main__":
    _main()
