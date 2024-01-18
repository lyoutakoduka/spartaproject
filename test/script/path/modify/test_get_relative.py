#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def to_pair(path_types: Strs, paths: Paths) -> PathPair:
    return {path_type: path for path_type, path in zip(path_types, paths)}


def test_unmatch() -> None:
    with raises(ValueError):
        get_relative(Path("empty"))


def test_single() -> None:
    expected: Path = Path(__file__)
    assert expected == get_absolute(get_relative(expected))


def test_root() -> None:
    current: Path = Path(__file__)

    assert Path(current.name) == get_relative(
        current, root_path=current.parent
    )


def test_array() -> None:
    current: Path = Path(__file__)
    expected: Paths = [current.parents[i] for i in range(3)]

    assert expected == get_absolute_array(get_relative_array(expected))


def test_pair() -> None:
    current: Path = Path(__file__)
    keys: Strs = ["R", "G", "B"]

    expected: PathPair = to_pair(keys, [current.parents[i] for i in range(3)])
    result: PathPair = get_absolute_pair(get_relative_pair(expected))

    assert bool_same_array([expected[key] == result[key] for key in keys])


def main() -> bool:
    test_single()
    test_root()
    test_array()
    test_pair()
    test_unmatch()
    return True
