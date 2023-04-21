#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.same_elements import all_true


def test() -> bool:
    assert all_true([
        0 == 0,
        '1' == '1',
        True == True,
        2.0 == 2.0,
    ])

    return True
