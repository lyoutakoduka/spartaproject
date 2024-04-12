#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to take out name and index from base name of file."""

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.typed.user_context import BaseName
from pyspartaproj.interface.pytest import fail
from pyspartaproj.script.string.base_name_elements import BaseNameElements


def _compare_name(name: str, name_elements: BaseName) -> None:
    assert name == name_elements["name"]


def _compare_index(index: int, name_elements: BaseName) -> None:
    assert index == name_elements["index"]


def _compare_elements(name: str, index: int, name_elements: BaseName) -> None:
    _compare_name(name, name_elements)
    _compare_index(index, name_elements)


def _get_identifier() -> str:
    return "_"


def _get_name(names: Strs) -> str:
    return _get_identifier().join(names)


def _get_index(index: int, digit: int) -> str:
    return str(index).zfill(digit)


def _merge_base_name(name: str, index_text: str) -> str:
    return name + _get_identifier() + index_text


def _get_base_name(name: str, index: int) -> str:
    return _merge_base_name(name, _get_index(index, 1))


def _get_base_name_option(name: str, index: int) -> str:
    return _merge_base_name(name, "v" + _get_index(index, 1) + "a")


def _get_base_name_digit(name: str, index: int) -> str:
    return _merge_base_name(name, _get_index(index, 4))


def _compare_base_name(
    name: str, index: int, elements: BaseName | None
) -> None:
    if elements is None:
        fail()
    else:
        _compare_elements(name, index, elements)


def test_single() -> None:
    """Test for base name of file including only single split identifier."""
    name: str = "file"
    index: int = 1

    _compare_base_name(
        name, index, BaseNameElements().split_name(_get_base_name(name, index))
    )


def test_multiple() -> None:
    """Test for base name of file including several same split identifier."""
    name: str = _get_name(["group", "type"])
    index: int = 1

    _compare_base_name(
        name, index, BaseNameElements().split_name(_get_base_name(name, index))
    )


def test_index() -> None:
    """Test for base name of file, but it doesn't include index string."""
    name: str = "file"

    assert BaseNameElements().split_name(name) is None


def test_option() -> None:
    """Test for index string including option characters."""
    name: str = "file"
    index: int = 1

    _compare_base_name(
        name,
        index,
        BaseNameElements().split_name(_get_base_name_option(name, index)),
    )


def test_digit() -> None:
    """Test for base name of file including 4 digit index text."""
    name: str = "file"
    index: int = 1

    _compare_base_name(
        name,
        index,
        BaseNameElements().split_name(_get_base_name_digit(name, index)),
    )


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_single()
    test_multiple()
    test_index()
    test_option()
    test_digit()
    return True