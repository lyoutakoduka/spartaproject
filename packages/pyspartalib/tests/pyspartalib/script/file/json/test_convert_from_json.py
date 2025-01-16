#!/usr/bin/env python

"""Test module to convert data from json format."""

from collections.abc import Sized
from decimal import Decimal
from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair, PathPair2
from pyspartalib.context.file.json_context import (
    Array,
    Array2,
    Json,
    Pair,
    Pair2,
    Single,
    SinglePair,
)
from pyspartalib.context.type_context import Type
from pyspartalib.script.bool.compare_json import is_same_json
from pyspartalib.script.file.json.convert_from_json import (
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


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _length_error(result: Sized, expected: int) -> None:
    if len(result) == expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_bool() -> bool:
    return True


def _get_bool_array() -> Json:
    return [_get_bool()]


def _get_bool_arrays() -> Json:
    return [_get_bool_array()]


def _get_bool_pair() -> Json:
    return {"B": _get_bool()}


def _get_bool_pairs() -> Json:
    return {"A": _get_bool_pair()}


def _get_integer() -> int:
    return 1


def _get_integer_array() -> Json:
    return [_get_integer()]


def _get_integer_arrays() -> Json:
    return [_get_integer_array()]


def _get_integer_pair() -> Json:
    return {"B": _get_integer()}


def _get_integer_pairs() -> Json:
    return {"A": _get_integer_pair()}


def _get_decimal() -> Decimal:
    return Decimal("1.0")


def _get_float() -> float:
    return float(_get_decimal())


def _get_float_array() -> Json:
    return [_get_float()]


def _get_float_arrays() -> Json:
    return [_get_float_array()]


def _get_float_pair() -> Json:
    return {"B": _get_float()}


def _get_float_pairs() -> Json:
    return {"A": _get_float_pair()}


def _get_string() -> str:
    return "root"


def _get_path() -> Path:
    return Path(_get_string())


def _get_string_array() -> Json:
    return [_get_string()]


def _get_string_arrays() -> Json:
    return [_get_string_array()]


def _get_string_pair() -> Json:
    return {"B": _get_string(), "C.path": _get_path()}


def _get_string_pairs() -> Json:
    return {"A": _get_string_pair()}


def _get_path_pair() -> Json:
    return {"B.path": _get_string(), "C": _get_string()}


def _get_path_pairs() -> Json:
    return {"A": _get_path_pair()}


def _common_test(expected: Single, result: Single, size: Sized) -> None:
    _length_error(size, 1)
    _difference_error(result, expected)


def _common_test_array(expected: Single, result: Array) -> None:
    _common_test(expected, result[0], result)


def _common_test_array2(expected: Single, result: Array2) -> None:
    _common_test_array(expected, result[0])


def _common_test_pair(expected: Single, result: Pair) -> None:
    _common_test(expected, result["B"], result)


def _common_test_pair2(expected: Single, result: Pair2) -> None:
    _common_test_pair(expected, result["A"])


def _compare_path_pair(expected: Path, result: PathPair) -> None:
    _common_test(expected, result["B.path"], result)


def _compare_path_pair2(expected: Path, result: PathPair2) -> None:
    _compare_path_pair(expected, result["A"])


def _get_mixed() -> SinglePair:
    return {
        "null": None,
        "boolean": _get_bool(),
        "integer": _get_integer(),
        "decimal": _get_float(),
        "string": _get_string(),
        "path.path": _get_string(),
    }


def _get_config_source() -> Json:
    return {"section": dict(_get_mixed())}


def _get_expected_safe() -> Json:
    return {
        "null": None,
        "boolean": _get_bool(),
        "integer": _get_integer(),
        "decimal": _get_decimal(),
        "string": _get_string(),
        "path.path": _get_path(),
    }


def test_bool_array() -> None:
    """Test to convert json format data to list of type "bool"."""
    source: bool = _get_bool()

    _common_test_array(source, bool_array_from_json(_get_bool_array()))
    _common_test_array2(source, bool_array2_from_json(_get_bool_arrays()))


def test_bool_pair() -> None:
    """Test to convert json format data to dictionary of type "bool"."""
    source: bool = _get_bool()

    _common_test_pair(source, bool_pair_from_json(_get_bool_pair()))
    _common_test_pair2(source, bool_pair2_from_json(_get_bool_pairs()))


def test_integer_array() -> None:
    """Test to convert json format data to list of type "int"."""
    source: int = _get_integer()

    _common_test_array(source, integer_array_from_json(_get_integer_array()))
    _common_test_array2(
        source,
        integer_array2_from_json(_get_integer_arrays()),
    )


def test_integer_pair() -> None:
    """Test to convert json format data to dictionary of type "int"."""
    source: int = _get_integer()

    _common_test_pair(source, integer_pair_from_json(_get_integer_pair()))
    _common_test_pair2(source, integer_pair2_from_json(_get_integer_pairs()))


def test_decimal_array() -> None:
    """Test to convert json format data to list of type "Decimal"."""
    source: Decimal = _get_decimal()

    _common_test_array(source, decimal_array_from_json(_get_float_array()))
    _common_test_array2(source, decimal_array2_from_json(_get_float_arrays()))


def test_decimal_pair() -> None:
    """Test to convert json format data to dictionary of type "Decimal"."""
    source: Decimal = _get_decimal()

    _common_test_pair(source, decimal_pair_from_json(_get_float_pair()))
    _common_test_pair2(source, decimal_pair2_from_json(_get_float_pairs()))


def test_string_array() -> None:
    """Test to convert json format data to list of type "str"."""
    source: str = _get_string()

    _common_test_array(source, string_array_from_json(_get_string_array()))
    _common_test_array2(source, string_array2_from_json(_get_string_arrays()))


def test_string_pair() -> None:
    """Test to convert json format data to dictionary of type "str"."""
    source: str = _get_string()

    _common_test_pair(source, string_pair_from_json(_get_string_pair()))
    _common_test_pair2(source, string_pair2_from_json(_get_string_pairs()))


def test_path_array() -> None:
    """Test to convert json format data to list of type "Path"."""
    source: Path = _get_path()

    _common_test_array(source, path_array_from_json(_get_string_array()))
    _common_test_array2(source, path_array2_from_json(_get_string_arrays()))


def test_path_pair() -> None:
    """Test to convert json format data to dictionary of type "Path"."""
    source: Path = _get_path()

    _compare_path_pair(source, path_pair_from_json(_get_path_pair()))
    _compare_path_pair2(source, path_pair2_from_json(_get_path_pairs()))


def test_safe() -> None:
    """Test to convert default json format data to custom json format."""
    _fail_error(
        is_same_json(
            from_safe_json(_get_config_source()),
            _get_expected_safe(),
        ),
    )
