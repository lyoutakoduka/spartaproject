#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get statistics about file."""

from pathlib import Path

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.extension.path_context import Paths


def get_file_size(path: Path) -> int:
    """Get size of file.

    Args:
        path (Path): Path of file you want to get size.

    Returns:
        int: File size.
    """
    return path.stat().st_size


def get_file_size_array(paths: Paths) -> Ints:
    return [path.stat().st_size for path in paths if path.is_file()]
