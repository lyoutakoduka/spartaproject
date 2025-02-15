#!/usr/bin/env python

from pathlib import Path

from pyspartalib.script.path.modify.current.get_relative import (
    get_relative,
    is_relative,
)
from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)


def _convert_root(target_root: Path, symbolic_link: SymbolicLink) -> Path:
    return Path(
        symbolic_link["symbolic"],
        get_relative(target_root, root_path=symbolic_link["source"]),
    )


def convert_symbolic_link(
    target_root: Path,
    symbolic_link: SymbolicLink,
) -> Path:
    if is_relative(target_root, root_path=symbolic_link["source"]):
        return _convert_root(target_root, symbolic_link)

    return target_root
