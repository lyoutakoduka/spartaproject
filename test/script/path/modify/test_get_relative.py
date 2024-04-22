#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert absolute path to relative."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.interface.pytest import raises
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.path.modify.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartaproj.script.path.modify.get_relative import (
    get_relative,
    get_relative_array,
    get_relative_pair,
)


def _get_current_file() -> Path:
    return Path(__file__)


def _to_pair(path_types: Strs, paths: Paths) -> PathPair:
    return {path_type: path for path_type, path in zip(path_types, paths)}


def test_unmatch() -> None:
    """Test to convert absolute path, but using invalid path."""
    with raises(ValueError):
        get_relative(Path("empty"))


def test_single() -> None:
    """Test to convert absolute path by using specific root path."""
    expected: Path = _get_current_file()
    assert expected == get_absolute(get_relative(expected))


def test_root() -> None:
    """Test to convert absolute path with specific root."""
    expected_base: Path = _get_current_file()

    assert Path(expected_base.name) == get_relative(
        expected_base, root_path=expected_base.parent
    )


def test_array() -> None:
    """Test to convert list of absolute paths to relative."""
    expected_base: Path = _get_current_file()
    expected: Paths = [expected_base.parents[i] for i in range(3)]

    assert expected == get_absolute_array(get_relative_array(expected))


def test_pair() -> None:
    """Test to convert dictionary of absolute paths to relative."""
    expected_base: Path = _get_current_file()
    keys: Strs = ["R", "G", "B"]

    expected: PathPair = _to_pair(
        keys, [expected_base.parents[i] for i in range(3)]
    )
    result: PathPair = get_absolute_pair(get_relative_pair(expected))

    assert bool_same_array([expected[key] == result[key] for key in keys])


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_unmatch()
    test_single()
    test_root()
    test_array()
    test_pair()
    return True
