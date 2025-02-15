#!/usr/bin/env python

from pathlib import Path

from pyspartalib.script.path.modify.current.get_relative import get_relative
from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)


def _convert_root(target_root: Path, symbolic_link: SymbolicLink) -> Path:
    return Path(
        symbolic_link["symbolic"],
        get_relative(target_root, root_path=symbolic_link["source"]),
    )
