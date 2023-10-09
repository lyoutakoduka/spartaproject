#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.file.json.export_json import json_dump, json_export
from pyspartaproj.script.file.text.import_file import text_import
from pyspartaproj.script.string.format_texts import format_indent


def _common_test(expected: str, source: Json) -> None:
    assert format_indent(expected) == json_dump(source)


def test_type() -> None:
    source: Json = {
        "None": None,
        "bool": True,
        "int": 1,
        "float": 1.0,
        "str": "1",
    }

    # 2 space indent
    expected: str = """
      {
        "None": null,
        "bool": true,
        "float": 1.0,
        "int": 1,
        "str": "1"
      }
    """

    _common_test(expected, source)


def test_tree() -> None:
    source: Json = {"0": {"1": {"2": {"3": {"4": {"5": {"6": None}}}}}}}
    expected: str = """
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

    _common_test(expected, source)


def test_compress() -> None:
    source: Json = {"0": {"1": {"2": {"3": {"4": {"5": {"6": None}}}}}}}
    expected: str = """{"0":{"1":{"2":{"3":{"4":{"5":{"6":null}}}}}}}"""
    assert expected == json_dump(source, compress=True)


def test_export() -> None:
    keys: Json = ["R", "G", "B"]
    expected: str = """
      [
        "R",
        "G",
        "B"
      ]
    """

    expected: str = format_indent(expected)

    with TemporaryDirectory() as temporary_path:
        assert expected == text_import(
            json_export(Path(temporary_path, "temporary.json"), keys)
        )


def main() -> bool:
    test_type()
    test_tree()
    test_compress()
    test_export()
    return True
