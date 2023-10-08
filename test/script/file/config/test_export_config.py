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


def _common_test(expected: str, input: Config) -> None:
    assert format_indent(expected, stdout=True) == config_dump(input)


def test_bool() -> None:
    input: BoolPair = {"b": True}
    input_pair: BoolPair2 = {"A": input}
    expected: str = """
        [A]
        b = True
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_integer() -> None:
    input: IntPair = {"b": 1}
    input_pair: IntPair2 = {"A": input}
    expected: str = """
        [A]
        b = 1
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_float() -> None:
    input: FloatPair = {"b": 1.0}
    input_pair: FloatPair2 = {"A": input}
    expected: str = """
        [A]
        b = 1.0
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_string() -> None:
    input: StrPair = {"b": "test"}
    input_pair: StrPair2 = {"A": input}
    expected: str = """
        [A]
        b = test
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_decimal() -> None:
    input: DecPair = {"b": Decimal("0.1")}
    input_pair: DecPair2 = {"A": input}
    expected: str = """
        [A]
        b = 0.1
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_path() -> None:
    input: PathPair = {"path": Path("root")}
    input_pair: PathPair2 = {"A": input}
    expected: str = """
        [A]
        path = root
    """
    _common_test(expected, {"A": input})
    _common_test(expected, input_pair)


def test_mix_option() -> None:
    input: Config = {
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

    _common_test(expected, input)


def test_mix_section() -> None:
    flags: BoolPair = {"bool": True}
    indies: IntPair = {"int": 1}
    numbers: FloatPair = {"float": 1.0}
    texts: StrPair = {"str": "test"}
    decimals: DecPair = {"decimal": Decimal("0.1")}
    paths: PathPair = {"path": Path("root")}

    input: Config = {
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

    _common_test(expected, input)


def test_compress() -> None:
    input: Config = {"bool": {"true": True}, "int": {"one": 1}}
    expected: str = """
        [bool]
        true=True
        [int]
        one=1
    """
    expected: str = format_indent(expected)

    assert expected == config_dump(input, compress=True)


def test_lower() -> None:
    input: Config = {"SECTION": {"TRUE": True, "FALSE": False}}
    expected: str = """
        [SECTION]
        true = True
        false = False
    """

    _common_test(expected, input)


def test_key() -> None:
    noise: Strs = [" 　\n\t"] * 2
    input: Config = {"section".join(noise): {"key".join(noise): True}}
    expected: str = """
        [section]
        key = True
    """

    _common_test(expected, input)


def test_export() -> None:
    input: Config = {"true": {"true": True}, "false": {"false": False}}
    expected: str = """
        [true]
        true = True

        [false]
        false = False
    """

    expected: str = format_indent(expected, stdout=True)

    with TemporaryDirectory() as temporary_path:
        assert expected == text_import(
            config_export(Path(temporary_path, "temporary.ini"), input)
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
