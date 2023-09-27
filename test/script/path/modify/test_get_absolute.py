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


def to_relative(path: Path) -> Path:
    current: Path = Path.cwd()
    path_text: str = path.as_posix()
    return Path(path_text[len(current.as_posix()) + 1 :])


def to_pair(types: Strs, paths: Paths) -> PathPair:
    return {type: path for type, path in zip(types, paths)}


def test_ignore() -> None:
    path: Path = Path(__file__)
    assert path == get_absolute(path)


def test_single() -> None:
    expected: Path = Path(__file__)
    assert expected == get_absolute(to_relative(expected))


def test_root() -> None:
    expected: Path = Path(__file__)

    assert expected == get_absolute(
        Path(expected.name), root_path=expected.parent
    )


def test_array() -> None:
    current: Path = Path(__file__)
    expected: Paths = [current.parents[i] for i in range(3)]

    assert expected == get_absolute_array(
        [to_relative(path) for path in expected]
    )


def test_pair() -> None:
    current: Path = Path(__file__)
    types: Strs = ["R", "G", "B"]
    parents: Paths = [current.parents[i] for i in range(3)]

    expected: PathPair = to_pair(types, parents)
    result: PathPair = get_absolute_pair(
        to_pair(types, [to_relative(path) for path in parents])
    )

    assert bool_same_array([expected[type] == result[type] for type in types])


def main() -> bool:
    test_ignore()
    test_single()
    test_root()
    test_array()
    test_pair()
    return True
