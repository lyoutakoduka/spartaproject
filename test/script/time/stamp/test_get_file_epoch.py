#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.decimal_context import Decs
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _common_test(times: Decs) -> None:
    assert 1 == len(set(times))


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_create() -> None:
    def individual_test(path: Path) -> None:
        file_path: Path = create_temporary_file(path)
        _common_test(
            [
                get_file_epoch(file_path, access=status)
                for status in [False, True]
            ]
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_create()
    return True
