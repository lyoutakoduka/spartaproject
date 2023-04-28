#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryDirectory

from contexts.path_context import Path
from contexts.json_context import TypeJson
from scripts.files.export_json import json_dump, json_export
from scripts.format_texts import format_indent


_JSON_INPUT: TypeJson = {
    'str': '1',
    'float': 1.0,
    'int': 1,
    'bool': True,
    'None': None,
}

# 2 space indent
_EXPECTED_SRC: str = """
  {
    "None": null,
    "bool": true,
    "float": 1.0,
    "int": 1,
    "str": "1"
  }
"""


def test_dump() -> None:
    EXPECTED: str = format_indent(_EXPECTED_SRC)
    assert EXPECTED == json_dump(_JSON_INPUT)


def test_export() -> None:
    EXPECTED: str = format_indent(_EXPECTED_SRC)

    with TemporaryDirectory() as tmp_path:
        export_path: Path = Path(tmp_path, 'tmp.json')
        json_export(export_path, _JSON_INPUT)

        with open(export_path, 'r') as file:
            assert EXPECTED == file.read()


def main() -> bool:
    test_dump()
    test_export()
    return True
