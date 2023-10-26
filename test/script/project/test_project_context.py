#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to import a context of whole project from outside Json."""

from pathlib import Path
from platform import uname

from pyspartaproj.context.default.integer_context import IntPair
from pyspartaproj.context.default.string_context import StrPair, Strs, Strs2
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.project.project_context import ProjectContext


def _common_test(keys_pair: Strs2) -> None:
    assert 1 == len(set([str(sorted(keys)) for keys in keys_pair]))


def _import_context() -> ProjectContext:
    return ProjectContext(forward=get_resource(["forward.json"]))


def test_integer() -> None:
    """Test to filter and get project context by integer type."""
    expected: IntPair = {"index": 0, "count": 1}

    project: ProjectContext = _import_context()
    integer_context: IntPair = project.get_integer_context("type")

    _common_test([list(items.keys()) for items in [expected, integer_context]])

    for key, value in expected.items():
        assert value == integer_context[key]


def test_string() -> None:
    """Test to filter and get project context by string type."""
    expected: StrPair = {"name": "name", "language": "language"}

    project: ProjectContext = _import_context()
    string_context: StrPair = project.get_string_context("type")

    _common_test([list(items.keys()) for items in [expected, string_context]])

    for key, value in expected.items():
        assert value == string_context[key]


def test_path() -> None:
    """Test to filter and get project context by path type."""
    expected: PathPair = {
        "root.path": Path("root"),
        "head.path": Path("root", "head"),
    }

    project: ProjectContext = _import_context()
    path_context: PathPair = project.get_path_context("type")

    _common_test([list(items.keys()) for items in [expected, path_context]])

    for key, value in expected.items():
        assert value == path_context[key]


def test_key() -> None:
    expected: Strs = ["group", "type"]
    context_key: str = _import_context().get_platform_key(expected)
    key_elements: Strs = context_key.split("_")

    assert expected == key_elements[:2]
    assert uname().system == key_elements[-1].capitalize()


def test_merge() -> None:
    expected: Strs = ["directory", "file"]
    project: ProjectContext = _import_context()

    assert Path(*expected) == project.merge_platform_path(
        "platform", *expected
    )


def main() -> bool:
    """Run all tests.

    Returns:
        bool: success if get to the end of function
    """
    test_integer()
    test_string()
    test_path()
    test_key()
    test_merge()
    return True
