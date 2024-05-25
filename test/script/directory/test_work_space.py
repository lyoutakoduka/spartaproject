#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working space shared in class."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.work_space import WorkSpace
from pyspartaproj.script.path.modify.get_relative import is_relative


def _get_directory() -> Path:
    return Path("main", "sub")


def _check_exists(result: Path) -> None:
    assert result.exists()


def _relative_test(result: Path, root: Path) -> None:
    _check_exists(result)

    assert is_relative(result, root_path=root)


def _compare_root(temporary_root: Path, work_space: WorkSpace) -> None:
    _relative_test(work_space.get_working_root(), temporary_root)


def _compare_directory(work_space: WorkSpace) -> None:
    _relative_test(
        work_space.create_sub_directory(_get_directory()),
        work_space.get_working_root(),
    )


def _compare_working(
    result: Path, expected: Path, work_space: WorkSpace
) -> None:
    _check_exists(result)

    assert result == Path(
        work_space.get_working_root(), Path(_get_directory(), expected)
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_work_space() -> WorkSpace:
    return WorkSpace()


def _get_work_space_root(working_root: Path) -> WorkSpace:
    return WorkSpace(working_root=working_root)


def test_path() -> None:
    """Test to check path of temporary working space you specified."""
    work_space: WorkSpace = _get_work_space()
    working_root: Path = work_space.get_working_root()

    _check_exists(working_root)

    del work_space
    assert not working_root.exists()


def test_root() -> None:
    def individual_test(temporary_root: Path) -> None:
        _compare_root(temporary_root, _get_work_space_root(temporary_root))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to check path of sub directory in temporary working space."""

    def individual_test(temporary_root: Path) -> None:
        _compare_directory(_get_work_space_root(temporary_root))

    _inside_temporary_directory(individual_test)


def test_working() -> None:
    """Test to compare path of temporary working space in sub directory.

    Path include date time string in UTC time zone.
    """
    expected: Path = Path("2023", "04", "01", "00", "00", "00", "000000")

    work_space: WorkSpace = _get_work_space()
    temporary_path: Path = work_space.create_date_time_space(
        _get_directory(), override=True
    )

    _compare_working(temporary_path, expected, work_space)


def test_jst() -> None:
    """Test to compare path of temporary working space in sub directory.

    Path include date time string in JST time zone.
    """
    expected: Path = Path("2023", "04", "01", "09", "00", "00", "000000")

    work_space: WorkSpace = _get_work_space()
    temporary_path: Path = work_space.create_date_time_space(
        _get_directory(), override=True, jst=True
    )

    _compare_working(temporary_path, expected, work_space)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_path()
    test_root()
    test_directory()
    test_working()
    test_jst()
    return True
