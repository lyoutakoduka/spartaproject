#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Execution and debugging from VSCode."""

from pathlib import Path
from sys import argv

from pyspartaproj.script.execute.call_module import call_function


def main() -> int:
    """Call main function of designated module.

    Returns:
        bool: success if get to the end of function
    """
    return call_function(Path(argv[0]), Path(argv[1]))


if __name__ == "__main__":
    main()
