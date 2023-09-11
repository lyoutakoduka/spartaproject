#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from script.directory.create_directory import create_directory
from script.path.temporary.create_temporary_file import create_temporary_file
from script.path.temporary.create_temporary_tree import create_temporary_tree
from script.server.upload_server import UploadServer


def _common_test(server: UploadServer, source_path: Path) -> None:
    assert server.upload(source_path)


def _inside_temporary_directory(
    function: Callable[[UploadServer], None]
) -> None:
    server: UploadServer = UploadServer()

    if server.connect():
        function(server)


def test_file() -> None:
    def individual_test(server: UploadServer) -> None:
        _common_test(server, create_temporary_file(server.get_working_space()))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(server: UploadServer) -> None:
        _common_test(
            server,
            create_directory(Path(server.get_working_space(), 'directory'))
        )

    _inside_temporary_directory(individual_test)


def test_tree() -> None:
    def individual_test(server: UploadServer) -> None:
        source_path: Path = Path(server.get_working_space(), 'tree')
        create_temporary_tree(source_path, tree_deep=2)
        _common_test(server, source_path)

    _inside_temporary_directory(individual_test)


def test_place() -> None:
    def individual_test(server: UploadServer) -> None:
        with TemporaryDirectory() as temporary_path:
            source_path: Path = create_temporary_file(Path(temporary_path))

            assert server.upload(
                source_path,
                destination=Path(
                    server.to_remote_path(server.get_working_space()),
                    source_path.name
                )
            )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_directory()
    test_tree()
    test_place()
    return True
