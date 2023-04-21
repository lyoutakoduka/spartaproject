#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module, util
from typing import List
from pathlib import Path

from scripts.absolute_path import convert_path

_Strs = List[str]


def _add_system_path(imports: _Strs) -> None:
    for path in imports:
        if path in sys.path:
            sys.path.remove(path)
        sys.path.insert(0, path)


def _not_callable_target(module_name: str, func_name: str) -> bool:
    if not util.find_spec(module_name):
        return True

    return not hasattr(import_module(module_name), func_name)


def _get_common_directory(arguments: _Strs) -> str:
    return os.path.commonpath([Path(path).parents[1] for path in arguments])


def _is_test_call(arguments: _Strs) -> bool:
    if 2 != len(arguments):
        return True

    if 1 == len(set([Path(argument).name for argument in arguments])):
        return True

    return False


def _target_override(module_path: str) -> str:
    OVERRIDE_FILE:  _Strs = ['scripts', 'debug_empty.py']
    return str(Path(Path(module_path).parent, *OVERRIDE_FILE))


def call_function(src_path: str, module_path: str, func_name: str) -> bool:
    src_path = convert_path(src_path)
    module_path = convert_path(module_path)

    if _is_test_call([src_path, module_path]):
        module_path = _target_override(module_path)

    imports: _Strs = [
        _get_common_directory([src_path, module_path]),
        str(Path(module_path).parent),
    ]

    _add_system_path(imports)

    module_name: str = str(Path(module_path).stem)

    if _not_callable_target(module_name, func_name):
        return False

    return getattr(import_module(module_name), func_name)()


def main() -> bool:
    MODULE_NAME: str = 'debug_empty.py'
    FUNC_NAME: str = 'main'

    call_path: str = __file__
    module_path: str = str(Path(call_path).with_name(MODULE_NAME))

    result: bool = call_function(call_path, module_path, FUNC_NAME)

    return result


if __name__ == '__main__':
    sys.exit(not main())
