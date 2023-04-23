#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

from scripts.same_bools import pair_true
from scripts.path_exists import check_paths, check_path

_Strs = List[str]


def test_single() -> None:
    assert check_path(__file__)


def test_multi() -> None:
    paths: _Strs = [__file__, str(Path(__file__).with_name('unknown.py'))]
    assert pair_true([True, False], check_paths(paths))


def main() -> bool:
    test_single()
    test_multi()
    return True
