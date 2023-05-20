#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from contexts.bool_context import BoolPair
from contexts.config_context import Config
from contexts.decimal_context import Decimal, DecPair
from contexts.float_context import FloatPair
from contexts.integer_context import IntPair
from contexts.path_context import Path, PathPair
from contexts.string_context import StrPair
from scripts.files.export_config import config_dump, config_export
from scripts.files.import_file import text_import
from scripts.format_texts import format_indent


def _common_test(expected: str, input: Config) -> None:
    assert format_indent(expected) == config_dump(input)


def test_section() -> None:
    INPUT: Config = {
        'section': {
            'path': Path('root'),
            'decimal': Decimal('0.1'),
            'str': '1',
            'float': 1.0,
            'int': 1,
            'bool': True,
        }
    }

    EXPECTED: str = """
        [section]
        path = root
        decimal = 0.1
        str = 1
        float = 1.0
        int = 1
        bool = True
    """

    _common_test(EXPECTED, INPUT)


def test_lower() -> None:
    INPUT: Config = {
        'SECTION': {
            'TRUE': True,
            'FALSE': False
        }
    }

    EXPECTED: str = """
        [SECTION]
        true = True
        false = False
    """

    _common_test(EXPECTED, INPUT)


def test_type() -> None:
    flags: BoolPair = {'a': True}
    indies: IntPair = {'b': 1}
    numbers: FloatPair = {'c': 1.0}
    texts: StrPair = {'d': 'hello'}
    decimals: DecPair = {'e': Decimal('0.1')}
    paths: PathPair = {'f': Path('root')}

    INPUT: Config = {
        'flags': flags,
        'indies': indies,
        'numbers': numbers,
        'texts': texts,
        'decimals': decimals,
        'paths': paths,
    }

    EXPECTED: str = """
        [flags]
        a = True

        [indies]
        b = 1

        [numbers]
        c = 1.0

        [texts]
        d = hello

        [decimals]
        e = 0.1

        [paths]
        f = root
    """

    _common_test(EXPECTED, INPUT)


def test_export() -> None:
    INPUT: Config = {
        'section': {
            'option': 'value',
        }
    }

    EXPECTED: str = """
        [section]
        option = value
    """

    expected: str = format_indent(EXPECTED)

    with TemporaryDirectory() as tmp_path:
        config_path: Path = config_export(Path(tmp_path, 'tmp.ini'), INPUT)
        assert expected == text_import(config_path)


def main() -> bool:
    test_section()
    test_lower()
    test_type()
    test_export()
    return True
