#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pathlib import Path

from scripts.call_module import call_function


src_path: str = __file__
unknown: str = 'unknown'


def test_unknown_module() -> None:
    error_path = str(Path(src_path).with_name(unknown + '.py'))
    with pytest.raises(FileNotFoundError, match='unknown'):
        call_function(src_path, error_path)


def test_unknown_func() -> None:
    with pytest.raises(ModuleNotFoundError, match=unknown):
        call_function(src_path, src_path, func_name=unknown)


def test_pass() -> None:
    assert call_function(src_path, src_path)


def main() -> bool:
    test_unknown_module()
    test_unknown_func()
    test_pass()
    return True
