#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.get_file import get_file


def test_relative() -> None:
    expected: Path = Path(
        "pyspartaproj", "script", "path", "modify", "get_file.py"
    )
    assert expected == get_file()


def main() -> bool:
    test_relative()
    return True
