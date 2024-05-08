#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle paths about file and directory on server."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.server.local.path_server import PathServer


def _compare_relative(
    expected: Path, result: Path, server: PathServer
) -> None:
    assert expected == server.to_relative_path(result)


def _compare_path(result: Path, expected: Path) -> None:
    assert result.exists()
    assert result == expected


def _compare_working(
    temporary_root: Path, date_time: Path, server: PathServer
) -> None:
    _compare_path(
        server.get_working_root(),
        Path(
            temporary_root,
            "local",
            server.get_path("work_root"),
            date_time,
        ),
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_table() -> None:
    """Test to get keys of predefined all paths about server."""
    expected: int = 6
    server = PathServer()

    assert expected == len([path for path in server.get_path_table()])


def test_path() -> None:
    """Test to get all paths about server."""
    server = PathServer()

    for path in server.get_path_table():
        server.get_path(path)
        assert True


def test_local() -> None:
    """Test to get temporary working space for connecting server."""

    def individual_test(temporary_root: Path) -> None:
        server = PathServer(local_root=temporary_root)
        _compare_path(server.get_local_root(), Path(temporary_root, "local"))

    _inside_temporary_directory(individual_test)


def test_temporary() -> None:
    """Test to get local temporary working space for connecting server."""
    date_time: Path = Path("2023", "04", "01", "00", "00", "00", "000000")

    def individual_test(temporary_root: Path) -> None:
        server = PathServer(local_root=temporary_root, override=True)
        _compare_working(temporary_root, date_time, server)

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    date_time: Path = Path("2023", "04", "01", "09", "00", "00", "000000")

    def individual_test(temporary_root: Path) -> None:
        server = PathServer(local_root=temporary_root, override=True, jst=True)
        _compare_working(temporary_root, date_time, server)

    _inside_temporary_directory(individual_test)


def test_relative() -> None:
    """Test to convert full path to relative path.

    The full path of directory is based on local temporary working space.
    """
    expected: Path = Path("temp")
    server = PathServer()

    _compare_relative(
        expected, Path(server.get_local_root(), expected), server
    )


def test_full() -> None:
    """Test to convert relative path to full path.

    The full path of directory is based on local temporary working space.
    """
    expected: Path = Path("temp")
    server = PathServer()

    _compare_relative(expected, server.to_full_path(expected), server)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_table()
    test_path()
    test_local()
    test_temporary()
    test_jst()
    test_relative()
    test_full()
    return True
