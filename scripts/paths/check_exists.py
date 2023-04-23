#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Paths = List[Path]
_Bools = List[bool]


def path_exists(path: Path) -> bool:
    return Path(path).exists()


def path_array_exists(paths: _Paths) -> _Bools:
    return [path_exists(path) for path in paths]
