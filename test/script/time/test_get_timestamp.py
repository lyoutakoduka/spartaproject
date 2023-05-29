#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from context.time_context import Times
from script.paths.create_temporary_file import create_temporary_file
from script.time.get_timestamp import get_latest, get_access


def _common_test(times: Times) -> None:
    assert times[0] == times[1]


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_file(Path(temporary_path)))


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        _common_test([function(path) for function in [get_latest, get_access]])

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    def individual_test(path: Path) -> None:
        times: Times = [
            function(path, jst=True) for function in [get_latest, get_access]
        ]
        _common_test(times)

        assert '9:00:00' == str(times[0].utcoffset())

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
