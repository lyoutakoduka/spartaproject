#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle paths about file and directory on server."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.server.local.path_server import PathServer


def _compare_path(result: Path, expected: Path) -> None:
    assert result.exists()
    assert result == expected


def _compare_local(temporary_root: Path, result: Path) -> None:
    _compare_path(result, Path(temporary_root, "local"))


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
    """Test to get temporary working space used when connecting server."""

    def individual_test(temporary_root: Path) -> None:
        server = PathServer(local_root=temporary_root)
        _compare_local(temporary_root, server.get_local_root())

    _inside_temporary_directory(individual_test)


def test_relative() -> None:
    """Test to convert full path to relative path.

    The full path of directory is based on local temporary working space.
    """
    expected: Path = Path("temp")
    server = PathServer()

    assert expected == server.to_relative_path(
        Path(server.get_local_root(), expected)
    )


def test_full() -> None:
    """Test to convert relative path to full path.

    The full path of directory is based on local temporary working space.
    """
    expected: Path = Path("temp")
    server = PathServer()

    assert expected == server.to_relative_path(server.to_full_path(expected))


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_table()
    test_path()
    test_local()
    test_relative()
    test_full()
    return True
