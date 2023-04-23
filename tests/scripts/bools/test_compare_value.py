#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from typing import List

from scripts.bools.compare_value import bool_compare_array

_Bools = List[bool]


def test_size() -> None:
    with pytest.raises(ValueError, match='size'):
        bool_compare_array([True], [True, False])


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        bool_compare_array([], [])


def test_pass() -> None:
    assert bool_compare_array([True, False], [True, False])


def main() -> bool:
    test_pass()
    return True
