#!/usr/bin/env python

from pathlib import Path

from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)


def get_symbolic_link(source_root: Path, symbolic_root: Path) -> SymbolicLink:
    return {"source": source_root, "symbolic": symbolic_root}


def create_symbolic(source_root: Path, symbolic_root: Path) -> SymbolicLink:
    symbolic_root.symlink_to(source_root, target_is_directory=True)
    return get_symbolic_link(source_root, symbolic_root)
