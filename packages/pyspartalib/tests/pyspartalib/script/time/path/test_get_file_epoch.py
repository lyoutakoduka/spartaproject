#!/usr/bin/env python

"""Test module to get date time about selected file or directory."""

from collections.abc import Sized
from os import utime
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.decimal_context import Decs
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.type_context import Type
from pyspartalib.script.directory.create_directory import create_directory
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartalib.script.time.path.get_file_epoch import get_file_epoch
from pyspartalib.script.time.path.set_timestamp import set_invalid


def _length_error(result: Sized, expected: int) -> None:
    if len(result) != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _not_none_error(result: object) -> None:
    if result is not None:
        raise ValueError


def _get_file_epochs(path: Path) -> Decs:
    return [
        epoch
        for status in [False, True]
        if (epoch := get_file_epoch(path, access=status))
    ]


def _common_test(path: Path) -> None:
    file_epochs: Decs = list(set(_get_file_epochs(path)))

    _length_error(file_epochs, 1)
    _none_error(file_epochs[0])


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
        file_path: Path = set_invalid(create_temporary_file(temporary_root))

        for status in [False, True]:
            _not_none_error(get_file_epoch(file_path, access=status))

    _inside_temporary_directory(individual_test)
