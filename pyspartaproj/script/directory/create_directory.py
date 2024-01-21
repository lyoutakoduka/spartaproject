#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to create empty directory or directories."""

from pathlib import Path

from pyspartaproj.context.extension.path_context import PathPair, Paths


def create_directory(path: Path) -> Path:
    """Create empty directory to the path you specified.

    Args:
        path (Path): Path you want to create.

    Returns:
        Path: Path that newly created.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_directory_array(paths: Paths) -> Paths:
    """Create empty directories which is specified by list of path.

    Args:
        paths (Paths): List of paths you want to create.

    Returns:
        Paths: List of paths that newly created.
    """
    return [create_directory(path) for path in paths]


def create_directory_pair(path_pair: PathPair) -> PathPair:
    """Create empty directories which is specified by dictionary of path.

    Args:
        path_pair (PathPair): Dictionary of paths you want to create.

    Returns:
        PathPair: Dictionary of paths that newly created.
    """
    return {key: create_directory(path) for key, path in path_pair.items()}
