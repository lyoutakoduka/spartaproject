#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Paths = List[Path]
_Bools = List[bool]


def check_path(path: Path) -> bool:
    return Path(path).exists()


def check_paths(paths: _Paths) -> _Bools:
    return [check_path(path) for path in paths]
