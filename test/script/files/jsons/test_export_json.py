#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory

from context.json_context import Json
from script.files.import_file import text_import
from script.files.jsons.export_json import json_dump, json_export
from script.format_texts import format_indent


def _common_test(expected: str, input: Json) -> None:
    assert format_indent(expected) == json_dump(input)


def test_type() -> None:
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

    _common_test(EXPECTED, INPUT)


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

    _common_test(EXPECTED, INPUT)


def test_compress() -> None:
    INPUT: Json = {'0': {'1': {'2': {'3': {'4': {'5': {'6': None}}}}}}}
    EXPECTED: str = '''{"0":{"1":{"2":{"3":{"4":{"5":{"6":null}}}}}}}'''
    assert EXPECTED == json_dump(INPUT, compress=True)


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

    with TemporaryDirectory() as temporary_path:
        assert expected == text_import(
            json_export(Path(temporary_path, 'temporary.json'), INPUT)
        )


def main() -> bool:
    test_type()
    test_tree()
    test_compress()
    test_export()
    return True
