#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from typing import List

from scripts.same_bools import pair_true

_Strs = List[str]
_Bools = List[bool]


def check_path(path: str) -> bool:
    return Path(path).exists()


def check_paths(paths: _Strs) -> _Bools:
    return [check_path(path) for path in paths]


def main() -> bool:
    EXISTS_EXPECTED: _Bools = [False, False, False, True]
    FILE_TYPES: _Strs = ['red', 'green', 'blue', 'empty']

    full_paths: _Strs = [
        str(Path(__file__).with_name(f'debug_{type}.py'))
        for type in FILE_TYPES
    ]

    file_exists: _Bools = check_paths(full_paths)

    result:  bool = pair_true(EXISTS_EXPECTED, file_exists)

    return result


if __name__ == '__main__':
    sys.exit(not main())
