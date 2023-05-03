#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from scripts.files.import_json import json_load, json_import
from scripts.files.export_json import json_export


def _get_input_json(input: str) -> str:
    return '{"group": ' + input + '}'


def test_bool() -> None:
    content: Json = json_load(_get_input_json('true'))
    if isinstance(content, Dict):
        assert content['group']


def test_int() -> None:
    content: Json = json_load(_get_input_json('1'))
    if isinstance(content, Dict):
        assert 1 == content['group']


def test_decimal() -> None:
    content: Json = json_load(_get_input_json('0.1'))
    if isinstance(content, Dict):
        assert Decimal('0.1') == content['group']


def test_string() -> None:
    content: Json = json_load(_get_input_json('"test"'))
    if isinstance(content, Dict):
        assert 'test' == content['group']


def test_path() -> None:
    content: Json = json_load('{"path": "root"}')
    if isinstance(content, Dict):
        assert Path('root') == content['path']


def test_export() -> None:
    INPUT: Json = [None, True, 1, 'test']

    with TemporaryDirectory() as tmp_path:
        json_path: Path = Path(tmp_path, 'tmp.ini')
        json_export(json_path, INPUT)
        assert INPUT == json_import(json_path)


def main() -> bool:
    test_bool()
    test_int()
    test_decimal()
    test_string()
    test_path()
    test_export()
    return True
