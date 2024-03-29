#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle paths about file and directory on server."""

from pathlib import Path
from typing import Callable

from pyspartaproj.script.server.local.path_server import PathServer


def _common_test(function: Callable[[PathServer], None]) -> None:
    function(PathServer())


def test_table() -> None:
    """Test to get keys of predefined all paths about server."""
    expected: int = 6

    def individual_test(server: PathServer) -> None:
        assert expected == len([path for path in server.get_path_table()])

    _common_test(individual_test)


def test_path() -> None:
    """Test to get all paths about server."""

    def individual_test(server: PathServer) -> None:
        for path in server.get_path_table():
            server.get_path(path)
            assert True

    _common_test(individual_test)


def test_relative() -> None:
    """Test to convert full path to relative path.

    The full path is based on Python default temporary directory.
    """
    expected: Path = Path("temp")

    def individual_test(server: PathServer) -> None:
        assert expected == server.to_relative_path(
            Path(server.get_root(), expected)
        )

    _common_test(individual_test)


def test_full() -> None:
    """Test to convert relative path to full path.

    The full path is based on Python default temporary directory.
    """
    expected: Path = Path("temp")

    def individual_test(server: PathServer) -> None:
        assert expected == server.to_relative_path(
            server.to_full_path(expected)
        )

    _common_test(individual_test)


def test_working() -> None:
    """Test to create temporary working space on local environment."""
    expected: Path = Path(
        "private", "work", "2023", "04", "01", "00", "00", "00", "000000"
    )

    def individual_test(server: PathServer) -> None:
        temporary_path: Path = server.create_local_working_space(override=True)

        assert temporary_path.exists()
        assert expected == server.to_relative_path(temporary_path)

    _common_test(individual_test)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_table()
    test_path()
    test_relative()
    test_full()
    test_working()
    return True
