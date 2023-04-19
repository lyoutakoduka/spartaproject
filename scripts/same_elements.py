#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import List

_Flag = List[bool]


def all_true(elements: _Flag) -> bool:
    elements = list(set(elements))
    return 1 == len(elements) and elements[0]


def main() -> bool:
    result: bool = all_true([
        0 == 0,
        '1' == '1',
        True == True,
        2.0 == 2.0,
    ])

    return result


if __name__ == '__main__':
    sys.exit(not main())
