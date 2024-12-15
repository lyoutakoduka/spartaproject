#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert relative path to absolute."""


from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.bool.same_value import bool_same_array
from pyspartalib.script.path.modify.current.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative


def _get_absolute_current() -> Path:
    return Path(__file__)


def _to_pair(keys: Strs, paths: Paths) -> PathPair:
    return {key: path for key, path in zip(keys, paths)}


def test_ignore() -> None:
    """Test to convert absolute path to absolute."""
    expected: Path = _get_absolute_current()
    assert expected == get_absolute(expected)


def test_single() -> None:
    """Test to convert relative path to absolute."""
    expected: Path = _get_absolute_current()
    assert expected == get_absolute(get_relative(expected))


def test_root() -> None:
    """Test to convert relative path by using specific root path."""
    expected: Path = _get_absolute_current()

    assert expected == get_absolute(
        Path(expected.name), root_path=expected.parent
    )


def test_array() -> None:
    """Test to convert list of relative paths to absolute."""
    expected_base: Path = _get_absolute_current()
    expected: Paths = [expected_base.parents[i] for i in range(3)]

    assert expected == get_absolute_array(
        [get_relative(path) for path in expected]
    )


def test_pair() -> None:
    """Test to convert dictionary of relative paths to absolute."""
    expected_base: Path = _get_absolute_current()
    keys: Strs = ["R", "G", "B"]
    parents: Paths = [expected_base.parents[i] for i in range(3)]

    expected: PathPair = _to_pair(keys, parents)
    result: PathPair = get_absolute_pair(
        _to_pair(keys, [get_relative(path) for path in parents])
    )

    assert bool_same_array([expected[key] == result[key] for key in keys])
