#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from sys import exit, argv

from contexts.string_context import Strs
from scripts.call_module import call_function


def main() -> bool:
    arguments: Strs = argv

    if 2 == len(arguments):
        return call_function(Path(arguments[0]), Path(arguments[1]))

    return True  # TODO: untestable


if __name__ == '__main__':
    exit(not main())
