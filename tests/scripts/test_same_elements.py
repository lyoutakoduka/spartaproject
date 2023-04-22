#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from scripts.same_elements import all_true


def test_empty() -> None:
    with pytest.raises(ValueError, match='empty'):
        all_true([])


def test_mixed() -> None:
    with pytest.raises(ValueError, match='true and false'):
        all_true([False, True, False])


def test_false() -> None:
    with pytest.raises(ValueError, match='false'):
        all_true([False, False, False])


def test_pass() -> None:
    assert all_true([True, True, True])


def main() -> bool:
    test_empty()
    test_mixed()
    test_false()
    test_pass()
    return True
