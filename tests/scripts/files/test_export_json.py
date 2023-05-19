#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from scripts.files.export_json import json_dump, json_export
from scripts.files.import_file import text_import
from scripts.format_texts import format_indent


def _common_test(expected: str, input: Json, compress: bool = False) -> None:
    assert expected == json_dump(input, compress=compress)


def test_default() -> None:
    INPUT: Json = {
        'None': None,
        'bool': True,
        'int': 1,
        'float': 1.0,
        'str': '1',
    }

    # 2 space indent
    EXPECTED: str = """
      {
        "None": null,
        "bool": true,
        "float": 1.0,
        "int": 1,
        "str": "1"
      }
    """

    _common_test(format_indent(EXPECTED), INPUT)


def test_extend() -> None:
    INPUT: Json = [Path('R'), Decimal('1.0')]
    EXPECTED: str = '["R",1.0]'
    _common_test(EXPECTED, INPUT, compress=True)


def test_tree() -> None:
    INPUT: Json = {'0': {'1': {'2': {'3': {'4': {'5': {'6': None}}}}}}}
    EXPECTED: str = '''{"0":{"1":{"2":{"3":{"4":{"5":{"6":null}}}}}}}'''
    _common_test(EXPECTED, INPUT, compress=True)


def test_export() -> None:
    INPUT: Json = ['R', 'G', 'B']
    EXPECTED: str = '["R","G","B"]'

    with TemporaryDirectory() as tmp_path:
        json_path: Path = json_export(
            Path(tmp_path, 'tmp.json'),
            INPUT,
            compress=True,
        )
        assert EXPECTED == text_import(json_path)


def main() -> bool:
    test_default()
    test_extend()
    test_tree()
    test_export()
    return True
