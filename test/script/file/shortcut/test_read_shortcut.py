#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import uname
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.interface.pytest import fail, raises
from pyspartaproj.script.file.shortcut.create_shortcut import create_shortcut
from pyspartaproj.script.file.shortcut.read_shortcut import read_shortcut
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _common_test(shortcut_target: Path, shortcut_root: Path) -> None:
    shortcut_path: Path = Path(shortcut_root, shortcut_target.name + ".lnk")
    create_shortcut(shortcut_target, shortcut_path)

    if returned_target := read_shortcut(shortcut_path):
        assert shortcut_target == returned_target
    else:
        fail()


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root), temporary_root)

    _inside_temporary_directory(individual_test)


def test_directory() -> None:
    def individual_test(temporary_root: Path) -> None:
        _common_test(temporary_root, temporary_root)

    _inside_temporary_directory(individual_test)


def test_exist() -> None:
    def individual_test(temporary_root: Path) -> None:
        empty_path: Path = Path("empty.lnk")

        if "Windows" == uname().system:
            with raises(FileNotFoundError):
                read_shortcut(empty_path)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_directory()
    test_exist()
    return True
