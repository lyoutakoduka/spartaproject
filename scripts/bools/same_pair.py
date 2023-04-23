#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from scripts.bools.same_array import all_true

_Bools = List[bool]
_Ints = List[int]


def pair_true(lefts: _Bools, rights: _Bools) -> bool:
    counts: _Ints = list(set([len(flags) for flags in [lefts, rights]]))
    count: int = len(counts)

    if 1 != count:
        raise ValueError('size')

    if 0 == counts[0]:
        raise ValueError('empty')

    return all_true([left == right for left, right in zip(lefts, rights)])
