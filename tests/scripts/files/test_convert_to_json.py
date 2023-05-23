#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools2, BoolPair2
from contexts.decimal_context import Decimal, Decs2, DecPair2
from contexts.float_context import Floats2, FloatPair2
from contexts.integer_context import Ints2, IntPair2
from contexts.json_context import Json, Multi2
from contexts.path_context import Path, Paths2, PathPair2
from contexts.string_context import Strs, Strs2, StrPair2
from scripts.files.convert_to_json import to_safe_json, multi2_to_json
from scripts.files.export_json import json_dump


def _common_test(expected: str, input: Multi2) -> None:
    assert expected == json_dump(multi2_to_json(input), compress=True)


def _common_test_array(expected: Strs, input: Multi2) -> None:
    expected_array: str = '[[' + ','.join(expected) + ']]'
    _common_test(expected_array, input)


def _common_test_pair(expected: str, input: Multi2) -> None:
    expected_pair: str = '''{"A":{"B":%s}}''' % expected
    _common_test(expected_pair, input)


def test_bool_array() -> None:
    INPUT: Bools2 = [[True, False]]
    EXPECTED: Strs = ['true', 'false']
    _common_test_array(EXPECTED, INPUT)


def test_bool_pair() -> None:
    INPUT: BoolPair2 = {'A': {'B': True}}
    EXPECTED: str = 'true'
    _common_test_pair(EXPECTED, INPUT)


def test_integer_array() -> None:
    INPUT: Ints2 = [[-1, 1]]
    EXPECTED: Strs = ['-1', '1']
    _common_test_array(EXPECTED, INPUT)


def test_integer_pair() -> None:
    INPUT: IntPair2 = {'A': {'B': 1}}
    EXPECTED: str = '1'
    _common_test_pair(EXPECTED, INPUT)


def test_float_array() -> None:
    INPUT: Floats2 = [[-1.0, 1.0]]
    EXPECTED: Strs = ['-1.0', '1.0']
    _common_test_array(EXPECTED, INPUT)


def test_float_pair() -> None:
    INPUT: FloatPair2 = {'A': {'B': 1.0}}
    EXPECTED: str = '1.0'
    _common_test_pair(EXPECTED, INPUT)


def test_string_array() -> None:
    INPUT: Strs2 = [['R', 'G']]
    EXPECTED: Strs = ['"R"', '"G"']
    _common_test_array(EXPECTED, INPUT)


def test_string_pair() -> None:
    INPUT: StrPair2 = {'A': {'B': 'R'}}
    EXPECTED: str = '"R"'
    _common_test_pair(EXPECTED, INPUT)


def test_decimal_array() -> None:
    INPUT: Decs2 = [[Decimal('-1.0'), Decimal('1.0')]]
    EXPECTED: Strs = ['-1.0', '1.0']
    _common_test_array(EXPECTED, INPUT)


def test_decimal_pair() -> None:
    INPUT: DecPair2 = {'A': {'B': Decimal('1.0')}}
    EXPECTED: str = '1.0'
    _common_test_pair(EXPECTED, INPUT)


def test_path_array() -> None:
    INPUT: Paths2 = [[Path('test'), Path('root')]]
    EXPECTED: Strs = ['"test"', '"root"']
    _common_test_array(EXPECTED, INPUT)


def test_path_pair() -> None:
    INPUT: PathPair2 = {'A': {'B': Path('root')}}
    EXPECTED: str = '"root"'
    _common_test_pair(EXPECTED, INPUT)


def test_tree() -> None:
    INPUT: Json = {'A': {'B': {'C': [None, Decimal('-1.0'), Path('root')]}}}
    EXPECTED: str = '''{"A":{"B":{"C":[null,-1.0,"root"]}}}'''
    assert EXPECTED == json_dump(to_safe_json(INPUT), compress=True)


def main() -> bool:
    test_bool_array()
    test_bool_pair()
    test_integer_array()
    test_integer_pair()
    test_float_array()
    test_float_pair()
    test_string_array()
    test_string_pair()
    test_decimal_array()
    test_decimal_pair()
    test_path_array()
    test_path_pair()
    test_tree()
    return True
