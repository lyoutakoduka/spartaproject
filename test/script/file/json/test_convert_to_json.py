#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.default.bool_context import (
    BoolPair,
    BoolPair2,
    Bools,
    Bools2,
)
from pyspartaproj.context.default.float_context import (
    FloatPair,
    FloatPair2,
    Floats,
    Floats2,
)
from pyspartaproj.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
    Ints2,
)
from pyspartaproj.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartaproj.context.extension.decimal_context import (
    DecPair,
    DecPair2,
    Decs,
    Decs2,
)
from pyspartaproj.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths,
    Paths2,
)
from pyspartaproj.context.file.json_context import Json, Multi, Multi2
from pyspartaproj.script.file.json.convert_to_json import (
    multiple2_to_json,
    multiple_to_json,
    to_safe_json,
)
from pyspartaproj.script.file.json.export_json import json_dump


def _common_test(expected: str, input: Json) -> None:
    assert expected == json_dump(input, compress=True)


def _common_test_array(expected: str, input: Multi) -> None:
    expected_array: str = f"[{expected}]"
    _common_test(expected_array, multiple_to_json(input))


def _common_test_array2(expected: str, input: Multi2) -> None:
    expected_array: str = f"[[{expected}]]"
    _common_test(expected_array, multiple2_to_json(input))


def _common_test_pair(expected: str, input: Multi) -> None:
    expected_pair: str = '{"B":%s}' % expected
    _common_test(expected_pair, multiple_to_json(input))


def _common_test_pair2(expected: str, input: Multi2) -> None:
    expected_pair: str = """{"A":{"B":%s}}""" % expected
    _common_test(expected_pair, multiple2_to_json(input))


def test_bool_array() -> None:
    input: bool = True
    input1: Bools = [input]
    input2: Bools2 = [input1]
    expected: str = "true"
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_bool_pair() -> None:
    input: bool = True
    input1: BoolPair = {"B": input}
    input2: BoolPair2 = {"A": input1}
    expected: str = "true"
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_integer_array() -> None:
    input: int = 1
    input1: Ints = [input]
    input2: Ints2 = [input1]
    expected: str = "1"
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_integer_pair() -> None:
    input: int = 1
    input1: IntPair = {"B": input}
    input2: IntPair2 = {"A": input1}
    expected: str = "1"
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_float_array() -> None:
    input: float = 1.0
    input1: Floats = [input]
    input2: Floats2 = [input1]
    expected: str = "1.0"
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_float_pair() -> None:
    input: float = 1.0
    input1: FloatPair = {"B": input}
    input2: FloatPair2 = {"A": input1}
    expected: str = "1.0"
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_string_array() -> None:
    input: str = "R"
    input1: Strs = [input]
    input2: Strs2 = [input1]
    expected: str = '"R"'
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_string_pair() -> None:
    input: str = "R"
    input1: StrPair = {"B": input}
    input2: StrPair2 = {"A": input1}
    expected: str = '"R"'
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_decimal_array() -> None:
    input: Decimal = Decimal("1.0")
    input1: Decs = [input]
    input2: Decs2 = [input1]
    expected: str = "1.0"
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_decimal_pair() -> None:
    input: Decimal = Decimal("1.0")
    input1: DecPair = {"B": input}
    input2: DecPair2 = {"A": input1}
    expected: str = "1.0"
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_path_array() -> None:
    input: Path = Path("root")
    input1: Paths = [input]
    input2: Paths2 = [input1]
    expected: str = '"root"'
    _common_test_array(expected, input1)
    _common_test_array2(expected, input2)


def test_path_pair() -> None:
    input: Path = Path("root")
    input1: PathPair = {"B": input}
    input2: PathPair2 = {"A": input1}
    expected: str = '"root"'
    _common_test_pair(expected, input1)
    _common_test_pair2(expected, input2)


def test_tree() -> None:
    input: Json = {"A": {"B": {"C": [None, Decimal("-1.0"), Path("root")]}}}
    expected: str = """{"A":{"B":{"C":[null,-1.0,"root"]}}}"""
    assert expected == json_dump(to_safe_json(input), compress=True)


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
