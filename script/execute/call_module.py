#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib import import_module, util
from os.path import commonpath
from sys import path as system_path

from context.default.string_context import Strs
from context.extension.path_context import Path, PathPair, Paths
from script.path.modify.get_absolute import get_absolute
from script.path.modify.get_relative import get_relative


def _get_path_key() -> Strs:
    return ['source', 'module']


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


def _switch_test_root(call_context: PathPair, head_added_path: Path) -> bool:
    root_path: Path = call_context['source'].parent
    module_path: Path = Path(
        root_path, 'test', get_relative(head_added_path, root_path=root_path)
    )

    if module_path.exists():
        call_context.update({'module': module_path})
        return True

    return False


def _check_test_path(call_context: PathPair) -> bool:
    HEAD: str = 'test' + '_'
    if call_context['source'].name.startswith(HEAD):
        return False

    return _switch_test_root(
        call_context, _replace_file_name(HEAD, call_context['module'])
    )


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
        _get_common_directory(call_context), call_context['module'].parent
    ])


def _check_callable_target(module_name: str, function: str) -> None:
    if not util.find_spec(module_name):
        raise FileNotFoundError(module_name)

    if not hasattr(import_module(module_name), function):
        raise ModuleNotFoundError(function)


def _call_target_function(module_name: str, function: str) -> None:
    getattr(import_module(module_name), function)()


def _check_call_environment(call_target: PathPair, function: str) -> None:
    module_name: str = call_target['module'].stem

    _check_callable_target(module_name, function)
    _call_target_function(module_name, function)


def call_function(
    source_path: Path, module_path: Path, function: str = 'main'
) -> bool:
    call_context: PathPair = {'source': source_path, 'module': module_path}

    _check_absolute_path(call_context)
    _check_same_path(call_context)

    if _check_test_path(call_context):
        function = 'main'

    _check_system_path(call_context)
    _check_call_environment(call_context, function)

    return True
