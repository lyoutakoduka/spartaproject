#!/usr/bin/env python

"""Module to convert path to symbolic link if it's available."""

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
    """Convert path to symbolic link if it's available.

    Args:
        target_root (Path): Path you want to convert to symbolic link.

        symbolic_link (SymbolicLink):
            Paths that is symbolic link and source of symbolic link.

    Returns:
        Path: Converted path.

    """
    if is_relative(target_root, root_path=symbolic_link["source"]):
        return _convert_root(target_root, symbolic_link)

    return target_root
