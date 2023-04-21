#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from typing import List

from scripts.call_module import call_function
from scripts.absolute_path import convert_paths

_Strs = List[str]


def _is_test_call(arguments: _Strs) -> bool:
    if 2 != len(arguments):
        return True

    if 1 == len(set([Path(argument).name for argument in arguments])):
        return True

    return False


def _target_override(arguments: _Strs) -> _Strs:
    OVERRIDE_FILE:  _Strs = ['scripts', 'debug_empty.py']

    return [
        arguments[0],
        str(Path(Path(__file__).parent, *OVERRIDE_FILE))]


def main() -> bool:
    FUNC_NAME: str = 'test'

    arguments: _Strs = convert_paths(sys.argv)

    if _is_test_call(arguments):
        arguments = _target_override(arguments)

    call_function(arguments[0], arguments[1], FUNC_NAME)

    return True


if __name__ == '__main__':
    sys.exit(not main())
