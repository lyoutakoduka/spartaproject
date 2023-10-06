#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.file.config_context import Basic, Config
from pyspartaproj.script.file.config.import_config import (
    config_import,
    config_load,
)
from pyspartaproj.script.file.text.export_file import text_export
from pyspartaproj.script.string.format_texts import format_indent


def _get_section(input: str) -> Basic:
    config: Config = config_load(input)
    return config["section"]["option"]


def test_bool() -> None:
    INPUT: str = """
        [section]
        option=True
    """

    assert _get_section(format_indent(INPUT))


def test_integer() -> None:
    INPUT: str = """
        [section]
        option=1
    """
    EXPECTED: int = 1

    assert EXPECTED == _get_section(format_indent(INPUT))


def test_decimal() -> None:
    INPUT: str = """
        [section]
        option=1.0
    """
    EXPECTED: Decimal = Decimal("1.0")

    assert EXPECTED == _get_section(format_indent(INPUT))


def test_string() -> None:
    INPUT: str = """
        [section]
        option=text
    """
    EXPECTED: str = "text"

    assert EXPECTED == _get_section(format_indent(INPUT))


def test_path() -> None:
    INPUT: str = """
        [section]
        path=text
    """
    EXPECTED: Path = Path("text")

    config: Config = config_load(format_indent(INPUT))
    assert EXPECTED == config["section"]["path"]


def test_import() -> None:
    INPUT: str = """
        [section]
        option=text
    """
    EXPECTED: str = "text"

    with TemporaryDirectory() as temporary_path:
        config: Config = config_import(
            text_export(
                Path(temporary_path, "temporary.ini"), format_indent(INPUT)
            )
        )
        assert EXPECTED == config["section"]["option"]


def main() -> bool:
    test_bool()
    test_integer()
    test_decimal()
    test_string()
    test_path()
    test_import()
    return True
