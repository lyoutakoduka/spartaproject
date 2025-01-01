#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert relative path to absolute."""

from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.path.modify.current.get_current import get_current


def get_absolute(relative_path: Path, root_path: Path | None = None) -> Path:
    """Function to convert relative path to absolute.

    Args:
        relative_path (Path): Path you want to convert to absolute.

        root_path (Path | None, optional): Defaults to None.
            Root of relative path used for converting path.

    Returns:
        Path: Converted absolute path.
    """
    if relative_path.is_absolute():
        return relative_path

    if root_path is None:
        root_path = get_current()

    return Path(root_path, relative_path)


def get_absolute_array(
    relative_paths: Paths, root_path: Path | None = None
) -> Paths:
    """Function to convert list of relative paths to absolute.

    Args:
        relative_paths (Paths): Paths you want to convert to absolute.

        root_path (Path | None, optional): Defaults to None.
            Root of relative path used for converting path.

    Returns:
        Paths: Converted absolute paths.
    """
    return [get_absolute(path, root_path=root_path) for path in relative_paths]


def get_absolute_pair(
    relative_pair: PathPair, root_path: Path | None = None
) -> PathPair:
    """Function to convert dictionary of relative paths to absolute.

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
