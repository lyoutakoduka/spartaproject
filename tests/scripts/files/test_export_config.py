#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from contexts.bool_context import BoolPair, BoolPair2
from contexts.config_context import Config
from contexts.decimal_context import Decimal, DecPair, DecPair2
from contexts.float_context import FloatPair, FloatPair2
from contexts.integer_context import IntPair, IntPair2
from contexts.path_context import Path, PathPair, PathPair2
from contexts.string_context import StrPair, StrPair2
from scripts.files.export_config import config_dump, config_export
from scripts.files.import_file import text_import
from scripts.format_texts import format_indent


def _common_test(expected: str, input: Config) -> None:
    assert format_indent(expected) == config_dump(input)


def test_lower() -> None:
    INPUT: Config = {'SECTION': {'TRUE': True, 'FALSE': False}}
    EXPECTED: str = """
        [SECTION]
        true = True
        false = False
    """

    _common_test(EXPECTED, INPUT)


def test_bool() -> None:
    INPUT: BoolPair = {'b': True}
    input_pair: BoolPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        b = True
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_int() -> None:
    INPUT: IntPair = {'b': 1}
    input_pair: IntPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        b = 1
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_float() -> None:
    INPUT: FloatPair = {'b': 1.0}
    input_pair: FloatPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        b = 1.0
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_str() -> None:
    INPUT: StrPair = {'b': 'test'}
    input_pair: StrPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        b = test
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_decimal() -> None:
    INPUT: DecPair = {'b': Decimal('0.1')}
    input_pair: DecPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        b = 0.1
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_path() -> None:
    INPUT: PathPair = {'path': Path('root')}
    input_pair: PathPair2 = {'A': INPUT}
    EXPECTED: str = """
        [A]
        path = root
    """
    _common_test(EXPECTED, {'A': INPUT})
    _common_test(EXPECTED, input_pair)


def test_mix_option() -> None:
    INPUT: Config = {
        'section': {
            'bool': True,
            'int': 1,
            'float': 1.0,
            'str': 'test',
            'decimal': Decimal('0.1'),
            'path': Path('root'),
        }
    }

    EXPECTED: str = """
        [section]
        bool = True
        int = 1
        float = 1.0
        str = test
        decimal = 0.1
        path = root
    """

    _common_test(EXPECTED, INPUT)


def test_mix_section() -> None:
    flags: BoolPair = {'bool': True}
    indies: IntPair = {'int': 1}
    numbers: FloatPair = {'float': 1.0}
    texts: StrPair = {'str': 'test'}
    decimals: DecPair = {'decimal': Decimal('0.1')}
    paths: PathPair = {'path': Path('root')}

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

    _common_test(EXPECTED, INPUT)


def test_compress() -> None:
    INPUT: Config = {'bool': {'true': True}, 'int': {'one': 1}}
    EXPECTED: str = "[bool]\ntrue=True\n[int]\none=1"

    assert EXPECTED == config_dump(INPUT, compress=True)


def test_export() -> None:
    INPUT: Config = {'section': {'option': 'value'}}
    EXPECTED: str = """
        [section]
        option = value
    """

    expected: str = format_indent(EXPECTED)

    with TemporaryDirectory() as tmp_path:
        config_path: Path = config_export(Path(tmp_path, 'tmp.ini'), INPUT)
        assert expected == text_import(config_path)


def main() -> bool:
    test_lower()
    test_bool()
    test_int()
    test_float()
    test_str()
    test_decimal()
    test_path()
    test_mix_option()
    test_mix_section()
    test_compress()
    test_export()
    return True
