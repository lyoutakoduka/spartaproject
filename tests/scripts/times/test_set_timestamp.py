#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable
from tempfile import TemporaryDirectory

from contexts.json_context import Json
from contexts.path_context import Path
from scripts.files.export_json import json_export
from scripts.times.set_timestamp import set_latest
from scripts.times.get_timestamp import get_latest


_INPUT_UTC: str = '2023-04-15T20:09:30.936886+00:00'


def _inside_tmp_directory(func: Callable[[Path], None]) -> None:
    INPUT_JSON: Json = {'A': None}

    with TemporaryDirectory() as tmp_path:
        path: Path = Path(tmp_path, 'tmp.json')
        json_export(path, INPUT_JSON)
        func(path)
        assert _INPUT_UTC == get_latest(path)


def test_utc() -> None:
    def individual_test(path: Path) -> None:
        set_latest(path, _INPUT_UTC)

    _inside_tmp_directory(individual_test)


def test_jst() -> None:
    INPUT_JST: str = '2023-04-16T05:09:30.936886+09:00'

    def individual_test(path: Path) -> None:
        set_latest(path, INPUT_JST)

    _inside_tmp_directory(individual_test)


def main() -> bool:
    test_utc()
    test_jst()
    return True
