#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict

from contexts.bool_context import BoolPair
from contexts.float_context import Floats
from contexts.decimal_context import Decimal
from contexts.string_context import Strs
from contexts.path_context import Path
from contexts.json_context import TypeJson, serialize_json
from scripts.bools.same_value import bool_same_pair

_KEYS: Strs = ['R', 'G', 'B']
_NUMBERS: Floats = [-1.0, 0.0, 1.0]


def test_adapt() -> None:
    INPUT: TypeJson = [Path('R'), Decimal('1.0')]
    EXPECTED: TypeJson = ['R', 1.0,]

    assert EXPECTED == serialize_json(INPUT)


def test_array() -> None:
    INPUT: TypeJson = [
        [Path(number) for number in _KEYS],
        [Decimal(str(number)) for number in _NUMBERS],
    ]

    EXPECTED: TypeJson = [
        _KEYS,
        _NUMBERS,
    ]

    assert EXPECTED == serialize_json(INPUT)


def _check_result_same(expected: TypeJson, results: TypeJson) -> BoolPair:
    match_result: BoolPair = {}

    if isinstance(results, List) and isinstance(expected, List):
        for i, result in enumerate(results):
            expected_inside: TypeJson = expected[i]

            if isinstance(result, Dict) and isinstance(expected_inside, Dict):
                for key, value in result.items():
                    match_result[key] = value == expected_inside[key]

    return match_result


def test_pair() -> None:
    VALUES: Strs = ['a', 'b', 'c']

    INPUT: TypeJson = [
        {key: Path(value) for key, value in zip(_KEYS, VALUES)},
        {key: Decimal(str(value)) for key, value in zip(_KEYS, _NUMBERS)},
    ]

    EXPECTED: TypeJson = [
        {key: value for key, value in zip(_KEYS, VALUES)},
        {key: value for key, value in zip(_KEYS, _NUMBERS)},
    ]

    results: TypeJson = serialize_json(INPUT)
    match_result: BoolPair = _check_result_same(EXPECTED, results)

    assert bool_same_pair(match_result)


def main() -> bool:
    test_adapt()
    test_array()
    test_pair()
    return True
