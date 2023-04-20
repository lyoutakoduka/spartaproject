#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from importlib import import_module, util
from typing import List
from pathlib import Path

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


def call_function(module_path: str, func_name: str, imports: _Strs = []) -> bool:
    _add_system_path(imports + [str(Path(module_path).parent)])

    module_name: str = str(Path(module_path).stem)

    if _not_callable_target(module_name, func_name):
        return False

    return getattr(import_module(module_name), func_name)()


def main() -> bool:
    MODULE_NAME: str = 'debug_empty.py'
    FUNC_NAME: str = 'main'

    call_path: str = __file__
    module_path: str = str(Path(call_path).with_name(MODULE_NAME))
    imports = [str(Path(module_path).parents[2])]

    result: bool = call_function(module_path, FUNC_NAME, imports=imports)

    return result


if __name__ == '__main__':
    sys.exit(not main())
