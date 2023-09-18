#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from spartaproject.script.directory.create_directory_parent import \
    create_directory_parent


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_pass() -> None:
    def individual_test(temporary_root: Path) -> None:
        EXPECTED: Path = Path(temporary_root, 'parent')
        parent_path: Path = create_directory_parent(
            Path(EXPECTED, 'temporary.json')
        )

        assert EXPECTED == parent_path
        assert parent_path.exists()

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_pass()
    return True
