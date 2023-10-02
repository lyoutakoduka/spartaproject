#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Connector to for execution and debugging from VSCode."""


from pyspartaproj.script.execute.debug_launcher import debug_launcher


def test_callable() -> None:
    """Used for test for function call."""
    assert debug_launcher()


def main() -> bool:
    """Test all public functions.

    Returns:
        bool: success if get to the end of function
    """

    test_callable()
    return True
