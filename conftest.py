#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path  # use default Path
from sys import path as system_path


def main() -> bool:
    system_path.append(str(Path(__file__).parent))
    return True  # untestable


main()  # not "__name__ == '__main__'" for pytest
