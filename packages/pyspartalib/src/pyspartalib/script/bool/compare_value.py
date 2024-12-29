#!/usr/bin/env python

from pyspartalib.context.default.bool_context import (
    BoolPair,
    Bools,
    Bools2,
    BoolType,
)
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs2


def _check_arguments_size(lefts: BoolType, rights: BoolType) -> None:
    flag_counts: Ints = list(set([len(flags) for flags in [lefts, rights]]))
    count: int = len(flag_counts)

    if count != 1:
        raise ValueError("size")

    if flag_counts[0] == 0:
        raise ValueError("empty")


def bool_compare_array(lefts: Bools, rights: Bools) -> bool:
    _check_arguments_size(lefts, rights)
    return lefts == rights


def bool_compare_pair(lefts: BoolPair, rights: BoolPair) -> bool:
    _check_arguments_size(lefts, rights)

    sorted_keys: Strs2 = [sorted(flags.keys()) for flags in [lefts, rights]]

    if sorted_keys[0] != sorted_keys[1]:
        raise KeyError("unmatch")

    sorted_flags: Bools2 = [
        [flags[key] for key in keys]
        for keys, flags in zip(sorted_keys, [lefts, rights])
    ]

    return sorted_flags[0] == sorted_flags[1]
