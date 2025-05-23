#!/usr/bin/env python

"""Test module to convert data to json format."""

from decimal import Decimal
from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.bool_context import (
    BoolPair,
    BoolPair2,
    Bools,
    Bools2,
)
from pyspartalib.context.default.float_context import (
    FloatPair,
    FloatPair2,
    Floats,
    Floats2,
)
from pyspartalib.context.default.integer_context import (
    IntPair,
    IntPair2,
    Ints,
    Ints2,
)
from pyspartalib.context.default.string_context import (
    StrPair,
    StrPair2,
    Strs,
    Strs2,
)
from pyspartalib.context.extension.decimal_context import (
    DecPair,
    DecPair2,
    Decs,
    Decs2,
)
from pyspartalib.context.extension.path_context import (
    PathPair,
    PathPair2,
    Paths,
    Paths2,
)
from pyspartalib.context.file.json_context import (
    Json,
    Multi,
    Multi2,
    Singles,
)
from pyspartalib.script.file.json.convert_to_json import (
    multiple2_to_json,
    multiple_to_json,
    to_safe_json,
)
from pyspartalib.script.file.json.export_json import json_dump


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _common_test(expected: str, source: Json) -> None:
    _difference_error(json_dump(source, compress=True), expected)


def _common_test_array(expected: str, source_array: Multi) -> None:
    _common_test(f"[{expected}]", multiple_to_json(source_array))


def _common_test_array2(expected: str, source_arrays: Multi2) -> None:
    _common_test(f"[[{expected}]]", multiple2_to_json(source_arrays))


def _common_test_pair(expected: str, source_pair: Multi) -> None:
    _common_test(f'{{"B":{expected}}}', multiple_to_json(source_pair))


def _common_test_pair2(expected: str, source_pairs: Multi2) -> None:
    _common_test(
        f'{{"A":{{"B":{expected}}}}}',
        multiple2_to_json(source_pairs),
    )


def _get_bool() -> bool:
    return True


def _get_bool_array() -> Bools:
    return [_get_bool()]


def _get_bool_arrays() -> Bools2:
    return [_get_bool_array()]


def _get_bool_pair() -> BoolPair:
    return {"B": _get_bool()}


def _get_bool_pairs() -> BoolPair2:
    return {"A": _get_bool_pair()}


def _get_integer() -> int:
    return 1


def _get_integer_array() -> Ints:
    return [_get_integer()]


def _get_integer_arrays() -> Ints2:
    return [_get_integer_array()]


def _get_integer_pair() -> IntPair:
    return {"B": _get_integer()}


def _get_integer_pairs() -> IntPair2:
    return {"A": _get_integer_pair()}


def _get_float() -> float:
    return 1.0


def _get_float_array() -> Floats:
    return [_get_float()]


def _get_float_arrays() -> Floats2:
    return [_get_float_array()]


def _get_float_pair() -> FloatPair:
    return {"B": _get_float()}


def _get_float_pairs() -> FloatPair2:
    return {"A": _get_float_pair()}


def _get_decimal() -> Decimal:
    return Decimal("1.0")


def _get_decimal_array() -> Decs:
    return [_get_decimal()]


def _get_decimal_arrays() -> Decs2:
    return [_get_decimal_array()]


def _get_decimal_pair() -> DecPair:
    return {"B": _get_decimal()}


def _get_decimal_pairs() -> DecPair2:
    return {"A": _get_decimal_pair()}


def _get_string() -> str:
    return "root"


def _get_string_array() -> Strs:
    return [_get_string()]


def _get_string_arrays() -> Strs2:
    return [_get_string_array()]


def _get_string_pair() -> StrPair:
    return {"B": _get_string()}


def _get_string_pairs() -> StrPair2:
    return {"A": _get_string_pair()}


def _get_path() -> Path:
    return Path(_get_string())


def _get_path_array() -> Paths:
    return [_get_path()]


def _get_path_arrays() -> Paths2:
    return [_get_path_array()]


def _get_path_pair() -> PathPair:
    return {"B": _get_path()}


def _get_path_pairs() -> PathPair2:
    return {"A": _get_path_pair()}


def _get_mixed() -> Singles:
    return [
        None,
        _get_bool(),
        _get_integer(),
        _get_float(),
        _get_decimal(),
        _get_string(),
        _get_path(),
    ]


def _get_config_source() -> Json:
    return {"A": {"B": {"C": list(_get_mixed())}}}


def _get_expected_bool() -> str:
    return "true"


def _get_expected_integer() -> str:
    return "1"


def _get_expected_float() -> str:
    return "1.0"


def _get_expected_string() -> str:
    return '"root"'


def _duplicate_text(text: str) -> Strs:
    return [text] * 2


def _get_expected_source() -> Strs:
    return [
        "null",
        _get_expected_bool(),
        _get_expected_integer(),
        *_duplicate_text(_get_expected_float()),
        *_duplicate_text(_get_expected_string()),
    ]


def _stringify_mixed() -> str:
    return "[" + ", ".join(_get_expected_source()) + "]"


def _get_config_expected() -> str:
    compressed: str = _stringify_mixed().replace(" ", "")
    return f'{{"A":{{"B":{{"C":{compressed}}}}}}}'


def test_bool_array() -> None:
    """Test to convert data which is list of type "bool"."""
    expected: str = _get_expected_bool()

    _common_test_array(expected, _get_bool_array())
    _common_test_array2(expected, _get_bool_arrays())


def test_bool_pair() -> None:
    """Test to convert data which is dictionary of type "bool"."""
    expected: str = _get_expected_bool()

    _common_test_pair(expected, _get_bool_pair())
    _common_test_pair2(expected, _get_bool_pairs())


def test_integer_array() -> None:
    """Test to convert data which is list of type "int"."""
    expected: str = _get_expected_integer()

    _common_test_array(expected, _get_integer_array())
    _common_test_array2(expected, _get_integer_arrays())


def test_integer_pair() -> None:
    """Test to convert data which is dictionary of type "int"."""
    expected: str = _get_expected_integer()

    _common_test_pair(expected, _get_integer_pair())
    _common_test_pair2(expected, _get_integer_pairs())


def test_float_array() -> None:
    """Test to convert data which is list of type "float"."""
    expected: str = _get_expected_float()

    _common_test_array(expected, _get_float_array())
    _common_test_array2(expected, _get_float_arrays())


def test_float_pair() -> None:
    """Test to convert data which is dictionary of type "float"."""
    expected: str = _get_expected_float()

    _common_test_pair(expected, _get_float_pair())
    _common_test_pair2(expected, _get_float_pairs())


def test_decimal_array() -> None:
    """Test to convert data which is list of type "Decimal"."""
    expected: str = _get_expected_float()

    _common_test_array(expected, _get_decimal_array())
    _common_test_array2(expected, _get_decimal_arrays())


def test_decimal_pair() -> None:
    """Test to convert data which is dictionary of type "Decimal"."""
    expected: str = _get_expected_float()

    _common_test_pair(expected, _get_decimal_pair())
    _common_test_pair2(expected, _get_decimal_pairs())


def test_string_array() -> None:
    """Test to convert data which is list of type "str"."""
    expected: str = _get_expected_string()

    _common_test_array(expected, _get_string_array())
    _common_test_array2(expected, _get_string_arrays())


def test_string_pair() -> None:
    """Test to convert data which is dictionary of type "str"."""
    expected: str = _get_expected_string()

    _common_test_pair(expected, _get_string_pair())
    _common_test_pair2(expected, _get_string_pairs())


def test_path_array() -> None:
    """Test to convert data which is list of type "Path"."""
    expected: str = _get_expected_string()

    _common_test_array(expected, _get_path_array())
    _common_test_array2(expected, _get_path_arrays())


def test_path_pair() -> None:
    """Test to convert data which is dictionary of type "Path"."""
    expected: str = _get_expected_string()

    _common_test_pair(expected, _get_path_pair())
    _common_test_pair2(expected, _get_path_pairs())


def test_safe() -> None:
    """Test to convert custom json format data to default json format."""
    _difference_error(
        json_dump(to_safe_json(_get_config_source()), compress=True),
        _get_config_expected(),
    )
