#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from scripts.paths.parent_directory import create_parent_directory


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        func(Path(tmp_path))


def test_pass() -> None:
    def individual_test(tmp_root: Path) -> None:
        EXPECTED: Path = Path(tmp_root, 'parent')
        parent_path: Path = create_parent_directory(Path(EXPECTED, 'tmp.json'))

        assert EXPECTED == parent_path
        assert parent_path.exists()

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_pass()
    return True
