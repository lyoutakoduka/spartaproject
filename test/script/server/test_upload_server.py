#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from script.path.temporary.create_temporary_file import create_temporary_file

from script.server.upload_server import UploadServer


def _common_test(server: UploadServer, source_path: Path) -> None:
    SOURCE_ROOT: Path = Path('private', 'work', 'upload')

    assert server.upload(source_path, Path(SOURCE_ROOT, source_path.name))


def _inside_temporary_directory(
    function: Callable[[UploadServer, Path], None]
) -> None:
    server: UploadServer = UploadServer()

    if server.connect():
        with TemporaryDirectory() as temporary_path:
            function(server, Path(temporary_path))


def test_file() -> None:
    def individual_test(server: UploadServer, temporary_path: Path) -> None:
        _common_test(server, create_temporary_file(Path(temporary_path)))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    return True
