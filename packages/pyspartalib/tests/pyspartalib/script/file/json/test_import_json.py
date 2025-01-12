#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to import Json file or load Json data."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict

from pyspartalib.context.file.json_context import Json, Single
from pyspartalib.script.file.json.export_json import json_export
from pyspartalib.script.file.json.import_json import json_import, json_load


def _common_test(expected: Single, key: str, value: str) -> None:
    result: Json = json_load('{"%s": %s}' % (key, value))

    assert isinstance(result, Dict)
    assert expected == result[key]


def _specify_pair(expected: Single, source: str) -> None:
    _common_test(expected, "group", source)


def test_none() -> None:
    """Test to load Json data as None data."""
    expected: None = None
    _specify_pair(expected, "null")


def test_bool() -> None:
    """Test to load Json data as type boolean."""
    expected: bool = True
    _specify_pair(expected, "true")


def test_integer() -> None:
    """Test to load Json data as type integer."""
    expected: int = 1
    _specify_pair(expected, str(expected))


def test_decimal() -> None:
    """Test to load Json data as type decimal."""
    expected: float = 0.1
    _specify_pair(expected, str(expected))


def test_string() -> None:
    """Test to load Json data as type string."""
    expected: str = "test"
    _specify_pair(expected, '"%s"' % expected)


def test_export() -> None:
    """Test to import Json file as format "json"."""
    expected: Json = [None, True, 1, "test"]

    with TemporaryDirectory() as temporary_path:
        assert expected == json_import(
            json_export(Path(temporary_path, "temporary.ini"), expected)
        )
