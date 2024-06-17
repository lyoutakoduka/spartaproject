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


def _get_section(formatted: str) -> Basic:
    config: Config = config_load(formatted)
    return config["section"]["option"]


def test_bool() -> None:
    source: str = """
        [section]
        option=True
    """

    assert _get_section(format_indent(source))


def test_integer() -> None:
    source: str = """
        [section]
        option=1
    """
    expected: int = 1

    assert expected == _get_section(format_indent(source))


def test_decimal() -> None:
    source: str = """
        [section]
        option=1.0
    """
    expected: Decimal = Decimal("1.0")

    assert expected == _get_section(format_indent(source))


def test_string() -> None:
    source: str = """
        [section]
        option=text
    """
    expected: str = "text"

    assert expected == _get_section(format_indent(source))


def test_path() -> None:
    source: str = """
        [section]
        path=text
    """
    expected: Path = Path("text")

    config: Config = config_load(format_indent(source))
    assert expected == config["section"]["path"]


def test_import() -> None:
    source: str = """
        [section]
        option=text
    """
    expected: str = "text"

    with TemporaryDirectory() as temporary_path:
        config: Config = config_import(
            text_export(
                Path(temporary_path, "temporary.ini"), format_indent(source)
            )
        )
        assert expected == config["section"]["option"]
