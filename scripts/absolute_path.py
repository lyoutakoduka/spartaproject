#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path
from typing import List

from scripts.same_bools import pair_true
from scripts.path_exists import check_exists

_Strs = List[str]
_Bools = List[bool]


def convert_path(arguments: _Strs) -> _Strs:
    def to_absolute(path: Path) -> str:
        return str(path if path.is_absolute() else Path(os.getcwd(), path))

    return [to_absolute(Path(argument)) for argument in arguments]


def main() -> bool:
    EXISTS_EXPECTED: _Bools = [
        False, True, False, False, False]

    RELATIVE_PATH: _Strs = [
        'develop', 'project', 'sparta', 'scripts', 'debug_empty.py']

    relative_paths: _Strs = [
        str(Path(*RELATIVE_PATH[i:]))
        for i in range(len(RELATIVE_PATH))
    ]

    absolute_paths: _Strs = convert_path(relative_paths)

    file_exists: _Bools = check_exists(absolute_paths)
    result: bool = pair_true(EXISTS_EXPECTED, file_exists)

    return result


if __name__ == '__main__':
    sys.exit(not main())
