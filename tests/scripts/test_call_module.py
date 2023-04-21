#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from scripts.call_module import call_function


def test() -> bool:
    src_path: str = __file__
    module_path = str(Path('project', 'sparta', 'scripts', 'debug_empty.py'))
    error_path = str(Path(src_path).with_name('error.py'))

    # Pass
    assert call_function(src_path, src_path, 'test')

    # Error: unknown func name
    assert not call_function(src_path, module_path, 'error')

    # Error: unknown func name
    assert not call_function(src_path, error_path, 'test')

    return True
