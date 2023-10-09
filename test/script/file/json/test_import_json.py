#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

from pyspartaproj.context.file.json_context import Json, Single
from pyspartaproj.script.file.json.export_json import json_export
from pyspartaproj.script.file.json.import_json import json_import, json_load


def _common_test(expected: Single, source: str) -> None:
    result: Json = json_load('{"group": %s}' % source)

    assert isinstance(result, Dict)
    assert expected == result["group"]


def test_none() -> None:
    expected: None = None
    _common_test(expected, "null")


def test_bool() -> None:
    expected: bool = True
    _common_test(expected, "true")


def test_integer() -> None:
    expected: int = 1
    _common_test(expected, str(expected))


def test_float() -> None:
    expected: float = 0.1
    _common_test(expected, str(expected))


def test_string() -> None:
    expected: str = "test"
    _common_test(expected, '"%s"' % expected)


def test_export() -> None:
    expected: Json = [None, True, 1, "test"]

    with TemporaryDirectory() as temporary_path:
        assert expected == json_import(
            json_export(Path(temporary_path, "temporary.ini"), expected)
        )


def main() -> bool:
    test_none()
    test_bool()
    test_integer()
    test_float()
    test_string()
    test_export()
    return True
