#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from typing import List

from scripts.call_module import call_function
from scripts.absolute_path import convert_paths

_Strs = List[str]


def main() -> bool:
    FUNC_NAME: str = 'test'

    arguments: _Strs = convert_paths(sys.argv)

    call_function(arguments[0], arguments[1], FUNC_NAME)

    return True


if __name__ == '__main__':
    sys.exit(not main())
