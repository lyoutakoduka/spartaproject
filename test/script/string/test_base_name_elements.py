#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to take out name and index from base name of file."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.typed.user_context import BaseName
from pyspartaproj.script.string.base_name_elements import BaseNameElements


def _compare_elements(name: str, index: int, name_elements: BaseName) -> None:
    assert name == name_elements["name"]
    assert index == name_elements["index"]


def _get_identifier() -> str:
    return "_"


def _get_name(names: Strs) -> str:
    return _get_identifier().join(names)


def test_single() -> None:
    """Test for base name of file including only single split identifier."""
    name: str = "file"
    index: int = 1

    name_elements: BaseName = BaseNameElements().split_name(
        _get_name([name, str(index).zfill(4)])
    )
    _compare_elements(name, index, name_elements)


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    return True
