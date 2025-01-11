#!/usr/bin/env python

"""Test module to convert relative path to absolute."""

from pathlib import Path

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.context.type_context import Type
from pyspartalib.script.path.modify.current.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartalib.script.path.modify.current.get_relative import get_relative


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_absolute_current() -> Path:
    return Path(__file__)


def _to_pair(keys: Strs, paths: Paths) -> PathPair:
    return dict(zip(keys, paths, strict=True))


def test_ignore() -> None:
    """Test to convert absolute path to absolute."""
    expected: Path = _get_absolute_current()
    _difference_error(get_absolute(expected), expected)


def test_single() -> None:
    """Test to convert relative path to absolute."""
    expected: Path = _get_absolute_current()
    _difference_error(get_absolute(get_relative(expected)), expected)


def test_root() -> None:
    """Test to convert relative path by using specific root path."""
    expected: Path = _get_absolute_current()

    _difference_error(
        get_absolute(Path(expected.name), root_path=expected.parent),
        expected,
    )


def test_array() -> None:
    """Test to convert list of relative paths to absolute."""
    expected_base: Path = _get_absolute_current()
    expected: Paths = [expected_base.parents[i] for i in range(3)]

    _difference_error(
        get_absolute_array(
            [get_relative(path) for path in expected],
        ),
        expected,
    )


def test_pair() -> None:
    """Test to convert dictionary of relative paths to absolute."""
    expected_base: Path = _get_absolute_current()
    keys: Strs = ["R", "G", "B"]
    parents: Paths = [expected_base.parents[i] for i in range(3)]

    expected: PathPair = _to_pair(keys, parents)
    result: PathPair = get_absolute_pair(
        _to_pair(keys, [get_relative(path) for path in parents]),
    )

    for key in keys:
        _difference_error(result[key], expected[key])
