#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for test to execute Python on all platform."""

from platform import uname

from pyspartaproj.script.platform.get_platform import get_platform


def _main() -> None:
    print(get_platform())


if __name__ == "__main__":
    _main()
