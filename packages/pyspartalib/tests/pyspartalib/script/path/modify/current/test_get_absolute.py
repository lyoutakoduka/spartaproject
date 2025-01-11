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


def _confirm_sorted_paths(
    keys: Strs,
    expected: PathPair,
    result: PathPair,
) -> None:
    for key in keys:
        _difference_error(result[key], expected[key])


def _get_parents(path: Path) -> Paths:
    return [path.parents[i] for i in range(3)]


def _get_relative_paths(paths: Paths) -> Paths:
    return [get_relative(path) for path in paths]


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
    parents: Paths = _get_parents(_get_absolute_current())

    _difference_error(
        get_absolute_array(_get_relative_paths(parents)),
        parents,
    )


def test_pair() -> None:
    """Test to convert dictionary of relative paths to absolute."""
    keys: Strs = ["R", "G", "B"]
    parents: Paths = _get_parents(_get_absolute_current())

    _confirm_sorted_paths(
        keys,
        get_absolute_pair(_to_pair(keys, _get_relative_paths(parents))),
        _to_pair(keys, parents),
    )
