#!/usr/bin/env python

"""Module to create symbolic link and link information."""

from pathlib import Path

from pyspartalib.script.path.symbolic.context.symbolic_context import (
    SymbolicLink,
)


def get_symbolic_link(source_root: Path, symbolic_root: Path) -> SymbolicLink:
    """Get type that represent paths about symbolic link.

    Args:
        source_root (Path): Path that is a target of symbolic link.

        symbolic_root (Path): Path of symbolic link you create.

    Returns:
        SymbolicLink: User defined type about symbolic link.

    """
    return {"source": source_root, "symbolic": symbolic_root}


def create_symbolic_link(
    source_root: Path,
    symbolic_root: Path,
) -> SymbolicLink:
    """Create symbolic link and link information.

    Args:
        source_root (Path): Path that is a target of symbolic link.

        symbolic_root (Path): Path of symbolic link you create.

    Returns:
        SymbolicLink: User defined type about symbolic link.

    """
    symbolic_root.symlink_to(source_root, target_is_directory=True)
    return get_symbolic_link(source_root, symbolic_root)
