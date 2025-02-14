#!/usr/bin/env python

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import Paths, Paths2
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.modify.current.get_relative import get_relative
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


def _get_symbolic_paths(symbolic_link: SymbolicLink) -> Paths:
    return [symbolic_link["source"], symbolic_link["symbolic"]]


def _get_relative_paths(working_root: Path) -> Paths:
    return [
        get_relative(path, root_path=working_root)
        for path in walk_iterator(working_root)
    ]


def _get_relative_pair(symbolic_link: SymbolicLink) -> Paths2:
    return [
        _get_relative_paths(working_root)
        for working_root in _get_symbolic_paths(symbolic_link)
    ]
