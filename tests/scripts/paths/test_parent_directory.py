#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from scripts.paths.parent_directory import create_parent_directory


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_pass() -> None:
    def individual_test(temporary_root: Path) -> None:
        EXPECTED: Path = Path(temporary_root, 'parent')
        parent_path: Path = create_parent_directory(
            Path(EXPECTED, 'temporary.json')
        )

        assert EXPECTED == parent_path
        assert parent_path.exists()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_pass()
    return True
