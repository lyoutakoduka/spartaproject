#!/usr/bin/env python

from pathlib import Path

from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)


def get_symbolic_link(source_root: Path, symbolic_root: Path) -> SymbolicLink:
    return {"source": source_root, "symbolic": symbolic_root}
