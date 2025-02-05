#!/usr/bin/env python

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_current() -> Path:
    return Path().cwd()


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))
