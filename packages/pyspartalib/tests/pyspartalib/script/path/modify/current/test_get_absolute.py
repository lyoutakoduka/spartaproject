#!/usr/bin/env python

"""Test module to convert relative path to absolute."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.frame.current_frame import CurrentFrame
from pyspartalib.script.path.modify.current.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
    is_absolute,
)
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    get_relative_array,
    get_relative_pair,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


class _Share:
    def _get_three_parents(self, path: Path) -> Paths:
        return [path.parents[i] for i in range(3)]

    def get_relative_paths(self, paths: Paths) -> Paths:
        return [get_relative(path) for path in paths]

    def get_relative_current(self) -> Path:
        return CurrentFrame().get_frame()["file"]

    def get_relative_parents(self) -> Paths:
        return self._get_three_parents(self.get_relative_current())


class TestIs(_Share):
    """Class to verify the input path is an absolute path."""

    def test_is(self) -> None:
        """Test to verify the input path is an absolute path."""
        expected: Path = self.get_relative_current()
        _fail_error(is_absolute(expected, root_path=expected.parent))


class TestIgnore(_Share):
    """Class to convert absolute path to absolute."""

    def test_ignore(self) -> None:
        """Test to convert absolute path to absolute."""
        expected: Path = self.get_relative_current()

        _difference_error(
            get_absolute(expected, root_path=expected.parent),
            expected,
        )


class TestSingle(_Share):
    """Class to convert relative path to absolute."""

    def test_single(self) -> None:
        """Test to convert relative path to absolute."""
        expected: Path = self.get_relative_current()
        _difference_error(get_relative(get_absolute(expected)), expected)


class TestRoot(_Share):
    """Class to convert relative path by using specific root path."""

    def test_root(self) -> None:
        """Test to convert relative path by using specific root path."""
        expected: Path = self.get_relative_current()

        _difference_error(
            get_absolute(Path(expected.name), root_path=expected.parent),
            expected,
        )


class TestArray(_Share):
    """Class to convert list of relative paths to absolute."""

    def test_array(self) -> None:
        """Test to convert list of relative paths to absolute."""
        parents: Paths = self.get_relative_parents()

        _difference_error(
            get_relative_array(get_absolute_array(parents)),
            parents,
        )


class TestPair(_Share):
    """Class to convert dictionary of relative paths to absolute."""

    def _get_keys(self) -> Strs:
        return ["R", "G", "B"]

    def _to_pair(self, paths: Paths) -> PathPair:
        return dict(zip(self._get_keys(), paths, strict=True))

    def _confirm_sorted_paths(
        self,
        expected: PathPair,
        result: PathPair,
    ) -> None:
        for key in self._get_keys():
            _difference_error(result[key], expected[key])

    def test_pair(self) -> None:
        """Test to convert dictionary of relative paths to absolute."""
        parents: Paths = self.get_relative_parents()

        self._confirm_sorted_paths(
            get_relative_pair(get_absolute_pair(self._to_pair(parents))),
            self._to_pair(parents),
        )
