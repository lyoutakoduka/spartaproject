#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.same_bools import pair_true
from scripts.path_exists import check_paths, check_path

_Paths = List[Path]
current_path = Path(__file__)


def test_single() -> None:
    assert check_path(current_path)


def test_multi() -> None:
    paths: _Paths = [current_path, current_path.with_name('unknown.py')]
    assert pair_true([True, False], check_paths(paths))


def main() -> bool:
    test_single()
    test_multi()
    return True
