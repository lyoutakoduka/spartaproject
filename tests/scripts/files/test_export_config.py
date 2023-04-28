#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from contexts.path_context import Path
from contexts.config_context import Config
from scripts.files.export_config import config_dump, config_export
from scripts.format_texts import format_indent


_JSON_INPUT: Config = {
    'section': {
        'str': '1',
        'float': 1.0,
        'int': 1,
        'bool': True,
    }
}

# 2 space indent
_EXPECTED_SRC: str = """
    [section]
    str = 1
    float = 1.0
    int = 1
    bool = True
"""


def test_dump() -> None:
    EXPECTED: str = format_indent(_EXPECTED_SRC)
    assert EXPECTED == config_dump(_JSON_INPUT)


def test_export() -> None:
    EXPECTED: str = format_indent(_EXPECTED_SRC)

    with TemporaryDirectory() as tmp_path:
        export_path: Path = Path(tmp_path, 'tmp.json')
        config_export(export_path, _JSON_INPUT)

        with open(export_path, 'r') as file:
            assert EXPECTED == file.read()


def test_lower() -> None:
    _JSON_INPUT: Config = {
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
    assert expected == config_dump(_JSON_INPUT)


def main() -> bool:
    test_dump()
    test_export()
    test_lower()
    return True
