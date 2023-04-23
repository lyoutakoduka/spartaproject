#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict

_Bools = List[bool]
_Ints = List[int]
_Strs = List[str]
_BoolsList = List[_Bools]
_StrsList = List[_Strs]
_BoolPair = Dict[str, bool]
_BoolType = _Bools | _BoolPair


def _check_args_size(lefts: _BoolType, rights: _BoolType) -> None:
    flag_counts: _Ints = list(set([len(flags) for flags in [lefts, rights]]))
    count: int = len(flag_counts)

    if 1 != count:
        raise ValueError('size')

    if 0 == flag_counts[0]:
        raise ValueError('empty')


def bool_compare_array(lefts: _Bools, rights: _Bools) -> bool:
    _check_args_size(lefts, rights)
    return lefts == rights


def bool_compare_pair(lefts: _BoolPair, rights: _BoolPair) -> bool:
    _check_args_size(lefts, rights)

    sorted_keys: _StrsList = [
        sorted(flags.keys())
        for flags in [lefts, rights]
    ]

    if sorted_keys[0] != sorted_keys[1]:
        raise KeyError('unmatch')

    sorted_flags: _BoolsList = [
        [flags[key] for key in keys]
        for keys, flags in zip(sorted_keys, [lefts, rights])
    ]

    return sorted_flags[0] == sorted_flags[1]
