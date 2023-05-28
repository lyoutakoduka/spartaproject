#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

from contexts.json_context import Json, Single, Array, Array2, Pair, Pair2
from scripts.bools.same_value import bool_same_array
from scripts.files.jsons.convert_from_json import (
    bool_array_from_json,
    integer_array_from_json,
    string_array_from_json,
    decimal_array_from_json,
    path_array_from_json,
    bool_pair_from_json,
    integer_pair_from_json,
    string_pair_from_json,
    decimal_pair_from_json,
    path_pair_from_json,
    bool_array2_from_json,
    integer_array2_from_json,
    string_array2_from_json,
    decimal_array2_from_json,
    path_array2_from_json,
    bool_pair2_from_json,
    integer_pair2_from_json,
    string_pair2_from_json,
    decimal_pair2_from_json,
    path_pair2_from_json,
    from_safe_json,
)


def _common_test(input: Single, result: Single) -> None:
    assert input == result


def _common_test_array(input: Single, result: Array) -> None:
    _common_test(input, result[0])


def _common_test_array2(input: Single, result: Array2) -> None:
    _common_test_array(input, result[0])


def _common_test_pair(input: Single, result: Pair) -> None:
    _common_test(input, result['B'])


def _common_test_pair2(input: Single, result: Pair2) -> None:
    _common_test_pair(input, result['A'])


def test_bool_array() -> None:
    INPUT: bool = True
    input1: Json = [INPUT]
    input2: Json = [input1]
    _common_test_array(INPUT, bool_array_from_json(input1))
    _common_test_array2(INPUT, bool_array2_from_json(input2))


def test_bool_pair() -> None:
    INPUT: bool = True
    input1: Json = {'B': INPUT}
    input2: Json = {'A': input1}
    _common_test_pair(INPUT, bool_pair_from_json(input1))
    _common_test_pair2(INPUT, bool_pair2_from_json(input2))


def test_integer_array() -> None:
    INPUT: int = 1
    input1: Json = [INPUT]
    input2: Json = [input1]
    _common_test_array(INPUT, integer_array_from_json(input1))
    _common_test_array2(INPUT, integer_array2_from_json(input2))


def test_integer_pair() -> None:
    INPUT: int = 1
    input1: Json = {'B': INPUT}
    input2: Json = {'A': input1}
    _common_test_pair(INPUT, integer_pair_from_json(input1))
    _common_test_pair2(INPUT, integer_pair2_from_json(input2))


def test_string_array() -> None:
    INPUT: str = 'test'
    input1: Json = [INPUT]
    input2: Json = [input1]
    _common_test_array(INPUT, string_array_from_json(input1))
    _common_test_array2(INPUT, string_array2_from_json(input2))


def test_string_pair() -> None:
    INPUT: str = 'test'
    input1: Json = {'B': INPUT}
    input2: Json = {'A': input1}
    _common_test_pair(INPUT, string_pair_from_json(input1))
    _common_test_pair2(INPUT, string_pair2_from_json(input2))


def test_decimal_array() -> None:
    INPUT: Decimal = Decimal('1.0')
    input1: Json = [float(INPUT)]
    input2: Json = [input1]
    _common_test_array(INPUT, decimal_array_from_json(input1))
    _common_test_array2(INPUT, decimal_array2_from_json(input2))


def test_decimal_pair() -> None:
    INPUT: Decimal = Decimal('1.0')
    input1: Json = {'B': float(INPUT)}
    input2: Json = {'A': input1}
    _common_test_pair(INPUT, decimal_pair_from_json(input1))
    _common_test_pair2(INPUT, decimal_pair2_from_json(input2))


def test_path_array() -> None:
    INPUT: Path = Path('root')
    input1: Json = [str(INPUT)]
    input2: Json = [input1]
    _common_test_array(INPUT, path_array_from_json(input1))
    _common_test_array2(INPUT, path_array2_from_json(input2))


def test_path_pair() -> None:
    INPUT: Path = Path('root')
    input1: Json = {'B': str(INPUT)}
    input2: Json = {'A': input1}
    _common_test_pair(INPUT, path_pair_from_json(input1))
    _common_test_pair2(INPUT, path_pair2_from_json(input2))


def test_tree() -> None:
    INPUT_DECIMAL: Decimal = Decimal('1.0')
    INPUT_PATH: Path = Path('root')
    input: Json = {'A': {
        'B': [None, float(INPUT_DECIMAL)], 'path': str(INPUT_PATH)
    }}
    result: Json = from_safe_json(input)

    assert isinstance(result, Dict)
    result_outside: Json = result['A']
    assert isinstance(result_outside, Dict)
    result_inside: Json = result_outside['B']
    assert isinstance(result_inside, List)

    assert bool_same_array([
        INPUT_PATH == result_outside['path'],
        [None, INPUT_DECIMAL] == result_inside,
    ])


def main() -> bool:
    test_bool_array()
    test_bool_pair()
    test_integer_array()
    test_integer_pair()
    test_string_array()
    test_string_pair()
    test_decimal_array()
    test_decimal_pair()
    test_path_array()
    test_path_pair()
    test_tree()
    return True
