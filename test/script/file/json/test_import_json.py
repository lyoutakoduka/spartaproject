#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

from pyspartaproj.context.file.json_context import Json, Single
from pyspartaproj.script.file.json.export_json import json_export
from pyspartaproj.script.file.json.import_json import json_import, json_load


def _common_test(input: Single, source: str) -> None:
    result: Json = json_load('{"group": %s}' % source)

    assert isinstance(result, Dict)
    assert input == result["group"]


def test_none() -> None:
    input: None = None
    _common_test(input, "null")


def test_bool() -> None:
    input: bool = True
    _common_test(input, "true")


def test_integer() -> None:
    input: int = 1
    _common_test(input, str(input))


def test_float() -> None:
    input: float = 0.1
    _common_test(input, str(input))


def test_string() -> None:
    input: str = "test"
    _common_test(input, '"%s"' % input)


def test_export() -> None:
    input: Json = [None, True, 1, "test"]

    with TemporaryDirectory() as temporary_path:
        assert input == json_import(
            json_export(Path(temporary_path, "temporary.ini"), input)
        )


def main() -> bool:
    test_none()
    test_bool()
    test_integer()
    test_float()
    test_string()
    test_export()
    return True
