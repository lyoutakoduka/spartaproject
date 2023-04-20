#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import List

from scripts.same_elements import all_true

_Bools = List[bool]


def pair_true(lefts: _Bools, rights: _Bools) -> bool:
    if 1 != len(set([len(flags) for flags in [lefts, rights]])):
        return False

    return all_true([left == right for left, right in zip(lefts, rights)])


def main() -> bool:
    LEFTS: _Bools = [True, False, True, False, True]
    RIGHTS: _Bools = [True, False, True, False, True]

    result: bool = pair_true(LEFTS, RIGHTS)

    return result


if __name__ == '__main__':
    sys.exit(not main())
