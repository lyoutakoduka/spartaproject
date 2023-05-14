#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from contexts.config_context import Config, Basic
from scripts.files.export_file import text_export
from scripts.files.import_config import config_load, config_import
from scripts.format_texts import format_indent


def _get_section(input: str) -> Basic:
    config: Config = config_load(input)
    return config['section']['option']


def test_bool() -> None:
    INPUT: str = """
        [section]
        option = True
    """
    assert _get_section(INPUT)


def test_int() -> None:
    INPUT: str = """
        [section]
        option = 1
    """
    assert 1 == _get_section(INPUT)


def test_decimal() -> None:
    INPUT: str = """
        [section]
        option = 1.0
    """
    assert Decimal('1.0') == _get_section(INPUT)


def test_string() -> None:
    INPUT: str = """
        [section]
        option = text
    """
    assert 'text' == _get_section(INPUT)


def test_path() -> None:
    INPUT: str = """
        [section]
        path = text
    """
    config: Config = config_load(INPUT)
    assert Path('text') == config['section']['path']


def test_import() -> None:
    INPUT: str = """
        [section]
        option = text
    """
    input: str = format_indent(INPUT)

    with TemporaryDirectory() as tmp_path:
        config_path: Path = text_export(Path(tmp_path, 'tmp.ini'), input)
        config: Config = config_import(config_path)
        assert 'text' == config['section']['option']


def main() -> bool:
    test_bool()
    test_int()
    test_decimal()
    test_string()
    test_path()
    test_import()
    return True
