#!/usr/bin/env python

"""Test module to export data used for configuration file."""

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.default.bool_context import BoolPair, BoolPair2
from pyspartalib.context.default.float_context import FloatPair, FloatPair2
from pyspartalib.context.default.integer_context import IntPair, IntPair2
from pyspartalib.context.default.string_context import StrPair, StrPair2, Strs
from pyspartalib.context.extension.decimal_context import DecPair, DecPair2
from pyspartalib.context.extension.path_context import (
    PathFunc,
    PathPair,
    PathPair2,
)
from pyspartalib.context.file.config_context import (
    Config,
    SectionPair,
    SinglePair,
    SinglePair2,
)
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.config.export_config import (
    config_dump,
    config_export,
)
from pyspartalib.script.file.text.import_file import text_import
from pyspartalib.script.string.format_texts import format_indent


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_config_bool() -> str:
    return """
        [bool]
        bool = True
    """


def _get_config_integer() -> str:
    return """
        [integer]
        integer = 1
    """


def _get_config_float() -> str:
    return """
        [float]
        float = 1.0
    """


def _get_config_decimal() -> str:
    return """
        [decimal]
        decimal = 0.1
    """


def _get_config_string() -> str:
    return """
        [string]
        string = test
    """


def _get_config_path() -> str:
    return """
        [path]
        path = root
    """


def _get_config_mix() -> str:
    return """
        [section]
        bool = True
        integer = 1
        float = 1.0
        decimal = 0.1
        string = test
        path = root
    """


def _get_config_mix_group() -> str:
    return """
        [bool]
        bool = True

        [integer]
        integer = 1

        [float]
        float = 1.0

        [decimal]
        decimal = 0.1

        [string]
        string = test

        [path]
        path = root
    """


def _get_config_compress() -> str:
    return """
        [bool]
        true=True
        [int]
        one=1
    """


def _get_config_lower() -> str:
    return """
        [SECTION]
        true = True
        false = False
    """


def _get_config_invalid() -> str:
    return """
        [section]
        key = True
    """


def _get_config_export() -> str:
    return """
        [true]
        true = True

        [false]
        false = False
    """


def _common_test(expected: str, source: Config) -> None:
    _difference_error(
        config_dump(source),
        format_indent(expected, stdout=True),
    )


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_source_bool() -> BoolPair:
    return {"bool": True}


def _get_source_bool_nest() -> BoolPair2:
    return {"bool": _get_source_bool()}


def _get_source_integer() -> IntPair:
    return {"integer": 1}


def _get_source_integer_nest() -> IntPair2:
    return {"integer": _get_source_integer()}


def _get_source_float() -> FloatPair:
    return {"float": 1.0}


def _get_source_float_nest() -> FloatPair2:
    return {"float": _get_source_float()}


def _get_source_decimal() -> DecPair:
    return {"decimal": Decimal("0.1")}


def _get_source_decimal_nest() -> DecPair2:
    return {"decimal": _get_source_decimal()}


def _get_source_string() -> StrPair:
    return {"string": "test"}


def _get_source_string_nest() -> StrPair2:
    return {"string": _get_source_string()}


def _get_source_path() -> PathPair:
    return {"path": Path("root")}


def _get_source_path_nest() -> PathPair2:
    return {"path": _get_source_path()}


def _get_source_mix_section() -> SinglePair:
    return {
        "bool": _get_source_bool()["bool"],
        "integer": _get_source_integer()["integer"],
        "float": _get_source_float()["float"],
        "decimal": _get_source_decimal()["decimal"],
        "string": _get_source_string()["string"],
        "path": _get_source_path()["path"],
    }


def _get_source_mix() -> SinglePair2:
    return {"section": _get_source_mix_section()}


def _get_source_group() -> SectionPair:
    return {
        "bool": _get_source_bool(),
        "integer": _get_source_integer(),
        "float": _get_source_float(),
        "decimal": _get_source_decimal(),
        "string": _get_source_string(),
        "path": _get_source_path(),
    }


def _get_source_compress() -> SectionPair:
    return {"bool": {"true": True}, "integer": {"one": 1}}


def _get_source_lower() -> Config:
    return {"SECTION": {"TRUE": True, "FALSE": False}}


def test_bool() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "bool".
    """
    expected: str = _get_config_bool()

    _common_test(expected, {"bool": _get_source_bool()})
    _common_test(expected, _get_source_bool_nest())


def test_integer() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "int".
    """
    expected: str = _get_config_integer()

    _common_test(expected, {"integer": _get_source_integer()})
    _common_test(expected, _get_source_integer_nest())


def test_float() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "float".
    """
    expected: str = _get_config_float()

    _common_test(expected, {"float": _get_source_float()})
    _common_test(expected, _get_source_float_nest())


def test_decimal() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "Decimal".
    """
    expected: str = _get_config_decimal()

    _common_test(expected, {"decimal": _get_source_decimal()})
    _common_test(expected, _get_source_decimal_nest())


def test_string() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "str".
    """
    expected: str = _get_config_string()

    _common_test(expected, {"string": _get_source_string()})
    _common_test(expected, _get_source_string_nest())


def test_path() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "Path".
    """
    expected: str = _get_config_path()

    _common_test(expected, {"path": _get_source_path()})
    _common_test(expected, _get_source_path_nest())


def test_mix() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with multiple mixed type.
    """
    _common_test(_get_config_mix(), _get_source_mix())


def test_mix_group() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary, the rule of dictionary is follow.

    1. Child dictionary is structured with same type values.

    2. Parent dictionary is structured with multiple child dictionaries.
    """
    _common_test(_get_config_mix_group(), _get_source_group())


def test_compress() -> None:
    """Test to convert data used for configuration file.

    Test for compress option is enable.
    """
    _difference_error(
        config_dump(_get_source_compress(), compress=True),
        format_indent(_get_config_compress()),
    )


def test_lower() -> None:
    """Test to convert data used for configuration file.

    Test for upper case of keys is enable.
    """
    _common_test(_get_config_lower(), _get_source_lower())


def test_noise() -> None:
    """Test to convert data used for configuration file with noisy keys."""
    noise: Strs = [" 　\n\t"] * 2
    source_pairs: Config = {"section".join(noise): {"key".join(noise): True}}
    expected: str = _get_config_invalid()

    _common_test(expected, source_pairs)


def test_export() -> None:
    """Test to export data used for configuration file."""
    source_pairs: Config = {"true": {"true": True}, "false": {"false": False}}
    expected: str = _get_config_export()

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            text_import(
                config_export(
                    Path(temporary_root, "temporary.ini"),
                    source_pairs,
                ),
            ),
            format_indent(expected, stdout=True),
        )

    _inside_temporary_directory(individual_test)
