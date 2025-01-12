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
        [A]
        b = True
    """


def _get_config_integer() -> str:
    return """
        [A]
        b = 1
    """


def _get_config_float() -> str:
    return """
        [A]
        b = 1.0
    """


def _get_config_decimal() -> str:
    return """
        [A]
        b = 0.1
    """


def _get_config_string() -> str:
    return """
        [A]
        b = test
    """


def _get_config_path() -> str:
    return """
        [A]
        path = root
    """


def _get_config_mix() -> str:
    return """
        [section]
        bool = True
        int = 1
        float = 1.0
        str = test
        decimal = 0.1
        path = root
    """


def _get_config_mix_section() -> str:
    return """
        [flags]
        bool = True

        [indies]
        int = 1

        [numbers]
        float = 1.0

        [texts]
        str = test

        [decimals]
        decimal = 0.1

        [paths]
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


def _common_test(expected: str, source: Config) -> None:
    _difference_error(
        config_dump(source),
        format_indent(expected, stdout=True),
    )


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_bool() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "bool".
    """
    source_pair: BoolPair = {"b": True}
    source_pairs: BoolPair2 = {"A": source_pair}
    expected: str = _get_config_bool()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_integer() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "int".
    """
    source_pair: IntPair = {"b": 1}
    source_pairs: IntPair2 = {"A": source_pair}
    expected: str = _get_config_integer()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_float() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "float".
    """
    source_pair: FloatPair = {"b": 1.0}
    source_pairs: FloatPair2 = {"A": source_pair}
    expected: str = _get_config_float()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_string() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "str".
    """
    source_pair: StrPair = {"b": "test"}
    source_pairs: StrPair2 = {"A": source_pair}
    expected: str = _get_config_string()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_decimal() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "Decimal".
    """
    source_pair: DecPair = {"b": Decimal("0.1")}
    source_pairs: DecPair2 = {"A": source_pair}
    expected: str = _get_config_decimal()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_path() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with type "Path".
    """
    source_pair: PathPair = {"path": Path("root")}
    source_pairs: PathPair2 = {"A": source_pair}
    expected: str = _get_config_path()

    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_mix() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary created with multiple mixed type.
    """
    source_pairs: SinglePair2 = {
        "section": {
            "bool": True,
            "int": 1,
            "float": 1.0,
            "str": "test",
            "decimal": Decimal("0.1"),
            "path": Path("root"),
        },
    }
    expected: str = _get_config_mix()

    _common_test(expected, source_pairs)


def test_mix_section() -> None:
    """Test to convert data used for configuration file to text.

    Data is 2 dimensional dictionary, the rule of dictionary is follow.

    1. Child dictionary is structured with same type values.

    2. Parent dictionary is structured with multiple child dictionaries.
    """
    flags: BoolPair = {"bool": True}
    indies: IntPair = {"int": 1}
    numbers: FloatPair = {"float": 1.0}
    texts: StrPair = {"str": "test"}
    decimals: DecPair = {"decimal": Decimal("0.1")}
    paths: PathPair = {"path": Path("root")}

    source_pairs: SectionPair = {
        "flags": flags,
        "indies": indies,
        "numbers": numbers,
        "texts": texts,
        "decimals": decimals,
        "paths": paths,
    }
    expected: str = _get_config_mix_section()

    _common_test(expected, source_pairs)


def test_compress() -> None:
    """Test to convert data used for configuration file.

    Test for compress option is enable.
    """
    source_pairs: SectionPair = {"bool": {"true": True}, "int": {"one": 1}}
    expected: str = _get_config_compress()

    _difference_error(
        config_dump(source_pairs, compress=True),
        format_indent(expected),
    )


def test_lower() -> None:
    """Test to convert data used for configuration file.

    Test for upper case of keys is enable.
    """
    source_pairs: Config = {"SECTION": {"TRUE": True, "FALSE": False}}
    expected: str = _get_config_lower()

    _common_test(expected, source_pairs)


def test_key() -> None:
    """Test to convert data used for configuration file with noisy keys."""
    noise: Strs = [" 　\n\t"] * 2
    source_pairs: Config = {"section".join(noise): {"key".join(noise): True}}
    expected: str = """
        [section]
        key = True
    """

    _common_test(expected, source_pairs)


def test_export() -> None:
    """Test to export data used for configuration file."""
    source_pairs: Config = {"true": {"true": True}, "false": {"false": False}}
    expected: str = """
        [true]
        true = True

        [false]
        false = False
    """

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
