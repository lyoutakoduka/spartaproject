#!/usr/bin/env python

"""Test module to set current working directory."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.directory.current.get_current import get_current
from pyspartalib.script.directory.current.set_current import SetCurrent


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_current() -> Path:
    return Path().cwd()


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_current() -> None:
    """Test to set current working directory."""

    def individual_test(temporary_root: Path) -> None:
        with SetCurrent(temporary_root):
            _difference_error(get_current(), temporary_root)

    _inside_temporary_directory(individual_test)
