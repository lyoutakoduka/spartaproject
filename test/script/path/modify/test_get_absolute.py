#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair, Paths
from pyspartaproj.script.bool.same_value import bool_same_array
from pyspartaproj.script.path.modify.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartaproj.script.path.modify.get_current import get_current
from pyspartaproj.script.path.modify.get_relative import get_relative


def _get_absolute_current() -> Path:
    return Path(__file__)


def to_relative(path: Path) -> Path:
    current: Path = get_current()
    path_text: str = path.as_posix()
    index: int = len(current.as_posix()) + 1
    return Path(path_text[index:])


def to_pair(keys: Strs, paths: Paths) -> PathPair:
    return {key: path for key, path in zip(keys, paths)}


def test_ignore() -> None:
    expected: Path = _get_absolute_current()
    assert expected == get_absolute(expected)


def test_single() -> None:
    expected: Path = _get_absolute_current()
    assert expected == get_absolute(get_relative(expected))


def test_root() -> None:
    expected: Path = _get_absolute_current()

    assert expected == get_absolute(
        Path(expected.name), root_path=expected.parent
    )


def test_array() -> None:
    expected_base: Path = _get_absolute_current()
    expected: Paths = [expected_base.parents[i] for i in range(3)]

    assert expected == get_absolute_array(
        [get_relative(path) for path in expected]
    )


def test_pair() -> None:
    expected_base: Path = _get_absolute_current()
    keys: Strs = ["R", "G", "B"]
    parents: Paths = [expected_base.parents[i] for i in range(3)]

    expected: PathPair = to_pair(keys, parents)
    result: PathPair = get_absolute_pair(
        to_pair(keys, [get_relative(path) for path in parents])
    )

    assert bool_same_array([expected[key] == result[key] for key in keys])


def main() -> bool:
    test_ignore()
    test_single()
    test_root()
    test_array()
    test_pair()
    return True
