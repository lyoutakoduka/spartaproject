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
        filter = "*/" * (depth - 1)
    else:
        filter = "**/"

    if file and directory:
        filter += "*"

    if file and not directory:
        filter += "*." + suffix

    if not file and directory:
        filter += "*/"

    return filter


def walk_iterator(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = "*",
    filter: str = default_filter,
) -> PathGene:
    if default_filter == filter:
        filter = _create_filter(depth, file, directory, suffix)

    if 0 < len(filter):
        for path in root.glob(filter):
            if root != path:
                yield path
