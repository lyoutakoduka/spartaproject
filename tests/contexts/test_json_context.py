#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _check_type_structure() -> bool:
    return True


def test_safe() -> None:
    assert _check_type_structure()


def test_type() -> None:
    assert _check_type_structure()


def main() -> bool:
    test_safe()
    test_type()
    return True
