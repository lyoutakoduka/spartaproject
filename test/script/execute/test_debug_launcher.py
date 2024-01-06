#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Connector to for execution and debugging from VSCode."""

from pyspartaproj.script.execute.debug_launcher import debug_launcher
from pyspartaproj.script.feature_flags import in_development


def test_callable() -> None:
    """Used for test for function call."""
    if in_development():
        assert debug_launcher()


def main() -> bool:
    """Test all public functions.

    Returns:
        bool: Success if get to the end of function.
    """
    test_callable()
    return True
