#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from pathlib import Path
from datetime import datetime
from tempfile import TemporaryDirectory

from contexts.string_context import Strs
from contexts.time_context import Times
from scripts.files.export_json import json_export
from scripts.times.set_timestamp import set_latest, set_access
from scripts.times.get_timestamp import get_latest, get_access

_TIMES: Strs = [
    '2023-04-01T00:00:00.000001+00:00',
    '2023-04-15T20:09:30.936886+00:00',
]


def _convert_input_time(times: Strs) -> Times:
    return [datetime.fromisoformat(time)for time in times]


def _common_test(path: Path) -> None:
    times: Times = _convert_input_time(_TIMES)
    results: Times = [func(path) for func in [get_latest, get_access]]

    for expected, result in zip(times, results):
        assert result == expected


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    with TemporaryDirectory() as tmp_path:
        func(json_export(Path(tmp_path, 'tmp.json'), 'test'))


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        times: Times = _convert_input_time(_TIMES)
        for func, time in zip([set_latest, set_access], times):
            func(path, time)
        _common_test(path)

    _inside_tmp_directory(individual_test)


def test_jst() -> None:
    TIMES_JST: Strs = [
        '2023-04-01T09:00:00.000001+09:00',
        '2023-04-16T05:09:30.936886+09:00',
    ]

    def individual_test(path: Path) -> None:
        times: Times = _convert_input_time(TIMES_JST)
        for func, time in zip([set_latest, set_access], times):
            func(path, time)
        _common_test(path)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
