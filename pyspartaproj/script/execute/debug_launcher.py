#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Execution and debugging from VSCode."""

from pathlib import Path
from sys import argv

from pyspartaproj.script.execute.call_module import call_function
from pyspartaproj.script.feature_flags import in_development


def debug_test() -> bool:
    """Function is used for test for function call.

    Returns:
        bool: just return True.
    """
    return True


def debug_launcher() -> bool:
    """An error has occurred if called from this this module by VSCode.

    Returns:
        bool: success if get to the end of function
    """
    if in_development():
        return call_function(Path(argv[0]), Path(argv[1]))

    return True


if __name__ == "__main__":
    debug_launcher()
