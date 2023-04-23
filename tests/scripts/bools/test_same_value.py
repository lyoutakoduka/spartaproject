#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from scripts.bools.same_value import bool_same_array


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        bool_same_array([])


def test_mixed() -> None:
    with pytest.raises(ValueError, match='true and false'):
        bool_same_array([False, True, False])


def test_false() -> None:
    with pytest.raises(ValueError, match='false'):
        bool_same_array([False, False, False])


def test_pass() -> None:
    assert bool_same_array([True, True, True])


def main() -> bool:
    test_pass()
    return True
