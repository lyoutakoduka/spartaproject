#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sparta.scripts.same_elements import all_true


def test() -> None:
    result: bool = all_true([
        0 == 0,
        '1' == '1',
        True == True,
        2.0 == 2.0,
    ])

    assert result
