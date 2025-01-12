#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to import configuration file or load configuration data."""

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.file.config_context import Basic, Config
from pyspartalib.script.file.config.import_config import (
    config_import,
    config_load,
)
from pyspartalib.script.file.text.export_file import text_export
from pyspartalib.script.string.format_texts import format_indent


def _get_section(formatted: str) -> Basic:
    config: Config = config_load(formatted)
    return config["section"]["option"]


def test_bool() -> None:
    """Test to load configuration data as type boolean."""
    source: str = """
        [section]
        option=True
    """

    assert _get_section(format_indent(source))


def test_integer() -> None:
    """Test to load configuration data as type integer."""
    source: str = """
        [section]
        option=1
    """
    expected: int = 1

    assert expected == _get_section(format_indent(source))


def test_decimal() -> None:
    """Test to load configuration data as type decimal."""
    source: str = """
        [section]
        option=1.0
    """
    expected: Decimal = Decimal("1.0")

    assert expected == _get_section(format_indent(source))


def test_string() -> None:
    """Test to load configuration data as type string."""
    source: str = """
        [section]
        option=text
    """
    expected: str = "text"

    assert expected == _get_section(format_indent(source))


def test_path() -> None:
    """Test to load configuration data as type path."""
    source: str = """
        [section]
        path=text
    """
    expected: Path = Path("text")

    config: Config = config_load(format_indent(source))
    assert expected == config["section"]["path"]


def test_import() -> None:
    """Test to import configuration file as format "ini"."""
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
