#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.default.bool_context import BoolPair, BoolPair2
from pyspartaproj.context.default.float_context import FloatPair, FloatPair2
from pyspartaproj.context.default.integer_context import IntPair, IntPair2
from pyspartaproj.context.default.string_context import StrPair, StrPair2, Strs
from pyspartaproj.context.extension.decimal_context import DecPair, DecPair2
from pyspartaproj.context.extension.path_context import PathPair, PathPair2
from pyspartaproj.context.file.config_context import Config
from pyspartaproj.script.file.config.export_config import (
    config_dump,
    config_export,
)
from pyspartaproj.script.file.text.import_file import text_import
from pyspartaproj.script.string.format_texts import format_indent


def _common_test(expected: str, source: Config) -> None:
    assert format_indent(expected, stdout=True) == config_dump(source)


def test_bool() -> None:
    source_pair: BoolPair = {"b": True}
    source_pairs: BoolPair2 = {"A": source_pair}
    expected: str = """
        [A]
        b = True
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_integer() -> None:
    source_pair: IntPair = {"b": 1}
    source_pairs: IntPair2 = {"A": source_pair}
    expected: str = """
        [A]
        b = 1
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_float() -> None:
    source_pair: FloatPair = {"b": 1.0}
    source_pairs: FloatPair2 = {"A": source_pair}
    expected: str = """
        [A]
        b = 1.0
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_string() -> None:
    source_pair: StrPair = {"b": "test"}
    source_pairs: StrPair2 = {"A": source_pair}
    expected: str = """
        [A]
        b = test
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_decimal() -> None:
    source_pair: DecPair = {"b": Decimal("0.1")}
    source_pairs: DecPair2 = {"A": source_pair}
    expected: str = """
        [A]
        b = 0.1
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_path() -> None:
    source_pair: PathPair = {"path": Path("root")}
    source_pairs: PathPair2 = {"A": source_pair}
    expected: str = """
        [A]
        path = root
    """
    _common_test(expected, {"A": source_pair})
    _common_test(expected, source_pairs)


def test_mix_option() -> None:
    source_pairs: Config = {
        "section": {
            "bool": True,
            "int": 1,
            "float": 1.0,
            "str": "test",
            "decimal": Decimal("0.1"),
            "path": Path("root"),
        }
    }

    expected: str = """
        [section]
        bool = True
        int = 1
        float = 1.0
        str = test
        decimal = 0.1
        path = root
    """

    _common_test(expected, source_pairs)


def test_mix_section() -> None:
    flags: BoolPair = {"bool": True}
    indies: IntPair = {"int": 1}
    numbers: FloatPair = {"float": 1.0}
    texts: StrPair = {"str": "test"}
    decimals: DecPair = {"decimal": Decimal("0.1")}
    paths: PathPair = {"path": Path("root")}

    source_pairs: Config = {
        "flags": flags,
        "indies": indies,
        "numbers": numbers,
        "texts": texts,
        "decimals": decimals,
        "paths": paths,
    }

    expected: str = """
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

    _common_test(expected, source_pairs)


def test_compress() -> None:
    source_pairs: Config = {"bool": {"true": True}, "int": {"one": 1}}
    expected: str = """
        [bool]
        true=True
        [int]
        one=1
    """
    expected: str = format_indent(expected)

    assert expected == config_dump(source_pairs, compress=True)


def test_lower() -> None:
    source_pairs: Config = {"SECTION": {"TRUE": True, "FALSE": False}}
    expected: str = """
        [SECTION]
        true = True
        false = False
    """

    _common_test(expected, source_pairs)


def test_key() -> None:
    noise: Strs = [" 　\n\t"] * 2
    source_pairs: Config = {"section".join(noise): {"key".join(noise): True}}
    expected: str = """
        [section]
        key = True
    """

    _common_test(expected, source_pairs)


def test_export() -> None:
    source_pairs: Config = {"true": {"true": True}, "false": {"false": False}}
    expected: str = """
        [true]
        true = True

        [false]
        false = False
    """

    expected: str = format_indent(expected, stdout=True)

    with TemporaryDirectory() as temporary_path:
        assert expected == text_import(
            config_export(Path(temporary_path, "temporary.ini"), source_pairs)
        )


def main() -> bool:
    test_bool()
    test_integer()
    test_float()
    test_string()
    test_decimal()
    test_path()
    test_mix_option()
    test_mix_section()
    test_compress()
    test_lower()
    test_key()
    test_export()
    return True
