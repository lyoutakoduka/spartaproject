#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to upload file or directory by SFTP functionality."""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.directory.create_directory import create_directory
from pyspartaproj.script.directory.date_time_space import get_working_space
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartaproj.script.server.local.upload_server import UploadServer


def _common_test(server: UploadServer, source_path: Path) -> None:
    assert server.upload(source_path)


def _inside_temporary_directory(
    function: Callable[[UploadServer, Path], None]
) -> None:
    server: UploadServer = UploadServer()
    assert server.connect()

    function(server, server.create_local_working_space(jst=True))


def test_file() -> None:
    """Test to upload single file to server."""

    def individual_test(server: UploadServer, temporary_path: Path) -> None:
        _common_test(server, create_temporary_file(temporary_path))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to upload single directory to server."""

    def individual_test(server: UploadServer, temporary_path: Path) -> None:
        _common_test(
            server, create_directory(Path(temporary_path, "directory"))
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    """Test to upload multiple files and directories to server."""

    def individual_test(server: UploadServer, temporary_path: Path) -> None:
        _common_test(
            server,
            create_temporary_tree(Path(temporary_path, "tree"), tree_deep=2),
        )

    _inside_temporary_directory(individual_test)


def test_place() -> None:
    """Test to upload single file from selected local root to server."""
    server: UploadServer = UploadServer()
    assert server.connect()

    with TemporaryDirectory() as temporary_path:
        working_path: Path = Path(
            server.get_path("work_root"), get_working_space(jst=True)
        )
        source_path: Path = create_temporary_file(
            Path(temporary_path, working_path)
        )

        assert server.upload(
            source_path, destination=Path(working_path, source_path.name)
        )


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_file()
    test_directory()
    test_tree()
    test_place()
    return True
