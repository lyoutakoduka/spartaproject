#!/usr/bin/env python

"""Test module to convert relative path to absolute."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.frame.stack_frame import current_frame
from pyspartalib.script.path.modify.current.get_absolute import (
    get_absolute,
    get_absolute_array,
    get_absolute_pair,
)
from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    get_relative_array,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


class _Share:
    def get_absolute_current(self) -> Path:
        return get_absolute(self.get_relative_current())

    def get_parents(self, path: Path) -> Paths:
        return [path.parents[i] for i in range(3)]

    def get_relative_paths(self, paths: Paths) -> Paths:
        return [get_relative(path) for path in paths]

    def get_relative_current(self) -> Path:
        return current_frame()["file"]


class TestIgnore(_Share):
    def test_ignore(self) -> None:
        """Test to convert absolute path to absolute."""
        expected: Path = self.get_absolute_current()
        _difference_error(get_absolute(expected), expected)


class TestSingle(_Share):
    def test_single(self) -> None:
        """Test to convert relative path to absolute."""
        expected: Path = self.get_relative_current()
        _difference_error(get_relative(get_absolute(expected)), expected)


class TestRoot(_Share):
    def test_root(self) -> None:
        """Test to convert relative path by using specific root path."""
        expected: Path = self.get_relative_current()

        _difference_error(
            get_absolute(Path(expected.name), root_path=expected.parent),
            expected,
        )


class TestArray(_Share):
    def test_array(self) -> None:
        """Test to convert list of relative paths to absolute."""
        parents: Paths = self.get_parents(self.get_relative_current())

        _difference_error(
            get_relative_array(get_absolute_array(parents)),
            parents,
        )


class TestPair(_Share):
    def _to_pair(self, keys: Strs, paths: Paths) -> PathPair:
        return dict(zip(keys, paths, strict=True))

    def _confirm_sorted_paths(
        self,
        keys: Strs,
        expected: PathPair,
        result: PathPair,
    ) -> None:
        for key in keys:
            _difference_error(result[key], expected[key])

    def test_pair(self) -> None:
        """Test to convert dictionary of relative paths to absolute."""
        keys: Strs = ["R", "G", "B"]
        parents: Paths = self.get_parents(self.get_absolute_current())

        self._confirm_sorted_paths(
            keys,
            get_absolute_pair(
                self._to_pair(keys, self.get_relative_paths(parents)),
            ),
            self._to_pair(keys, parents),
        )
