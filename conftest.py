#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path


def main() -> bool:
    sys.path.append(str(Path(__file__).parent))
    return True  # TODO: untestable


main()  # not "__name__ == '__main__'" for pytest
