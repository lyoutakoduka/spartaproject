#!/usr/bin/env python

"""Test module to export data used for json format."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.file.json_context import Json
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.json.export_json import json_dump, json_export
from pyspartalib.script.file.text.import_file import text_import
from pyspartalib.script.string.format_texts import format_indent


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected_type() -> str:
    return """
      {
        "None": null,
        "bool": true,
        "float": 1.0,
        "int": 1,
        "str": "1"
      }
    """  # 2 space indent


def _get_expected_nest() -> str:
    return """
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


def _get_expected_compress() -> str:
    return """{"0":{"1":{"2":{"3":{"4":{"5":{"6":null}}}}}}}"""


def _get_expected_export() -> str:
    return """
      [
        "R",
        "G",
        "B"
      ]
    """


def _get_source_type() -> Json:
    return {
        "None": None,
        "bool": True,
        "int": 1,
        "float": 1.0,
        "str": "1",
    }


def _get_source_nested() -> Json:
    return {"0": {"1": {"2": {"3": {"4": {"5": {"6": None}}}}}}}


def _get_source_export() -> Json:
    return ["R", "G", "B"]


def _common_test(expected: str, source: Json) -> None:
    _difference_error(json_dump(source), format_indent(expected))


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_type() -> None:
    """Test to convert data used for json format to text.

    Data is a dictionary created with multiple mixed type.
    """
    _common_test(_get_expected_type(), _get_source_type())


def test_tree() -> None:
    """Test to convert data used for json format to text.

    Data is multiple dimensional dictionary created with None object.
    """
    _common_test(_get_expected_nest(), _get_source_nested())


def test_compress() -> None:
    """Test to convert data used for json format with compress option."""
    _difference_error(
        json_dump(_get_source_nested(), compress=True),
        _get_expected_compress(),
    )


def test_export() -> None:
    """Test to export data used for json format."""

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            text_import(
                json_export(
                    Path(temporary_root, "temporary.json"),
                    _get_source_export(),
                ),
            ),
            format_indent(_get_expected_export()),
        )

    _inside_temporary_directory(individual_test)
