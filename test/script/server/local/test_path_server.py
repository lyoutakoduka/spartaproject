#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle paths about file and directory on server."""

from pathlib import Path

from pyspartaproj.script.server.local.path_server import PathServer


def _compare_working(temporary_root: Path, result: Path) -> None:
    assert result.exists()
    assert result == Path(temporary_root, "local")


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


def test_relative() -> None:
    """Test to convert full path to relative path.

    The full path is based on Python default temporary directory.
    """
    expected: Path = Path("temp")
    server = PathServer()

    assert expected == server.to_relative_path(
        Path(server.get_root(), expected)
    )


def test_full() -> None:
    """Test to convert relative path to full path.

    The full path is based on Python default temporary directory.
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
    test_relative()
    test_full()
    return True
