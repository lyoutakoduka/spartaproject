#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for test to execute specific script in Python."""

from pyspartalib.script.string.temporary_text import temporary_text


def _main() -> None:
    for test in temporary_text(3, 3):
        print(test)


if __name__ == "__main__":
    _main()
