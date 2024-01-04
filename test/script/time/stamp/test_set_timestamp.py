#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.time_context import Times
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)
from pyspartaproj.script.time.stamp.get_timestamp import get_latest
from pyspartaproj.script.time.stamp.set_timestamp import set_latest


def _get_time_text(jst: bool = False) -> Strs:
    times: Strs = [
        "2023-04-01T00:00:00.000001+00:00",
        "2023-04-15T20:09:30.936886+00:00",
    ]
    times_jst: Strs = [
        "2023-04-01T09:00:00.000001+09:00",
        "2023-04-16T05:09:30.936886+09:00",
    ]

    return times_jst if jst else times


def _convert_input_time(times: Strs) -> Times:
    return [datetime.fromisoformat(time) for time in times]


def _set_latest_datetime(path: Path, time_texts: Strs) -> None:
    for status, time in zip([False, True], _convert_input_time(time_texts)):
        set_latest(path, time, access=status)


def _common_test(path: Path, time_texts: Strs) -> None:
    _set_latest_datetime(path, time_texts)

    times: Times = _convert_input_time(_get_time_text())
    results: Times = [
        get_latest(path, access=status) for status in [False, True]
    ]

    for expected, result in zip(times, results):
        assert result == expected


def _inside_temporary_directory(function: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    def individual_test(temporary_root: Path) -> None:
        _common_test(create_temporary_file(temporary_root), _get_time_text())

    _inside_temporary_directory(individual_test)


def test_jst() -> None:
    def individual_test(temporary_root: Path) -> None:
        _common_test(
            create_temporary_file(temporary_root), _get_time_text(jst=True)
        )

    _inside_temporary_directory(individual_test)


def main() -> bool:
    test_file()
    test_jst()
    return True
