#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from typing import List

from scripts.same_bools import pair_true

_Bools = List[bool]


def test_size() -> None:
    with pytest.raises(ValueError, match='size'):
        pair_true([True], [True, False])


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        pair_true([], [])


def test_pass() -> None:
    assert pair_true([True, False], [True, False])


def main() -> bool:
    test_pass()
    return True
