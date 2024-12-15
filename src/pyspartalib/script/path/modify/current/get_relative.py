#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to convert absolute path to relative."""

from pathlib import Path

from pyspartalib.context.default.bool_context import Bools
from pyspartalib.context.extension.path_context import PathPair, Paths
from pyspartalib.script.path.modify.current.get_current import get_current


def _get_relative_root(root_path: Path | None = None) -> Path:
    if root_path is None:
        root_path = get_current()

    return root_path


def is_relative(absolute_path: Path, root_path: Path | None = None) -> bool:
    """Check that path is type relative.

    Args:
        absolute_path (Path): Absolute path you want to check.

        root_path (Path | None, optional): Defaults to None.
            Root of absolute path used for checking path.

    Returns:
        bool: True if path is type relative.
    """
    return absolute_path.is_relative_to(_get_relative_root(root_path))


def is_relative_array(
    absolute_paths: Paths, root_path: Path | None = None
) -> Bools:
    """Check that list of paths are type relative at once.

    Args:
        absolute_paths (Paths): Absolute paths you want to check.

        root_path (Path | None, optional): Defaults to None.
            Root of absolute path used for checking paths.

    Returns:
        Bools: List of True if all paths are type relative.
    """
    return [
        is_relative(absolute_path, root_path=root_path)
        for absolute_path in absolute_paths
    ]


def get_relative(absolute_path: Path, root_path: Path | None = None) -> Path:
    """Function to convert absolute path to relative.

    Args:
        absolute_path (Path): Path you want to convert to relative.

        root_path (Path | None, optional): Defaults to None.
            Root of absolute path used for converting path.

    Raises:
        ValueError:
            Throw an exception if absolute path don't include root path.

    Returns:
        Path: Converted relative path.
    """
    root_path = _get_relative_root(root_path)

    if not is_relative(absolute_path, root_path=root_path):
        raise ValueError

    return absolute_path.relative_to(root_path)


def get_relative_array(
    absolute_paths: Paths, root_path: Path | None = None
) -> Paths:
    """Function to convert list of absolute paths to relative.

    Args:
        absolute_paths (Paths): Paths you want to convert to relative.

        root_path (Path | None, optional): Defaults to None.
            Root of absolute paths used for converting path.
            It's used for argument "root_path" of function "get_relative".

    Returns:
        Paths: Converted relative paths.
    """
    return [get_relative(path, root_path=root_path) for path in absolute_paths]


def get_relative_pair(
    absolute_pair: PathPair, root_path: Path | None = None
) -> PathPair:
    """Function to convert dictionary of absolute paths to relative.

    Args:
        absolute_pair (PathPair): Paths you want to convert to relative.

        root_path (Path | None, optional): Defaults to None.
            Root of absolute paths used for converting path.
            It's used for argument "root_path" of function "get_relative".

    Returns:
        PathPair: Converted relative paths.
    """
    return {
        key: get_relative(path, root_path=root_path)
        for key, path in absolute_pair.items()
    }
