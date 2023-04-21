#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import List

from scripts.call_module import call_function

_Strs = List[str]


def test() -> bool:
    FUNC_NAME: str = 'test'
    arguments: _Strs = sys.argv

    if 2 == len(arguments):
        return call_function(arguments[0], arguments[1], FUNC_NAME)

    return True


if __name__ == '__main__':
    sys.exit(not test())
