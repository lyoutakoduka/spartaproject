#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from pathlib import Path
from datetime import datetime
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from scripts.files.export_json import json_export
from scripts.times.set_timestamp import set_latest
from scripts.times.get_timestamp import get_latest


_INPUT_UTC: str = '2023-04-15T20:09:30.936886+00:00'
_time_utc: datetime = datetime.fromisoformat(_INPUT_UTC)


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    INPUT_JSON: Json = {'A': None}

    with TemporaryDirectory() as tmp_path:
        path: Path = Path(tmp_path, 'tmp.json')
        json_export(path, INPUT_JSON)
        set_latest(path, _time_utc)
        func(path)


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        assert _time_utc == get_latest(path)

    _inside_tmp_directory(individual_test)


def test_jst() -> None:
    INPUT_JST: str = '2023-04-16T05:09:30.936886+09:00'
    _time_jst: datetime = datetime.fromisoformat(INPUT_JST)

    def individual_test(path: Path) -> None:
        assert _time_jst == get_latest(path, jst=True)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
