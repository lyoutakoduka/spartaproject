#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.extension.path_context import PathGene

default_filter: str = "**/*"


def _create_filter(
    depth: int, file: bool, directory: bool, suffix: str
) -> str:
    if not file and not directory:
        return ""

    if 0 < depth:
        glob_filter = "*/" * (depth - 1)
    else:
        glob_filter = "**/"

    if file and directory:
        glob_filter += "*"

    if file and not directory:
        glob_filter += "*." + suffix

    if not file and directory:
        glob_filter += "*/"

    return glob_filter


def walk_iterator(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = "*",
    glob_filter: str = default_filter,
) -> PathGene:
    if default_filter == glob_filter:
        glob_filter = _create_filter(depth, file, directory, suffix)

    if 0 < len(glob_filter):
        for path in root.glob(glob_filter):
            if root != path:
                yield path
