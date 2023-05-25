#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib import import_module, util
from os.path import commonpath
from sys import path as system_path
from typing import Any

from contexts.path_context import Path, Paths, PathPair
from contexts.string_context import Strs
from scripts.paths.get_absolute import get_absolute


def _get_path_key() -> Strs:
    return ['src', 'module']


def _check_absolute_path(call_context: PathPair) -> None:
    call_context.update({
        type: get_absolute(call_context[type])
        for type in _get_path_key()
    })


def _check_same_path(call_context: PathPair) -> None:
    if 1 == len(set([
        call_context[type].name
        for type in _get_path_key()
    ])):
        OVERRIDE_FILE: str = 'debug_empty.py'
        call_context['module'] = Path(__file__).with_name(OVERRIDE_FILE)


def _replace_file_name(head: str, module_path: Path) -> Path:
    return module_path.with_name(head + module_path.name)


def _switch_test_root(head_added_path: Path, root_path: Path) -> Path:
    return Path(root_path, 'tests', head_added_path.relative_to(root_path))


def _update_module_path(
    call_context: PathPair,
    root_names: Strs,
    head_added_path: Path,
    index: int,
) -> bool:
    root_path: Path = get_absolute(Path(*root_names[:index + 1]))
    if not head_added_path.is_relative_to(root_path):
        return False

    module_path: Path = _switch_test_root(head_added_path, root_path)
    if not module_path.exists():
        return False

    call_context.update({'module': module_path})
    return True


def _check_test_path(call_context: PathPair) -> bool:
    HEAD: str = 'test' + '_'
    if call_context['src'].name.startswith(HEAD):
        return False

    ROOT_NAMES: Strs = ['project', 'sparta']
    head_added_path: Path = _replace_file_name(HEAD, call_context['module'])

    for i in range(len(ROOT_NAMES)):
        if _update_module_path(call_context, ROOT_NAMES, head_added_path, i):
            return True

    return False


def _get_common_directory(call_context: PathPair) -> Path:
    return Path(commonpath([
        str(call_context[type].parents[1]) for type in _get_path_key()
    ]))


def _add_system_path(imports: Paths) -> None:
    for import_path in imports:
        path: str = str(import_path)
        if path in system_path:
            system_path.remove(path)
        system_path.insert(0, path)


def _check_system_path(call_context: PathPair) -> None:
    _add_system_path([
        _get_common_directory(call_context), call_context['module'].parent,
    ])


def _check_callable_target(module_name: str, func_name: str) -> None:
    if not util.find_spec(module_name):
        raise FileNotFoundError(module_name)

    if not hasattr(import_module(module_name), func_name):
        raise ModuleNotFoundError(func_name)


def _call_target_function(module_name: str, func_name: str) -> None:
    func: Any = getattr(import_module(module_name), func_name)
    func()


def _check_call_environment(call_target: PathPair, func_name: str) -> None:
    module_name: str = call_target['module'].stem

    _check_callable_target(module_name, func_name)
    _call_target_function(module_name, func_name)


def call_function(
    src_path: Path, module_path: Path, func_name: str = 'main',
) -> bool:
    call_context: PathPair = {'src': src_path, 'module': module_path}

    _check_absolute_path(call_context)
    _check_same_path(call_context)

    if _check_test_path(call_context):
        func_name = 'main'

    _check_system_path(call_context)
    _check_call_environment(call_context, func_name)

    return True
