#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module, util
from typing import List, Any, Dict
from pathlib import Path

from scripts.absolute_path import convert_path

_Strs = List[str]
_Pair = Dict[str, str]


def _get_path_key() -> _Strs:
    return ['src', 'module']


def _check_absolute_path(call_context: _Pair) -> None:
    call_context.update({
        type: convert_path(call_context[type])
        for type in _get_path_key()
    })


def _check_same_path(call_context: _Pair) -> None:
    if 1 == len(set([
        Path(call_context[type]).name
        for type in _get_path_key()
    ])):
        OVERRIDE_FILE: str = 'debug_empty.py'
        call_context['module'] = str(
            Path(Path(__file__).with_name(OVERRIDE_FILE)))


def _replace_file_name(path: str) -> str:
    module_path: Path = Path(path)
    return str(module_path.with_name('test' + '_' + module_path.name))


def _replace_to_test_root(test_added_path: str) -> str:
    ROOT_PATH: Path = Path('project', 'sparta')

    root_path: str = convert_path(str(ROOT_PATH))
    return str(Path(
        root_path,
        'tests',
        Path(test_added_path).relative_to(root_path)
    ))


def _check_test_path(call_context: _Pair) -> None:
    test_module_path: str = _replace_to_test_root(
        _replace_file_name(call_context['module']))

    if Path(test_module_path).exists():
        call_context.update({'module': test_module_path, 'func': 'test'})


def _get_common_directory(call_context: _Pair) -> str:
    return os.path.commonpath([
        Path(call_context[type]).parents[1]
        for type in _get_path_key()
    ])


def _add_system_path(imports: _Strs) -> None:
    for path in imports:
        if path in sys.path:
            sys.path.remove(path)
        sys.path.insert(0, path)


def _check_system_path(call_context: _Pair) -> None:
    _add_system_path([
        _get_common_directory(call_context),
        str(Path(call_context['module']).parent),
    ])


def _check_callable_target(module_name: str, func_name: str) -> None:
    if not util.find_spec(module_name):
        raise FileNotFoundError(module_name)

    if not hasattr(import_module(module_name), func_name):
        raise ModuleNotFoundError(func_name)


def _call_target_function(module_name: str, func_name: str) -> None:
    func: Any = getattr(import_module(module_name), func_name)
    func()


def _check_call_environment(call_target: _Pair) -> None:
    module_name: str = str(Path(call_target['module']).stem)
    func_name: str = call_target['func']

    _check_callable_target(module_name, func_name)
    _call_target_function(module_name, func_name)


def call_function(src_path: str, module_path: str, func_name: str) -> bool:
    call_context: _Pair = {
        'src': src_path,
        'module': module_path,
        'func': func_name
    }

    _check_absolute_path(call_context)
    _check_same_path(call_context)
    _check_test_path(call_context)
    _check_system_path(call_context)
    _check_call_environment(call_context)

    return True
