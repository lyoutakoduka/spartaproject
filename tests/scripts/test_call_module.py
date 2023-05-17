#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from pytest import raises

from scripts.call_module import call_function


_SRC_PATH: Path = Path(__file__)
_UNKNOWN: str = 'unknown'


def test_unknown_module() -> None:
    error_path = Path(_SRC_PATH).with_name(_UNKNOWN + '.py')
    with raises(FileNotFoundError, match='unknown'):
        call_function(_SRC_PATH, error_path)


def test_unknown_func() -> None:
    with raises(ModuleNotFoundError, match=_UNKNOWN):
        call_function(_SRC_PATH, _SRC_PATH, func_name=_UNKNOWN)


def test_pass() -> None:
    assert call_function(_SRC_PATH, _SRC_PATH)


def main() -> bool:
    test_pass()
    return True
