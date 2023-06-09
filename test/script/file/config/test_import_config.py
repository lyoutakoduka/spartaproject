#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from context.file.config_context import Config, Basic
from script.file.config.import_config import config_load, config_import
from script.file.text.export_file import text_export


def _get_section(input: str) -> Basic:
    config: Config = config_load(input)
    return config['section']['option']


def test_bool() -> None:
    INPUT: str = "[section]\noption=True"
    assert _get_section(INPUT)


def test_integer() -> None:
    INPUT: str = "[section]\noption=1"
    EXPECTED: int = 1
    assert EXPECTED == _get_section(INPUT)


def test_decimal() -> None:
    INPUT: str = "[section]\noption=1.0"
    EXPECTED: Decimal = Decimal('1.0')
    assert EXPECTED == _get_section(INPUT)


def test_string() -> None:
    INPUT: str = "[section]\noption=text"
    EXPECTED: str = 'text'
    assert EXPECTED == _get_section(INPUT)


def test_path() -> None:
    INPUT: str = "[section]\npath=text"
    EXPECTED: Path = Path('text')
    config: Config = config_load(INPUT)
    assert EXPECTED == config['section']['path']


def test_import() -> None:
    INPUT: str = "[section]\noption=text"
    EXPECTED: str = 'text'
    with TemporaryDirectory() as temporary_path:
        config: Config = config_import(
            text_export(Path(temporary_path, 'temporary.ini'), INPUT)
        )
        assert EXPECTED == config['section']['option']


def main() -> bool:
    test_bool()
    test_integer()
    test_decimal()
    test_string()
    test_path()
    test_import()
    return True
