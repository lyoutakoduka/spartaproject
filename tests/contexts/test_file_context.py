#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict

from contexts.bool_context import BoolPair
from contexts.float_context import Floats
from contexts.decimal_context import Decimal
from contexts.string_context import Strs
from contexts.path_context import Path
from contexts.file_context import TypeFile, serialize_unknown
from scripts.bools.same_value import bool_same_pair

_KEYS: Strs = ['R', 'G', 'B']
_NUMBERS: Floats = [-1.0, 0.0, 1.0]


def test_adapt() -> None:
    INPUT: TypeFile = [Path('R'), Decimal('1.0')]
    EXPECTED: TypeFile = ['R', 1.0,]

    assert EXPECTED == serialize_unknown(INPUT)


def test_array() -> None:
    INPUT: TypeFile = [
        [Path(number) for number in _KEYS],
        [Decimal(str(number)) for number in _NUMBERS],
    ]

    EXPECTED: TypeFile = [
        _KEYS,
        _NUMBERS,
    ]

    assert EXPECTED == serialize_unknown(INPUT)


def _check_result_same(expected: TypeFile, results: TypeFile) -> BoolPair:
    match_result: BoolPair = {}

    if isinstance(results, List) and isinstance(expected, List):
        for i, result in enumerate(results):
            expected_inside: TypeFile = expected[i]

            if isinstance(result, Dict) and isinstance(expected_inside, Dict):
                for key, value in result.items():
                    match_result[key] = value == expected_inside[key]

    return match_result


def test_pair() -> None:
    VALUES: Strs = ['a', 'b', 'c']

    INPUT: TypeFile = [
        {key: Path(value) for key, value in zip(_KEYS, VALUES)},
        {key: Decimal(str(value)) for key, value in zip(_KEYS, _NUMBERS)},
    ]

    EXPECTED: TypeFile = [
        {key: value for key, value in zip(_KEYS, VALUES)},
        {key: value for key, value in zip(_KEYS, _NUMBERS)},
    ]

    results: TypeFile = serialize_unknown(INPUT)
    match_result: BoolPair = _check_result_same(EXPECTED, results)

    assert bool_same_pair(match_result)


def main() -> bool:
    test_adapt()
    test_array()
    test_pair()
    return True
