#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import Dict, List

from pyspartaproj.context.default.string_context import StrPair, StrPair2
from pyspartaproj.context.extension.path_context import PathPair, PathPair2
from pyspartaproj.context.file.json_context import (
    Array,
    Array2,
    Json,
    Pair,
    Pair2,
    Single,
)
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.file.json.convert_from_json import (
    bool_array2_from_json,
    bool_array_from_json,
    bool_pair2_from_json,
    bool_pair_from_json,
    decimal_array2_from_json,
    decimal_array_from_json,
    decimal_pair2_from_json,
    decimal_pair_from_json,
    from_safe_json,
    integer_array2_from_json,
    integer_array_from_json,
    integer_pair2_from_json,
    integer_pair_from_json,
    path_array2_from_json,
    path_array_from_json,
    path_pair2_from_json,
    path_pair_from_json,
    string_array2_from_json,
    string_array_from_json,
    string_pair2_from_json,
    string_pair_from_json,
)


def _common_test(input: Single, result: Single, size: int) -> None:
    assert 1 == size
    assert input == result


def _common_test_array(input: Single, result: Array) -> None:
    _common_test(input, result[0], len(result))


def _common_test_array2(input: Single, result: Array2) -> None:
    _common_test_array(input, result[0])


def _common_test_pair(input: Single, result: Pair) -> None:
    _common_test(input, result["B"], len(result))


def _common_test_pair2(input: Single, result: Pair2) -> None:
    _common_test_pair(input, result["A"])


def test_bool_array() -> None:
    input: bool = True
    input1: Json = [input]
    input2: Json = [input1]
    _common_test_array(input, bool_array_from_json(input1))
    _common_test_array2(input, bool_array2_from_json(input2))


def test_bool_pair() -> None:
    input: bool = True
    input1: Json = {"B": input}
    input2: Json = {"A": input1}
    _common_test_pair(input, bool_pair_from_json(input1))
    _common_test_pair2(input, bool_pair2_from_json(input2))


def test_integer_array() -> None:
    input: int = 1
    input1: Json = [input]
    input2: Json = [input1]
    _common_test_array(input, integer_array_from_json(input1))
    _common_test_array2(input, integer_array2_from_json(input2))


def test_integer_pair() -> None:
    input: int = 1
    input1: Json = {"B": input}
    input2: Json = {"A": input1}
    _common_test_pair(input, integer_pair_from_json(input1))
    _common_test_pair2(input, integer_pair2_from_json(input2))


def test_string_array() -> None:
    input: str = "test"
    input1: Json = [input]
    input2: Json = [input1]
    _common_test_array(input, string_array_from_json(input1))
    _common_test_array2(input, string_array2_from_json(input2))


def test_string_pair() -> None:
    input: str = "test"
    input1: Json = {"B": input, "C.path": Path("remove")}
    input2: Json = {"A": input1}
    _common_test_pair(input, string_pair_from_json(input1))
    _common_test_pair2(input, string_pair2_from_json(input2))

    result: StrPair = string_pair_from_json(input1)
    _common_test(input, result["B"], len(result))

    result_parent: StrPair2 = string_pair2_from_json(input2)
    result_child: StrPair = result_parent["A"]
    _common_test(input, result_child["B"], len(result_child))


def test_decimal_array() -> None:
    input: Decimal = Decimal("1.0")
    input1: Json = [float(input)]
    input2: Json = [input1]
    _common_test_array(input, decimal_array_from_json(input1))
    _common_test_array2(input, decimal_array2_from_json(input2))


def test_decimal_pair() -> None:
    input: Decimal = Decimal("1.0")
    input1: Json = {"B": float(input)}
    input2: Json = {"A": input1}
    _common_test_pair(input, decimal_pair_from_json(input1))
    _common_test_pair2(input, decimal_pair2_from_json(input2))


def test_path_array() -> None:
    input: Path = Path("root")
    input1: Json = [str(input)]
    input2: Json = [input1]
    _common_test_array(input, path_array_from_json(input1))
    _common_test_array2(input, path_array2_from_json(input2))


def test_path_pair() -> None:
    input: Path = Path("root")
    input1: Json = {"B.path": str(input), "C": "remove"}
    input2: Json = {"A": input1}

    result: PathPair = path_pair_from_json(input1)
    _common_test(input, result["B.path"], len(result))

    result_parent: PathPair2 = path_pair2_from_json(input2)
    result_child: PathPair = result_parent["A"]
    _common_test(input, result_child["B.path"], len(result_child))


def test_tree() -> None:
    input_left: int = 1
    input_right: str = "test"
    input: Json = {"A": {"B": [None, input_left], "C": input_right}}
    result: Json = from_safe_json(input)

    assert isinstance(result, Dict)
    result_outside: Json = result["A"]
    assert isinstance(result_outside, Dict)
    result_inside: Json = result_outside["B"]
    assert isinstance(result_inside, List)

    assert bool_same_array(
        [
            input_right == result_outside["C"],
            [None, input_left] == result_inside,
        ]
    )


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
