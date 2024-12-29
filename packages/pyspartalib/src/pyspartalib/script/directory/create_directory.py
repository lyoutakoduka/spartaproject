#!/usr/bin/env python

"""Module to create empty directory or directories."""

from pathlib import Path

from pyspartalib.context.extension.path_context import PathPair, Paths


def create_directory(path: Path) -> Path:
    """Create empty directory to the path you specified.

    Args:
        path (Path): Path you want to create.

    Returns:
        Path: Path witch is newly created.

    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_directory_array(paths: Paths) -> Paths:
    """Create empty directories which is specified by list of path.

    Args:
        paths (Paths): List of paths you want to create.

    Returns:
        Paths: List of paths witch is newly created.

    """
    return [create_directory(path) for path in paths]


def create_directory_pair(path_pair: PathPair) -> PathPair:
    """Create empty directories which is specified by dictionary of path.

    Args:
        path_pair (PathPair): Dictionary of paths you want to create.

    Returns:
        PathPair: Dictionary of paths witch is newly created.

    """
    return {key: create_directory(path) for key, path in path_pair.items()}
