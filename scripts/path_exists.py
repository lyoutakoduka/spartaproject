#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

_Strs = List[str]
_Bools = List[bool]


def check_path(path: str) -> bool:
    return Path(path).exists()


def check_paths(paths: _Strs) -> _Bools:
    return [check_path(path) for path in paths]
