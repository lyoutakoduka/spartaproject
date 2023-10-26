#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.file.json.convert_from_json import (
    string_pair_from_json,
)
from pyspartaproj.script.file.json.import_json import json_import
from pyspartaproj.script.path.modify.get_resource import get_resource


def _common_test(expected: str, path_elements: Strs) -> None:
    result_path: Path = get_resource(path_elements)
    assert expected == string_pair_from_json(json_import(result_path))["name"]


def test_file() -> None:
    expected: str = "file"
    _common_test(expected, [expected + ".json"])


def main() -> bool:
    test_file()
    return True
