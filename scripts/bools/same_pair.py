#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from scripts.bools.same_array import bool_same_array

_Bools = List[bool]
_Ints = List[int]


def bool_same_pair(lefts: _Bools, rights: _Bools) -> bool:
    counts: _Ints = list(set([len(flags) for flags in [lefts, rights]]))
    count: int = len(counts)

    if 1 != count:
        raise ValueError('size')

    if 0 == counts[0]:
        raise ValueError('empty')

    return bool_same_array([left == right for left, right in zip(lefts, rights)])
