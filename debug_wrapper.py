#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import List

from scripts.call_module import call_function

_Strs = List[str]


def main() -> bool:
    arguments: _Strs = sys.argv

    if 2 == len(arguments):
        return call_function(arguments[0], arguments[1])

    return True  # TODO: untestable


if __name__ == '__main__':
    sys.exit(not main())
