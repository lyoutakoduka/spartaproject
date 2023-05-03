#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from decimal import Decimal
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from scripts.files.import_file import text_import
from scripts.files.export_json import json_dump, json_export
from scripts.format_texts import format_indent


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

    expected: str = format_indent(EXPECTED)
    assert expected == json_dump(INPUT)


def test_extend() -> None:
    INPUT: Json = [Path('R'), Decimal('1.0')]
    EXPECTED: str = """
      [
        "R",
        1.0
      ]
    """

    expected: str = format_indent(EXPECTED)
    assert expected == json_dump(INPUT)


def test_tree() -> None:
    INPUT: Json = {'0': {'1': {'2': {'3': {'4': {'5': {'6': None}}}}}}}
    EXPECTED: str = """
    {
      "0": {
        "1": {
          "2": {
            "3": {
              "4": {
                "5": {
                  "6": null
                }
              }
            }
          }
        }
      }
    }
    """

    expected: str = format_indent(EXPECTED)
    assert expected == json_dump(INPUT)


def test_export() -> None:
    INPUT: Json = ['R', 'G', 'B']
    EXPECTED: str = """
      [
        "R",
        "G",
        "B"
      ]
    """

    expected: str = format_indent(EXPECTED)

    with TemporaryDirectory() as tmp_path:
        json_path: Path = Path(tmp_path, 'tmp.json')
        json_export(json_path, INPUT)
        assert expected == text_import(json_path)


def main() -> bool:
    test_default()
    test_extend()
    test_tree()
    test_export()
    return True
