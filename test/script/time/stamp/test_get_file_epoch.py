#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.stamp.get_file_epoch import get_file_epoch


def _common_test(path: Path) -> None:
    assert 1 == len(
        set([get_file_epoch(path, access=status) for status in [False, True]])
    )


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_create() -> None:
    def individual_test(path: Path) -> None:
        _common_test(create_temporary_file(path))

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_create()
    return True
