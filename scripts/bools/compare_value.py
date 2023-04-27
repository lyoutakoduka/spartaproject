#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools, BoolPair, BoolsList, BoolType
from contexts.integer_context import Ints
from contexts.string_context import StrList


def _check_args_size(lefts: BoolType, rights: BoolType) -> None:
    flag_counts: Ints = list(set([len(flags) for flags in [lefts, rights]]))
    count: int = len(flag_counts)

    if 1 != count:
        raise ValueError('size')

    if 0 == flag_counts[0]:
        raise ValueError('empty')


def bool_compare_array(lefts: Bools, rights: Bools) -> bool:
    _check_args_size(lefts, rights)
    return lefts == rights


def bool_compare_pair(lefts: BoolPair, rights: BoolPair) -> bool:
    _check_args_size(lefts, rights)

    sorted_keys: StrList = [
        sorted(flags.keys())
        for flags in [lefts, rights]
    ]

    if sorted_keys[0] != sorted_keys[1]:
        raise KeyError('unmatch')

    sorted_flags: BoolsList = [
        [flags[key] for key in keys]
        for keys, flags in zip(sorted_keys, [lefts, rights])
    ]

    return sorted_flags[0] == sorted_flags[1]
