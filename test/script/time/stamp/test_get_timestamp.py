#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.extension.time_context import Times
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.stamp.get_timestamp import get_latest


def _common_test(times: Times) -> None:
    assert times[0] == times[1]


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_file(Path(temporary_path)))


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        _common_test(
            [get_latest(path, access=status) for status in [False, True]]
        )

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    def individual_test(path: Path) -> None:
        times: Times = [
            get_latest(path, access=status, jst=True)
            for status in [False, True]
        ]
        _common_test(times)

        assert "9:00:00" == str(times[0].utcoffset())

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
