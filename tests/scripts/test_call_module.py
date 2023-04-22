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
        call_function(src_path, error_path, 'test')


def test_unknown_func() -> None:
    with pytest.raises(ModuleNotFoundError, match=unknown):
        call_function(src_path, src_path, unknown)


def test() -> bool:
    call_function(src_path, src_path, 'test')
    return True
