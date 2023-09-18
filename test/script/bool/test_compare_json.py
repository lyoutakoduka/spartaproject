#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spartaproject.script.bool.compare_json import is_same_json


def test_pass() -> None:
    assert is_same_json({'A': True}, {'A': True})


def test_nest() -> None:
    assert is_same_json({'A': {'B': True}}, {'A': {'B': True}})


def test_multiple() -> None:
    assert is_same_json({'A': True, 'B': False}, {'B': False, 'A': True})


def test_array() -> None:
    assert is_same_json({'A': ['B', 'C']}, {'A': ['B', 'C']})


def test_type() -> None:
    for input in [None, True, 0, 0.1, 'test']:
        assert is_same_json(input, input)


def main() -> bool:
    test_pass()
    test_nest()
    test_multiple()
    test_array()
    test_type()
    return True
