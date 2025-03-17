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


class _Share:
    def get_error(self) -> Path:
        return Path("error")

    def get_paths(self, current: Path) -> Paths:
        return [current, self.get_error()]

    def get_expected(self) -> Bools:
        return [True, False]

    def get_parents(self, path: Path) -> Paths:
        return [path.parents[i] for i in range(3)]

    def get_absolute_current(self) -> Path:
        return get_absolute(current_frame()["file"])


def _re_implement(paths: Paths, root_path: Path | None) -> Bools:
    return [is_relative(path, root_path=root_path) for path in paths]


def test_check() -> None:
    """Test to check path which is type relative."""
    current: Path = _get_absolute_current()

    _fail_error(
        bool_compare_array(
            _get_expected(),
            _re_implement(_get_paths(current), current.parent),
        ),
    )


def test_check_array() -> None:
    """Test to check that list of paths are type relative at once."""
    current: Path = _get_absolute_current()

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


class TestSingle(_Share):
    def test_single(self) -> None:
        """Test to convert absolute path by using specific root path."""
        expected: Path = self.get_absolute_current()

        _difference_error(get_absolute(get_relative(expected)), expected)


class TestRoot(_Share):
    def test_root(self) -> None:
        """Test to convert absolute path with specific root."""
        expected_base: Path = self.get_absolute_current()

        _difference_error(
            get_relative(expected_base, root_path=expected_base.parent),
            Path(expected_base.name),
        )


class TestArray(_Share):
    def test_array(self) -> None:
        """Test to convert list of absolute paths to relative."""
        expected: Paths = self.get_parents(self.get_absolute_current())

        _difference_error(
            get_absolute_array(get_relative_array(expected)),
            expected,
        )


class TestPair(_Share):
    def _to_pair(self, path_types: Strs, paths: Paths) -> PathPair:
        return dict(zip(path_types, paths, strict=True))

    def _confirm_sorted_paths(
        self,
        keys: Strs,
        expected: PathPair,
        result: PathPair,
    ) -> None:
        for key in keys:
            _difference_error(result[key], expected[key])

    def test_pair(self) -> None:
        """Test to convert dictionary of absolute paths to relative."""
        keys: Strs = ["R", "G", "B"]
        expected: PathPair = self._to_pair(
            keys,
            self.get_parents(self.get_absolute_current()),
        )

        self._confirm_sorted_paths(
            keys,
            get_absolute_pair(get_relative_pair(expected)),
            expected,
        )
