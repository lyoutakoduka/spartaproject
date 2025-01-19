#!/usr/bin/env python

"""Test module to get date time about selected file or directory."""

from collections.abc import Sized
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.decimal_context import DecPair
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.type_context import Type
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.time.path.get_file_epoch import get_file_epoch
from pyspartalib.script.time.path.set_timestamp import set_invalid


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _is_access(group: str) -> bool:
    return group == "access"


def _get_file_epoch_pair(path: Path) -> DecPair:
    return {
        group: epoch
        for group in ["update", "access"]
        if (epoch := get_file_epoch(path, access=_is_access(group)))
    }


def _common_test(path: Path) -> None:
    epochs: DecPair = _get_file_epoch_pair(path)

    _length_error(epochs, 2)
    _difference_error(epochs["update"], epochs["access"])


def _invalid_test(path: Path) -> None:
    _length_error(_get_file_epoch_pair(path), 0)


def _set_invalid_date(path: Path) -> Path:
    return set_invalid(create_temporary_file(path))


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
        _invalid_test(_set_invalid_date(temporary_root))

    _inside_temporary_directory(individual_test)
