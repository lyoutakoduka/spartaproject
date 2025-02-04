#!/usr/bin/env python

"""Test module to get current working directory."""

from os import chdir
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.directory.current.get_current import get_current


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _set_current(path: Path) -> None:
    chdir(path)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_current() -> None:
    """Test to get current working directory."""

    def individual_test(temporary_root: Path) -> None:
        _set_current(temporary_root)
        _difference_error(get_current(), temporary_root)

    _inside_temporary_directory(individual_test)
