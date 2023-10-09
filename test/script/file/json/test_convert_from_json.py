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


def _common_test(expected: Single, result: Single, size: int) -> None:
    assert 1 == size
    assert expected == result


def _common_test_array(expected: Single, result: Array) -> None:
    _common_test(expected, result[0], len(result))


def _common_test_array2(expected: Single, result: Array2) -> None:
    _common_test_array(expected, result[0])


def _common_test_pair(expected: Single, result: Pair) -> None:
    _common_test(expected, result["B"], len(result))


def _common_test_pair2(expected: Single, result: Pair2) -> None:
    _common_test_pair(expected, result["A"])


def test_bool_array() -> None:
    source: bool = True
    source_array: Json = [source]
    source_arrays: Json = [source_array]
    _common_test_array(source, bool_array_from_json(source_array))
    _common_test_array2(source, bool_array2_from_json(source_arrays))


def test_bool_pair() -> None:
    source: bool = True
    source_pair: Json = {"B": source}
    source_pairs: Json = {"A": source_pair}
    _common_test_pair(source, bool_pair_from_json(source_pair))
    _common_test_pair2(source, bool_pair2_from_json(source_pairs))


def test_integer_array() -> None:
    source: int = 1
    source_array: Json = [source]
    source_arrays: Json = [source_array]
    _common_test_array(source, integer_array_from_json(source_array))
    _common_test_array2(source, integer_array2_from_json(source_arrays))


def test_integer_pair() -> None:
    source: int = 1
    source_pair: Json = {"B": source}
    source_pairs: Json = {"A": source_pair}
    _common_test_pair(source, integer_pair_from_json(source_pair))
    _common_test_pair2(source, integer_pair2_from_json(source_pairs))


def test_string_array() -> None:
    source: str = "test"
    source_array: Json = [source]
    source_arrays: Json = [source_array]
    _common_test_array(source, string_array_from_json(source_array))
    _common_test_array2(source, string_array2_from_json(source_arrays))


def test_string_pair() -> None:
    source: str = "test"
    source_pair: Json = {"B": source, "C.path": Path("remove")}
    source_pairs: Json = {"A": source_pair}
    _common_test_pair(source, string_pair_from_json(source_pair))
    _common_test_pair2(source, string_pair2_from_json(source_pairs))

    result: StrPair = string_pair_from_json(source_pair)
    _common_test(source, result["B"], len(result))

    result_parent: StrPair2 = string_pair2_from_json(source_pairs)
    result_child: StrPair = result_parent["A"]
    _common_test(source, result_child["B"], len(result_child))


def test_decimal_array() -> None:
    source: Decimal = Decimal("1.0")
    source_array: Json = [float(source)]
    source_arrays: Json = [source_array]
    _common_test_array(source, decimal_array_from_json(source_array))
    _common_test_array2(source, decimal_array2_from_json(source_arrays))


def test_decimal_pair() -> None:
    source: Decimal = Decimal("1.0")
    source_pair: Json = {"B": float(source)}
    source_pairs: Json = {"A": source_pair}
    _common_test_pair(source, decimal_pair_from_json(source_pair))
    _common_test_pair2(source, decimal_pair2_from_json(source_pairs))


def test_path_array() -> None:
    source: Path = Path("root")
    source_array: Json = [str(source)]
    source_arrays: Json = [source_array]
    _common_test_array(source, path_array_from_json(source_array))
    _common_test_array2(source, path_array2_from_json(source_arrays))


def test_path_pair() -> None:
    source: Path = Path("root")
    source_pair: Json = {"B.path": str(source), "C": "remove"}
    source_pairs: Json = {"A": source_pair}

    result: PathPair = path_pair_from_json(source_pair)
    _common_test(source, result["B.path"], len(result))

    result_parent: PathPair2 = path_pair2_from_json(source_pairs)
    result_child: PathPair = result_parent["A"]
    _common_test(source, result_child["B.path"], len(result_child))


def test_tree() -> None:
    input_left: int = 1
    input_right: str = "test"
    source_pairs: Json = {"A": {"B": [None, input_left], "C": input_right}}
    result: Json = from_safe_json(source_pairs)

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
