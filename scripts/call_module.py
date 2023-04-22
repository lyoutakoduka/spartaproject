#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module, util
from typing import List, Any
from pathlib import Path

from scripts.absolute_path import convert_paths

_Strs = List[str]


def _add_system_path(imports: _Strs) -> None:
    for path in imports:
        if path in sys.path:
            sys.path.remove(path)
        sys.path.insert(0, path)


def _check_callable_target(module_name: str, func_name: str) -> None:
    if not util.find_spec(module_name):
        raise FileNotFoundError(module_name)

    if not hasattr(import_module(module_name), func_name):
        raise ModuleNotFoundError(func_name)


def _get_common_directory(arguments: _Strs) -> str:
    return os.path.commonpath([Path(path).parents[1] for path in arguments])


def _check_same_path(arguments: _Strs) -> bool:
    if 2 != len(arguments):
        return True

    if 1 == len(set([Path(argument).name for argument in arguments])):
        return True

    return False


def _target_override(module_path: str) -> str:
    OVERRIDE_FILE: str = 'debug_empty.py'
    return str(Path(Path(__file__).with_name(OVERRIDE_FILE)))


def call_function(src_path: str, module_path: str, func_name: str) -> bool:
    paths: _Strs = [src_path, module_path]
    paths = convert_paths(paths)

    if _check_same_path(paths):
        module_path = _target_override(paths[0])

    imports: _Strs = [
        _get_common_directory(paths),
        str(Path(module_path).parent),
    ]

    _add_system_path(imports)

    module_name: str = str(Path(module_path).stem)

    _check_callable_target(module_name, func_name)

    func: Any = getattr(import_module(module_name), func_name)
    func()

    return True
