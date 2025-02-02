#!/usr/bin/env python

from collections.abc import Sized

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.bool_context import (
    BoolPair,
    BoolPairs,
    Bools,
    Bools2,
    BoolType,
)
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs, Strs2


def _raise_error(message: str | None) -> None:
    if message is None:
        raise ValueError

    raise ValueError(message)


def _length_error(
    result: Sized,
    expected: int,
    message: str | None = None,
) -> None:
    if len(result) != expected:
        _raise_error(message)


def _same_error(
    result: Type,
    expected: Type,
    message: str | None = None,
) -> None:
    if result == expected:
        _raise_error(message)


def _status_error(status: bool, message: str | None = None) -> None:
    if not status:
        _raise_error(message)


def _get_flag_counts(lefts: BoolType, rights: BoolType) -> Ints:
    return list({len(flags) for flags in [lefts, rights]})


def _check_arguments_size(lefts: BoolType, rights: BoolType) -> None:
    flag_counts: Ints = _get_flag_counts(lefts, rights)

    _length_error(flag_counts, 1, message="size")
    _same_error(flag_counts[0], 0, message="empty")


def _get_sorted_flags(sorted_keys: Strs2, flags_pair: BoolPairs) -> Bools2:
    return [
        [flags[key] for key in keys]
        for keys, flags in zip(sorted_keys, flags_pair, strict=True)
    ]


def _confirm_list_same(lefts: Bools, rights: Bools) -> bool:
    return lefts == rights


def _confirm_list_single(result: Sized) -> bool:
    return len(result) == 1


def _get_sorted_keys(lefts: BoolPair, rights: BoolPair) -> Strs2:
    return [sorted(flags.keys()) for flags in [lefts, rights]]


def _get_key_strings(sorted_keys: Strs2) -> Strs:
    return [str(keys) for keys in sorted_keys]


def bool_compare_array(lefts: Bools, rights: Bools) -> bool:
    _check_arguments_size(lefts, rights)

    return _confirm_list_same(lefts, rights)


def bool_compare_pair(lefts: BoolPair, rights: BoolPair) -> bool:
    _check_arguments_size(lefts, rights)

    sorted_keys: Strs2 = _get_sorted_keys(lefts, rights)

    _length_error(set(_get_key_strings(sorted_keys)), 1, message="unmatch")

    return _confirm_list_single(
        set(_get_sorted_flags(sorted_keys, [lefts, rights])),
    )
