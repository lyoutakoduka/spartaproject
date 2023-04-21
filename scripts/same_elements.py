#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

_Bools = List[bool]


def all_true(elements: _Bools) -> bool:
    elements = list(set(elements))
    return 1 == len(elements) and elements[0]
