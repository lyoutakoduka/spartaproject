#!/usr/bin/env python

"""Test module to get date time about selected file or directory."""

from os import utime
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.decimal_context import Decs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.time.path.get_file_epoch import get_file_epoch


def _set_invalid_datetime(file_path: Path) -> Path:
    utime(file_path, (0, 0))
    return file_path


def _get_file_epochs(path: Path) -> Decs:
    file_epochs: Decs = []

    for status in [False, True]:
        if epoch := get_file_epoch(path, access=status):
            file_epochs += [epoch]

    return file_epochs


def _common_test(path: Path) -> None:
    file_epochs: Decs = list(set(_get_file_epochs(path)))

    assert len(file_epochs) == 1


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to get the date time about file you select."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root))

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    """Test to get the date time about directory you select."""

    def individual_test(temporary_root: Path) -> None:
        _common_test(create_directory(Path(temporary_root, "temporary")))

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    """Test to check the invalid date time about file you select."""

    def individual_test(temporary_root: Path) -> None:
        file_path: Path = _set_invalid_datetime(
            create_temporary_file(temporary_root),
        )
        for status in [False, True]:
            assert get_file_epoch(file_path, access=status) is None

    _inside_temporary_directory(individual_test)
