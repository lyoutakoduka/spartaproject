#!/usr/bin/env python

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)
from pyspartalib.script.path.symbolic.create_symbolic import create_symbolic
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _status_error(status: bool) -> None:
    if not status:
        raise ValueError


def _create_symbolic(path: Path) -> SymbolicLink:
    return create_symbolic(
        create_temporary_tree(Path(path, "source"), tree_deep=1),
        Path(path, "symbolic"),
    )
