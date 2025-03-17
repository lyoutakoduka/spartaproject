#!/usr/bin/env python

"""Test module to convert absolute path to relative."""

from pathlib import Path

import pytest
from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.bool_context import Bools
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.bool.compare_value import bool_compare_array
from pyspartalib.script.frame.stack_frame import current_frame
from pyspartalib.script.path.modify.current.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    get_relative_array,
    get_relative_pair,
    is_relative,
    is_relative_array,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_error() -> Path:
    return Path("error")


def _get_current_file() -> Path:
    return Path(__file__)


def _get_absolute_current() -> Path:
    return get_absolute(current_frame()["file"])


def _get_expected() -> Bools:
    return [True, False]


def _get_paths(current: Path) -> Paths:
    return [current, _get_error()]


def _to_pair(path_types: Strs, paths: Paths) -> PathPair:
    return dict(zip(path_types, paths, strict=True))


def _confirm_sorted_paths(
    keys: Strs,
    expected: PathPair,
    result: PathPair,
) -> None:
    for key in keys:
        _difference_error(result[key], expected[key])


def _get_parents(path: Path) -> Paths:
    return [path.parents[i] for i in range(3)]


def _re_implement(paths: Paths, root_path: Path | None) -> Bools:
    return [is_relative(path, root_path=root_path) for path in paths]


def test_check() -> None:
    """Test to check path which is type relative."""
    current: Path = _get_current_file()

    _fail_error(
        bool_compare_array(
            _get_expected(),
            _re_implement(_get_paths(current), current.parent),
        ),
    )


def test_check_array() -> None:
    """Test to check that list of paths are type relative at once."""
    current: Path = _get_current_file()

    _fail_error(
        bool_compare_array(
            _get_expected(),
            is_relative_array(_get_paths(current), root_path=current.parent),
        ),
    )


def test_unmatch() -> None:
    """Test to convert absolute path, but using invalid path."""
    with pytest.raises(ValueError, match="relative"):
        get_relative(_get_error())


def test_single() -> None:
    """Test to convert absolute path by using specific root path."""
    expected: Path = _get_current_file()
    _difference_error(get_absolute(get_relative(expected)), expected)


def test_root() -> None:
    """Test to convert absolute path with specific root."""
    expected_base: Path = _get_current_file()

    _difference_error(
        get_relative(expected_base, root_path=expected_base.parent),
        Path(expected_base.name),
    )


def test_array() -> None:
    """Test to convert list of absolute paths to relative."""
    expected: Paths = _get_parents(_get_current_file())

    _difference_error(
        get_absolute_array(get_relative_array(expected)),
        expected,
    )


def test_pair() -> None:
    """Test to convert dictionary of absolute paths to relative."""
    keys: Strs = ["R", "G", "B"]
    expected: PathPair = _to_pair(keys, _get_parents(_get_current_file()))

    _confirm_sorted_paths(
        keys,
        get_absolute_pair(get_relative_pair(expected)),
        expected,
    )
