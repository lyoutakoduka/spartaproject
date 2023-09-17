#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pytest import raises
from script.execute.call_module import call_function

_SOURCE_PATH: Path = Path(__file__)
_UNKNOWN: str = 'unknown'


def test_unknown_module() -> None:
    error_path = Path(_SOURCE_PATH).with_name(_UNKNOWN + '.py')
    with raises(FileNotFoundError, match='unknown'):
        call_function(_SOURCE_PATH, error_path)


def test_unknown_function() -> None:
    with raises(ModuleNotFoundError, match=_UNKNOWN):
        call_function(_SOURCE_PATH, _SOURCE_PATH, function=_UNKNOWN)


def test_pass() -> None:
    assert call_function(_SOURCE_PATH, _SOURCE_PATH)


def main() -> bool:
    test_pass()
    return True
