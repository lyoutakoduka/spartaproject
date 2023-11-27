#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for test to execute Python on all platform."""

from platform import uname


def _main() -> None:
    print(uname().system)


if __name__ == "__main__":
    _main()
