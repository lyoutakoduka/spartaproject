#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import StrPair, Strs2
from pyspartaproj.script.file.json.project_context import ProjectContext


def _common_test(keys_pair: Strs2) -> None:
    assert 1 == len(set([str(sorted(keys)) for keys in keys_pair]))


def test_integer() -> None:
    expected: IntPair = {"index": 0, "count": 1}

    project = ProjectContext(
        forward=Path(Path(__file__).parent, "resource", "forward.json")
    )
    integer_context: IntPair = project.get_integer_context("test")

    _common_test([list(items.keys()) for items in [expected, integer_context]])

    for key, value in expected.items():
        assert value == integer_context[key]


def test_string() -> None:
    expected: StrPair = {"name": "name", "language": "language"}

    project = ProjectContext(
        forward=Path(Path(__file__).parent, "resource", "forward.json")
    )
    string_context: StrPair = project.get_string_context("test")

    _common_test([list(items.keys()) for items in [expected, string_context]])

    for key, value in expected.items():
        assert value == string_context[key]


def main() -> bool:
    test_integer()
    test_string()
    return True
