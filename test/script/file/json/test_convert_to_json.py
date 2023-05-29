#!/usr/bin/env python
# -*- coding: utf-8 -*-

from context.default.bool_context import Bools, Bools2, BoolPair, BoolPair2
from context.default.float_context import (
    Floats, Floats2, FloatPair, FloatPair2
)
from context.default.integer_context import Ints, Ints2, IntPair, IntPair2
from context.default.string_context import Strs, Strs2, StrPair, StrPair2
from context.extension.decimal_context import (
    Decimal, Decs, Decs2, DecPair, DecPair2
)
from context.extension.path_context import (
    Path, Paths, Paths2, PathPair, PathPair2
)
from context.file.json_context import Json, Multi, Multi2
from script.file.json.convert_to_json import (
    to_safe_json, multiple_to_json, multiple2_to_json
)
from script.file.json.export_json import json_dump


def _common_test(expected: str, input: Json) -> None:
    assert expected == json_dump(input, compress=True)


def _common_test_array(expected: str, input: Multi) -> None:
    expected_array: str = f'[{expected}]'
    _common_test(expected_array, multiple_to_json(input))


def _common_test_array2(expected: str, input: Multi2) -> None:
    expected_array: str = f'[[{expected}]]'
    _common_test(expected_array, multiple2_to_json(input))


def _common_test_pair(expected: str, input: Multi) -> None:
    expected_pair: str = '{"B":%s}' % expected
    _common_test(expected_pair, multiple_to_json(input))


def _common_test_pair2(expected: str, input: Multi2) -> None:
    expected_pair: str = '''{"A":{"B":%s}}''' % expected
    _common_test(expected_pair, multiple2_to_json(input))


def test_bool_array() -> None:
    INPUT: bool = True
    input1: Bools = [INPUT]
    input2: Bools2 = [input1]
    EXPECTED: str = 'true'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_bool_pair() -> None:
    INPUT: bool = True
    input1: BoolPair = {'B': INPUT}
    input2: BoolPair2 = {'A': input1}
    EXPECTED: str = 'true'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


def test_integer_array() -> None:
    INPUT: int = 1
    input1: Ints = [INPUT]
    input2: Ints2 = [input1]
    EXPECTED: str = '1'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_integer_pair() -> None:
    INPUT: int = 1
    input1: IntPair = {'B': INPUT}
    input2: IntPair2 = {'A': input1}
    EXPECTED: str = '1'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


def test_float_array() -> None:
    INPUT: float = 1.0
    input1: Floats = [INPUT]
    input2: Floats2 = [input1]
    EXPECTED: str = '1.0'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_float_pair() -> None:
    INPUT: float = 1.0
    input1: FloatPair = {'B': INPUT}
    input2: FloatPair2 = {'A': input1}
    EXPECTED: str = '1.0'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


def test_string_array() -> None:
    INPUT: str = 'R'
    input1: Strs = [INPUT]
    input2: Strs2 = [input1]
    EXPECTED: str = '"R"'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_string_pair() -> None:
    INPUT: str = 'R'
    input1: StrPair = {'B': INPUT}
    input2: StrPair2 = {'A': input1}
    EXPECTED: str = '"R"'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


def test_decimal_array() -> None:
    INPUT: Decimal = Decimal('1.0')
    input1: Decs = [INPUT]
    input2: Decs2 = [input1]
    EXPECTED: str = '1.0'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_decimal_pair() -> None:
    INPUT: Decimal = Decimal('1.0')
    input1: DecPair = {'B': INPUT}
    input2: DecPair2 = {'A': input1}
    EXPECTED: str = '1.0'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


def test_path_array() -> None:
    INPUT: Path = Path('root')
    input1: Paths = [INPUT]
    input2: Paths2 = [input1]
    EXPECTED: str = '"root"'
    _common_test_array(EXPECTED, input1)
    _common_test_array2(EXPECTED, input2)


def test_path_pair() -> None:
    INPUT: Path = Path('root')
    input1: PathPair = {'B': INPUT}
    input2: PathPair2 = {'A': input1}
    EXPECTED: str = '"root"'
    _common_test_pair(EXPECTED, input1)
    _common_test_pair2(EXPECTED, input2)


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
