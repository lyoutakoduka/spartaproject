#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create temporary working space shared in class."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.directory.create_directory import (
    create_directory_pair,
)
from pyspartaproj.script.directory.work_space import WorkSpace
from pyspartaproj.script.path.modify.get_relative import is_relative
from pyspartaproj.script.time.path.get_time_path import get_initial_time_path


def _get_directory() -> Path:
    return Path("main", "sub")


def _create_sub_directory(temporary_root: Path, groups: Strs) -> PathPair:
    return create_directory_pair(
        {group: Path(temporary_root, group) for group in groups}
    )


def _create_sub_work(temporary_root: Path) -> PathPair:
    return _create_sub_directory(temporary_root, ["work"])


def _create_sub_select(temporary_root: Path) -> PathPair:
    return _create_sub_directory(temporary_root, ["work", "select"])


def _get_expected(group: str) -> Path:
    return Path(group, _get_directory())


def _check_exists(result: Path) -> None:
    assert result.exists()


def _relative_test(result: Path, root: Path) -> None:
    _check_exists(result)

    assert is_relative(result, root_path=root)


def _compare_root(temporary_root: Path, work_space: WorkSpace) -> None:
    _relative_test(work_space.get_working_root(), temporary_root)


def _compare_common(result: Path, expected: Path) -> None:
    assert result == expected


def _compare_base(temporary_root: Path, result: Path) -> None:
    _check_exists(result)
    _compare_common(result, Path(temporary_root, "work"))


def _compare_sub(temporary_root: Path, group: str, result: Path) -> None:
    _check_exists(result)
    _compare_common(result, Path(temporary_root, _get_expected(group)))


def _compare_date(
    temporary_root: Path, group: str, result: Path, expected: Path
) -> None:
    _compare_common(result, Path(temporary_root, group, expected))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def _get_work_space() -> WorkSpace:
    return WorkSpace()


def _get_work_space_root(working_root: Path) -> WorkSpace:
    return WorkSpace(working_root=working_root)


def _get_default_work_space(directory_pair: PathPair) -> WorkSpace:
    return _get_work_space_root(directory_pair["work"])


def test_path() -> None:
    """Test for path which is use Python default temporary working space."""
    work_space: WorkSpace = _get_work_space()
    working_root: Path = work_space.get_working_root()

    _check_exists(working_root)

    del work_space
    assert not working_root.exists()


def test_root() -> None:
    """Test for path of temporary working space you specified."""

    def individual_test(temporary_root: Path) -> None:
        _compare_root(temporary_root, _get_work_space_root(temporary_root))

    _inside_temporary_directory(individual_test)


def test_base() -> None:
    """Test to get path of temporary working space."""

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_base(temporary_root, work_space.get_selected_root())

    _inside_temporary_directory(individual_test)


def test_work() -> None:
    """Test for path of sub directory tree.

    It's placed to Python default temporary working space.
    """

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_sub(
            temporary_root,
            "work",
            work_space.create_sub_directory(_get_directory()),
        )

    _inside_temporary_directory(individual_test)


def test_select() -> None:
    """Test for path of sub directory tree.

    It's placed to temporary working space you specified.
    """

    def individual_test(temporary_root: Path) -> None:
        directory_pair: PathPair = _create_sub_select(temporary_root)
        work_space: WorkSpace = _get_default_work_space(directory_pair)

        _compare_sub(
            temporary_root,
            "select",
            work_space.create_sub_directory(
                _get_directory(), selected_root=directory_pair["select"]
            ),
        )

    _inside_temporary_directory(individual_test)


def test_date() -> None:
    """Test for path of temporary working space including date time string.

    It's placed to Python default temporary working space.
    """
    date_time_root: Path = get_initial_time_path()

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_date(
            temporary_root,
            "work",
            work_space.create_date_time_space(override=True),
            date_time_root,
        )

    _inside_temporary_directory(individual_test)


def test_body() -> None:
    """Test for path of temporary working space including date time string.

    It's placed to temporary working space you specified.
    """
    date_time_root: Path = get_initial_time_path()

    def individual_test(temporary_root: Path) -> None:
        directory_pair: PathPair = _create_sub_select(temporary_root)
        work_space: WorkSpace = _get_default_work_space(directory_pair)

        _compare_date(
            temporary_root,
            "select",
            work_space.create_date_time_space(
                body_root=directory_pair["select"], override=True
            ),
            date_time_root,
        )

    _inside_temporary_directory(individual_test)


def test_head() -> None:
    """Test for path of sub directory tree.

    Temporary working space including date time string is placed to here.
    """
    date_time_root: Path = get_initial_time_path()

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_date(
            temporary_root,
            "work",
            work_space.create_date_time_space(
                head_root=_get_directory(), override=True
            ),
            Path(_get_directory(), date_time_root),
        )

    _inside_temporary_directory(individual_test)


def test_foot() -> None:
    """Test for path of sub directory tree.

    It's placed to temporary working space including date time string.
    """
    date_time_root: Path = get_initial_time_path()

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_date(
            temporary_root,
            "work",
            work_space.create_date_time_space(
                foot_root=_get_directory(), override=True
            ),
            Path(date_time_root, _get_directory()),
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    """Test for path of temporary working space you specified.

    It's including date time string in JST time zone.
    """
    date_time_root: Path = get_initial_time_path(jst=True)

    def individual_test(temporary_root: Path) -> None:
        work_space: WorkSpace = _get_default_work_space(
            _create_sub_work(temporary_root)
        )

        _compare_date(
            temporary_root,
            "work",
            work_space.create_date_time_space(override=True, jst=True),
            date_time_root,
        )

    _inside_temporary_directory(individual_test)
