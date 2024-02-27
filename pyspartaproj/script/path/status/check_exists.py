#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to check existing of files or directories."""

from pathlib import Path

from pyspartaproj.context.default.bool_context import BoolPair, Bools
from pyspartaproj.context.extension.path_context import PathPair, Paths


def _check_exists(path: Path) -> bool:
    return path.exists()


def check_exists_array(paths: Paths) -> Bools:
    """Check existing of list of file or directory.

    Args:
        paths (Paths): Paths you want to check existing.

    Returns:
        Bools: Return list of True if file or directory is exists.
    """
    return [_check_exists(path) for path in paths]


def check_exists_pair(paths: PathPair) -> BoolPair:
    """Check existing of directory of file or directory.

    Args:
        paths (PathPair): Paths you want to check existing.

    Returns:
        BoolPair: Return directory of True if file or directory is exists.
    """
    return {key: _check_exists(path) for key, path in paths.items()}
