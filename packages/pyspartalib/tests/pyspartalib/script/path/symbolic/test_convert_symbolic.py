#!/usr/bin/env python


from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import Paths
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
