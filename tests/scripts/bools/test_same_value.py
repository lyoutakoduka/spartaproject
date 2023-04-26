#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import raises

from scripts.bools.same_value import bool_same_array, bool_same_pair


def test_empty() -> None:
    with raises(ValueError, match='empty'):
        bool_same_array([])


def test_mixed() -> None:
    with raises(ValueError, match='true_false'):
        bool_same_array([False, True, False])


def test_false() -> None:
    with raises(ValueError, match='false'):
        bool_same_array([False, False, False])


def test_array() -> None:
    assert bool_same_array([True, True, True])


def test_invert() -> None:
    assert bool_same_array([False, False, False], invert=True)


def test_pair() -> None:
    assert bool_same_pair({'R': True, 'G': True, 'B': True})


def main() -> bool:
    test_array()
    test_invert()
    test_pair()
    return True
