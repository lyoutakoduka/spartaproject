#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module, util
from pathlib import Path


def _add_system_path(path: str) -> None:
    if path not in sys.path:
        sys.path.insert(0, path)


def _build_call_environment(path: str) -> None:
    module_root: str = str(Path(path).parent)
    _add_system_path(module_root)
    os.chdir(module_root)


def _not_callable_target(module_name: str, func_name: str) -> bool:
    if not util.find_spec(module_name):
        return True

    return not hasattr(import_module(module_name), func_name)


def call_function(module_path: str, func_name: str) -> bool:
    _build_call_environment(module_path)

    module_name: str = str(Path(module_path).stem)

    if _not_callable_target(module_name, func_name):
        return False

    return getattr(import_module(module_name), func_name)()


def main() -> bool:
    MODULE_NAME: str = 'debug_empty.py'
    FUNC_NAME: str = 'main'

    call_path: str = __file__
    module_path: str = str(Path(call_path).with_name(MODULE_NAME))

    result: bool = call_function(module_path, FUNC_NAME)

    return result


if __name__ == '__main__':
    sys.exit(not main())
