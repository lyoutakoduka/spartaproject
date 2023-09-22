#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Call designated function of designated module."""

from importlib.machinery import SourceFileLoader
from pathlib import Path
from types import ModuleType

from spartaproject.context.default.string_context import Strs
from spartaproject.context.extension.path_context import PathPair
from spartaproject.script.path.modify.get_absolute import get_absolute
from spartaproject.script.path.modify.get_relative import get_relative


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
    relative: Path = get_relative(head_added_path, root_path=root_path)

    module_path: Path = Path(
        root_path, relative.parts[0], 'test', *list(relative.parts[1:])
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


def _call_target_function(module: ModuleType, function: str) -> None:
    if not hasattr(module, function):
        raise ModuleNotFoundError(function)

    return getattr(module, function)()


def _check_call_environment(call_target: PathPair, function: str) -> None:
    loader = SourceFileLoader('temporary', call_target['module'].as_posix())
    _call_target_function(loader.load_module(), function)


def call_function(source: Path, module: Path, function: str = 'main') -> bool:
    """Call function and return True.

    Args:
        source (Path): module path of call source
        module (Path): designated module path
        function (str, optional): designated function name. Defaults to 'main'.

    Returns:
        bool: success if get to the end of function
    """
    call_context: PathPair = {
        key: path
        for key, path in zip(_get_path_key(), [source, module])
    }

    _check_absolute_path(call_context)
    _check_same_path(call_context)

    if _check_test_path(call_context):
        function = 'main'

    _check_call_environment(call_context, function)

    return True
