#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from context.default.string_context import Strs
from context.extension.time_context import Times
from script.path.temporary.create_temporary_file import create_temporary_file
from script.time.stamp.get_timestamp import get_access, get_latest
from script.time.stamp.set_timestamp import set_access, set_latest

_TIMES: Strs = [
    '2023-04-01T00:00:00.000001+00:00', '2023-04-15T20:09:30.936886+00:00'
]


def _convert_input_time(times: Strs) -> Times:
    return [datetime.fromisoformat(time)for time in times]


def _common_test(path: Path) -> None:
    times: Times = _convert_input_time(_TIMES)
    results: Times = [function(path) for function in [get_latest, get_access]]

    for expected, result in zip(times, results):
        assert result == expected


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(create_temporary_file(Path(temporary_path)))


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        times: Times = _convert_input_time(_TIMES)
        for function, time in zip([set_latest, set_access], times):
            function(path, time)
        _common_test(path)

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    TIMES_JST: Strs = [
        '2023-04-01T09:00:00.000001+09:00', '2023-04-16T05:09:30.936886+09:00'
    ]

    def individual_test(path: Path) -> None:
        times: Times = _convert_input_time(TIMES_JST)
        for function, time in zip([set_latest, set_access], times):
            function(path, time)
        _common_test(path)

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
