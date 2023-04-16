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
    CALL_PATH: str = __file__
    MODULE_PATH: str = str(Path(CALL_PATH).with_name('debug_empty.py'))
    FUNC_NAME: str = 'main'

    RESULT: bool = call_function(MODULE_PATH, FUNC_NAME)

    return RESULT


if __name__ == '__main__':
    sys.exit(not main())
