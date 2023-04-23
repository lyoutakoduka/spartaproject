#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

_Bools = List[bool]


def bool_same_array(elements: _Bools) -> bool:
    if 0 == len(elements):
        raise ValueError('empty')

    elements = list(set(elements))

    if 1 != len(elements):
        raise ValueError('true and false')

    if not elements[0]:
        raise ValueError('false')

    return True
