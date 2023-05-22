#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

from contexts.json_context import Json
from scripts.files.export_json import json_export
from scripts.files.import_json import json_load, json_import


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


def test_float() -> None:
    content: Json = json_load(_get_input_json('0.1'))
    if isinstance(content, Dict):
        assert 0.1 == content['group']


def test_string() -> None:
    content: Json = json_load(_get_input_json('"test"'))
    if isinstance(content, Dict):
        assert 'test' == content['group']


def test_export() -> None:
    INPUT: Json = [None, True, 1, 'test']

    with TemporaryDirectory() as tmp_path:
        json_path: Path = json_export(Path(tmp_path, 'tmp.ini'), INPUT)
        assert INPUT == json_import(json_path)


def main() -> bool:
    test_bool()
    test_int()
    test_float()
    test_string()
    test_export()
    return True
