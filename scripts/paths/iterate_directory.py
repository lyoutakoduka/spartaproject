#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Generator
from pathlib import Path

_PathGene = Generator[Path, None, None]

DEFAULT_FILTER: str = '**/*'


def _create_filter(depth: int, file: bool, directory: bool, suffix: str) -> str:
    if not file and not directory:
        return ''

    if 0 < depth:
        filter = '*/' * (depth - 1)
    else:
        filter = '**/'

    if file and directory:
        filter += '*'

    if file and not directory:
        filter += '*.' + suffix

    if not file and directory:
        filter += '*/'

    return filter


def walk_iterator(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = '*',
    filter: str = DEFAULT_FILTER,
) -> _PathGene:

    if DEFAULT_FILTER == filter:
        filter = _create_filter(depth, file, directory, suffix)

    if 0 < len(filter):
        print(filter)
        for path in root.glob(filter):
            if root != path:
                yield path
