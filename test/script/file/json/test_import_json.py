#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

from context.json_context import Json, Single
from script.file.json.export_json import json_export
from script.file.json.import_json import json_load, json_import


def _common_test(input: Single, result: Json) -> None:
    assert isinstance(result, Dict)
    assert input == result['group']


def _get_input_json(input: str) -> str:
    return '{"group": %s}' % input


def test_none() -> None:
    input: None = None
    _common_test(input, json_load(_get_input_json('null')))


def test_bool() -> None:
    input: bool = True
    _common_test(input, json_load(_get_input_json('true')))


def test_integer() -> None:
    input: int = 1
    _common_test(input, json_load(_get_input_json(str(input))))


def test_float() -> None:
    input: float = 0.1
    _common_test(input, json_load(_get_input_json(str(input))))


def test_string() -> None:
    input: str = 'test'
    _common_test(input, json_load(_get_input_json('"%s"' % input)))


def test_export() -> None:
    INPUT: Json = [None, True, 1, 'test']

    with TemporaryDirectory() as temporary_path:
        assert INPUT == json_import(
            json_export(Path(temporary_path, 'temporary.ini'), INPUT)
        )


def main() -> bool:
    test_none()
    test_bool()
    test_integer()
    test_float()
    test_string()
    test_export()
    return True
