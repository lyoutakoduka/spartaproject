#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from contexts.time_context import Times
from scripts.files.export_json import json_export
from scripts.times.get_timestamp import get_latest, get_create


def _common_test(times: Times) -> None:
    assert times[0] == times[1]


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    INPUT_JSON: Json = {'A': None}

    with TemporaryDirectory() as tmp_path:
        path: Path = Path(tmp_path, 'tmp.json')
        json_export(path, INPUT_JSON)
        func(path)


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        _common_test([func(path) for func in [get_latest, get_create]])

    _inside_tmp_directory(individual_test)


def test_jst() -> None:
    def individual_test(path: Path) -> None:
        times: Times = [
            func(path, jst=True)
            for func in [get_latest, get_create]
        ]
        _common_test(times)

        assert '9:00:00' == str(times[0].utcoffset())

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
