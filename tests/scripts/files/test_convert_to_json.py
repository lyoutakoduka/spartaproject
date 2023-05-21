#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.bool_context import Bools2, BoolPair2
from contexts.decimal_context import Decimal, Decs2, DecPair2
from contexts.float_context import Floats2, FloatPair2
from contexts.integer_context import Ints2, IntPair2
from contexts.json_context import Json, Array2, Pair2
from contexts.path_context import Path, Paths2, PathPair2
from contexts.string_context import Strs, Strs2, StrPair2
from scripts.files.convert_to_json import (
    to_safe_json, array2_to_json, pair2_to_json
)
from scripts.files.export_json import json_dump


def _common_test(expected: str, result: Json) -> None:
    assert expected == json_dump(result, compress=True)


def _common_test_array(expected: Strs, input: Array2) -> None:
    expected_array: str = '[[' + ','.join(expected) + ']]'
    _common_test(expected_array, array2_to_json(input))


def _common_test_pair(expected: str, input: Pair2) -> None:
    expected_pair: str = '''{"A":{"B":%s}}''' % expected
    _common_test(expected_pair, pair2_to_json(input))


def test_bool_array() -> None:
    INPUT: Bools2 = [[True, False]]
    EXPECTED: Strs = ['true', 'false']
    _common_test_array(EXPECTED, INPUT)


def test_bool_pair() -> None:
    INPUT: BoolPair2 = {'A': {'B': True}}
    EXPECTED: str = 'true'
    _common_test_pair(EXPECTED, INPUT)


def test_int_array() -> None:
    INPUT: Ints2 = [[-1, 1]]
    EXPECTED: Strs = ['-1', '1']
    _common_test_array(EXPECTED, INPUT)


def test_int_pair() -> None:
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


def test_str_array() -> None:
    INPUT: Strs2 = [['R', 'G']]
    EXPECTED: Strs = ['"R"', '"G"']
    _common_test_array(EXPECTED, INPUT)


def test_str_pair() -> None:
    INPUT: StrPair2 = {'A': {'B': 'R'}}
    EXPECTED: str = '"R"'
    _common_test_pair(EXPECTED, INPUT)


def test_dec_array() -> None:
    INPUT: Decs2 = [[Decimal('-1.0'), Decimal('1.0')]]
    EXPECTED: Strs = ['-1.0', '1.0']
    _common_test_array(EXPECTED, INPUT)


def test_dec_pair() -> None:
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
    _common_test(EXPECTED, to_safe_json(INPUT))


def main() -> bool:
    test_bool_array()
    test_bool_pair()
    test_int_array()
    test_int_pair()
    test_float_array()
    test_float_pair()
    test_str_array()
    test_str_pair()
    test_dec_array()
    test_dec_pair()
    test_path_array()
    test_path_pair()
    test_tree()
    return True
