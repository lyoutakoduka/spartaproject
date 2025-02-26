#!/usr/bin/env python

"""Test module to create empty temporary file as json format."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _exists_error(path: Path) -> None:
    if not path.exists():
        raise ValueError


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to create empty temporary file as json format."""

    def individual_test(temporary_root: Path) -> None:
        file_path: Path = create_temporary_file(temporary_root)

        _exists_error(file_path)
        _difference_error(file_path, Path(temporary_root, "temporary.json"))

    _inside_temporary_directory(individual_test)
