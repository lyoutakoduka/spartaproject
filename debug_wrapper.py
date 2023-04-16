#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from typing import List

from scripts.call_module import call_function

_Strs = List[str]

OVERRIDE_FILE:  _Strs = ['scripts', 'debug_empty.py']
FUNC_NAME: str = 'main'


def _is_test_call(arguments: _Strs) -> bool:
    if 2 != len(arguments):
        return True

    if 1 == len(set([Path(argument).name for argument in arguments])):
        return True

    return False


def _target_override(arguments: _Strs) -> _Strs:
    return [
        arguments[0],
        str(Path(Path(__file__).parent, *OVERRIDE_FILE))]


def main() -> bool:
    arguments: _Strs = sys.argv

    if _is_test_call(arguments):
        arguments = _target_override(arguments)

    module_path: str = arguments[1]

    RESULT: bool = call_function(module_path, FUNC_NAME)

    return RESULT


if __name__ == '__main__':
    sys.exit(not main())
