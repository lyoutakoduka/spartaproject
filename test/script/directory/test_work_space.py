#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working space shared in class."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.work_space import WorkSpace
from pyspartaproj.script.path.modify.get_relative import is_relative


def _relative_test(path: Path, root: Path) -> None:
    assert path.exists()
    assert is_relative(path, root_path=root)


def _compare_path(temporary_root: Path, work_space: WorkSpace) -> None:
    _relative_test(work_space.get_working_root(), temporary_root)


def _compare_directory(work_space: WorkSpace) -> None:
    _relative_test(
        work_space.create_sub_directory("test"), work_space.get_working_root()
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_path() -> None:
    """Test to check path of temporary working space you specified."""

    def individual_test(temporary_root: Path) -> None:
        _compare_path(temporary_root, WorkSpace(working_root=temporary_root))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to check path of sub directory in temporary working space."""

    def individual_test(temporary_root: Path) -> None:
        _compare_directory(WorkSpace(working_root=temporary_root))

    _inside_temporary_directory(individual_test)


def test_working() -> None:
    expected: Path = Path(
        "test", "2023", "04", "01", "00", "00", "00", "000000"
    )

    def individual_test(temporary_root: Path) -> None:
        work_space = WorkSpace()
        temporary_path: Path = work_space.create_date_time_space(
            "test", override=True
        )

        assert temporary_path.exists()
        assert temporary_path == Path(work_space.get_working_root(), expected)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_path()
    test_directory()
    test_working()
    return True
