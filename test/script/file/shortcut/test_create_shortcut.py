#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import uname
from pytest import raises
from tempfile import TemporaryDirectory
from typing import Callable

from script.file.shortcut.create_shortcut import create_shortcut
from script.file.shortcut.get_shortcut_path import get_shortcut_path
from script.path.temporary.create_temporary_file import create_temporary_file


def _common_test(shortcut_target: Path, shortcut_root: Path) -> None:
    shortcut_path: Path = get_shortcut_path(shortcut_target, shortcut_root)
    create_shortcut(shortcut_target, shortcut_path)

    assert shortcut_path.exists()
    assert shortcut_target.name == shortcut_path.stem


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    platform_name = uname()
    if 'Windows' == platform_name.system:
        with TemporaryDirectory() as temporary_path:
            function(Path(temporary_path))


def test_file() -> None:
    def individual_test(temporary_root: Path) -> None:
        source_path: Path = create_temporary_file(temporary_root)
        _common_test(source_path, temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(temporary_root: Path) -> None:
        _common_test(temporary_root, temporary_root)

    _inside_temporary_directory(individual_test)


def test_exist() -> None:
    def individual_test(temporary_root: Path) -> None:
        empty_path: Path = Path('empty')
        with raises(FileNotFoundError, match=str(empty_path)):
            _common_test(empty_path, temporary_root)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_directory()
    return True
