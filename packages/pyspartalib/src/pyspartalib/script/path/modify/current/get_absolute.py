#!/usr/bin/env python

"""Module to convert relative path to absolute."""

from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.directory.current.get_current import get_current


def _extract_parent(relative_path: Path, size: int) -> Path:
    return Path(*list(relative_path.parts)[:size])


def is_absolute(relative_path: Path, root_path: Path | None = None) -> bool:
    if root_path is None:
        return relative_path.is_absolute()

    return _extract_parent(relative_path, len(root_path.parts)) == root_path


def get_absolute(relative_path: Path, root_path: Path | None = None) -> Path:
    """Convert relative path to absolute.

    Args:
        relative_path (Path): Path you want to convert to absolute.

        root_path (Path | None, optional): Defaults to None.
            Root of relative path used for converting path.

    Returns:
        Path: Converted absolute path.

    """
    if is_absolute(relative_path, root_path=root_path):
        return relative_path

    if root_path is None:
        root_path = get_current()

    return Path(root_path, relative_path)


def get_absolute_array(
    relative_paths: Paths,
    root_path: Path | None = None,
) -> Paths:
    """Convert list of relative paths to absolute.

    Args:
        relative_paths (Paths): Paths you want to convert to absolute.

        root_path (Path | None, optional): Defaults to None.
            Root of relative path used for converting path.

    Returns:
        Paths: Converted absolute paths.

    """
    return [get_absolute(path, root_path=root_path) for path in relative_paths]


def get_absolute_pair(
    relative_pair: PathPair,
    root_path: Path | None = None,
) -> PathPair:
    """Convert dictionary of relative paths to absolute.

    Args:
        relative_pair (PathPair): Paths you want to convert to absolute.

        root_path (Path | None, optional): Defaults to None.
            Root of relative path used for converting path.

    Returns:
        PathPair: Converted absolute paths.

    """
    return {
        key: get_absolute(path, root_path=root_path)
        for key, path in relative_pair.items()
    }
