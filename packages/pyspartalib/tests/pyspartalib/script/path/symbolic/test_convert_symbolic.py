#!/usr/bin/env python

"""Test module to convert path to symbolic link if it's available."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc, Paths
from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)
from pyspartalib.script.path.symbolic.convert_symbolic import (
    convert_symbolic_link,
)
from pyspartalib.script.path.symbolic.create_symbolic import get_symbolic_link


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_directories(path: Path) -> Paths:
    return [Path(path, group) for group in ["source", "symbolic"]]


def _get_link_paths(directories: Paths) -> SymbolicLink:
    return get_symbolic_link(*directories)


def _convert_root(directories: Paths) -> Path:
    return convert_symbolic_link(directories[0], _get_link_paths(directories))


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_convert() -> None:
    """Test to convert path to symbolic link if it's available."""

    def individual_test(temporary_root: Path) -> None:
        directories: Paths = _get_directories(temporary_root)
        _difference_error(_convert_root(directories), directories[1])

    _inside_temporary_directory(individual_test)
