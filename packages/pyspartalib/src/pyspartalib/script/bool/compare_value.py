#!/usr/bin/env python

from pyspartalib.context.default.bool_context import (
    BoolPair,
    BoolPairs,
    Bools,
    Bools2,
    BoolType,
)
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs2


def _size_error(
    expected: int,
    result: Ints,
    message: str | None = None,
) -> None:
    if len(result) != expected:
        raise ValueError(message)


def _zero_error(result: int, message: str | None = None) -> None:
    if result == 0:
        raise ValueError(message)


def _get_flag_counts(lefts: BoolType, rights: BoolType) -> Ints:
    return list({len(flags) for flags in [lefts, rights]})


def _check_arguments_size(lefts: BoolType, rights: BoolType) -> None:
    flag_counts: Ints = _get_flag_counts(lefts, rights)

    _size_error(1, flag_counts, message="size")
    _zero_error(flag_counts[0], message="empty")


def _get_sorted_flags(sorted_keys: Strs2, flags_pair: BoolPairs) -> Bools2:
    return [
        [flags[key] for key in keys]
        for keys, flags in zip(sorted_keys, flags_pair, strict=True)
    ]


def _same_error(lefts: Bools, rights: Bools) -> bool:
    return lefts == rights


def bool_compare_array(lefts: Bools, rights: Bools) -> bool:
    _check_arguments_size(lefts, rights)

    return _same_error(lefts, rights)


def bool_compare_pair(lefts: BoolPair, rights: BoolPair) -> bool:
    _check_arguments_size(lefts, rights)

    flags_pair: BoolPairs = [lefts, rights]
    sorted_keys: Strs2 = [sorted(flags.keys()) for flags in flags_pair]

    if len(set(sorted_keys)) != 1:
        message: str = "unmatch"
        raise KeyError(message)

    return len(set(_get_sorted_flags(sorted_keys, flags_pair))) == 1
