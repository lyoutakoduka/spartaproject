#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from typing import List

from scripts.bools.same_pair import bool_same_pair

_Bools = List[bool]


def test_size() -> None:
    with pytest.raises(ValueError, match='size'):
        bool_same_pair([True], [True, False])


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        bool_same_pair([], [])


def test_pass() -> None:
    assert bool_same_pair([True, False], [True, False])


def main() -> bool:
    test_pass()
    return True
