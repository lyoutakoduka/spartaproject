#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import path as system_path
from pathlib import Path  # use default Path


def main() -> bool:
    system_path.append(str(Path(__file__).parent))
    return True  # TODO: untestable


main()  # not "__name__ == '__main__'" for pytest
