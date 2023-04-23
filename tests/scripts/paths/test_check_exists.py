#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.bools.same_pair import bool_same_pair
from scripts.paths.check_exists import path_array_exists, path_exists

_Paths = List[Path]
current_path = Path(__file__)


def test_single() -> None:
    assert path_exists(current_path)


def test_multi() -> None:
    paths: _Paths = [current_path, current_path.with_name('unknown.py')]
    assert bool_same_pair([True, False], path_array_exists(paths))


def main() -> bool:
    test_single()
    test_multi()
    return True
