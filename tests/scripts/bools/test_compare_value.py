#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from scripts.bools.compare_value import bool_compare_array, bool_compare_pair


def test_size() -> None:
    with pytest.raises(ValueError, match='size'):
        bool_compare_array([True], [True, False])


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        bool_compare_array([], [])


def test_key() -> None:
    with pytest.raises(KeyError, match='unmatch'):
        bool_compare_pair(
            {'R': False, 'G': True, 'B': True},
            {'R': True, 'error': False, 'B': True},
        )


def test_array() -> None:
    assert bool_compare_array([True, False], [True, False])


def test_pair() -> None:
    assert bool_compare_pair(
        {'R': True, 'G': False, 'B': True},
        {'R': True, 'G': False, 'B': True},
    )


def main() -> bool:
    test_array()
    test_pair()
    return True
