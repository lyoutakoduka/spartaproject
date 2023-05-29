#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from script.paths.create_temporary_file import create_temporary_file


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_pass() -> None:
    def individual_test(temporary_path: Path) -> None:
        EXPECTED: Path = Path(temporary_path, 'temporary.json')
        file_path: Path = create_temporary_file(temporary_path)
        assert EXPECTED == file_path
        assert file_path.exists()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_pass()
    return True
