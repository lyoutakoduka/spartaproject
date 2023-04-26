#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Generator
from pathlib import Path

_PathGene = Generator[Path, None, None]

DEFAULT_FILTER: str = '**/*'


def _create_filter(depth: int, file: bool, directory: bool, suffix: str) -> str:
    if 0 < depth:
        filter = '*/' * (depth - 1)
    else:
        filter = '**/'

    if file and directory:
        filter += '*'
    elif file and not directory:
        filter += '*.' + suffix

    return filter


def walk_iterator(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = '*',
    filter: str = DEFAULT_FILTER,
) -> _PathGene:

    start_iter = True

    if DEFAULT_FILTER == filter:
        if not file and not directory:
            start_iter = False
        else:
            filter = _create_filter(depth, file, directory, suffix)

    if start_iter:
        for path in root.glob(filter):
            if root != path:
                yield path
