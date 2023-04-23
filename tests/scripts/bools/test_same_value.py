#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from scripts.bools.same_value import bool_same_array, bool_same_pair


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        bool_same_array([])


def test_mixed() -> None:
    with pytest.raises(ValueError, match='true and false'):
        bool_same_array([False, True, False])


def test_false() -> None:
    with pytest.raises(ValueError, match='false'):
        bool_same_array([False, False, False])


def test_array() -> None:
    assert bool_same_array([True, True, True])


def test_pair() -> None:
    assert bool_same_pair({'R': True, 'G': True, 'B': True})


def main() -> bool:
    test_array()
    test_pair()
    return True
