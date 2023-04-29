#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from contexts.bool_context import BoolPair
from contexts.integer_context import IntPair
from contexts.float_context import FloatPair
from contexts.string_context import StrPair
from contexts.decimal_context import Decimal, DecPair
from contexts.path_context import Path, PathPair
from contexts.config_context import Config, Section
from scripts.files.export_config import config_dump, config_export
from scripts.format_texts import format_indent


_CONFIG_INPUT: Config = {
    'section': {
        'path': Path('root'),
        'decimal': Decimal('0.1'),
        'str': '1',
        'float': 1.0,
        'int': 1,
        'bool': True,
    }
}

# 2 space indent
_EXPECTED_SRC: str = """
    [section]
    path = root
    decimal = 0.1
    str = 1
    float = 1.0
    int = 1
    bool = True
"""


def test_dump() -> None:
    INPUT: Section = {
        'path': Path('root'),
        'decimal': Decimal('0.1'),
        'str': '1',
        'float': 1.0,
        'int': 1,
        'bool': True,
    }
    config_input: Config = {'section': INPUT}

    EXPECTED: str = """
        [section]
        path = root
        decimal = 0.1
        str = 1
        float = 1.0
        int = 1
        bool = True
    """

    expected: str = format_indent(EXPECTED)
    assert expected == config_dump(config_input)


def test_export() -> None:
    expected: str = format_indent(_EXPECTED_SRC)

    with TemporaryDirectory() as tmp_path:
        export_path: Path = Path(tmp_path, 'tmp.json')
        config_export(export_path, _CONFIG_INPUT)

        with open(export_path, 'r') as file:
            assert expected == file.read()


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

    expected: str = format_indent(EXPECTED)
    assert expected == config_dump(INPUT)


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

    expected: str = format_indent(EXPECTED)
    assert expected == config_dump(INPUT)


def main() -> bool:
    test_dump()
    test_export()
    test_lower()
    test_type()
    return True
