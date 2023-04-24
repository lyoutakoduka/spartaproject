#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.times.offset_timezone import offset_time


def test_pass() -> None:
    INPUT_UTC: str = '2023-04-15T20:09:30.936886+00:00'
    INPUT_JST: str = '2023-04-16T05:09:30.936886+09:00'

    utc: str = offset_time(INPUT_UTC)
    utc_converted: str = offset_time(INPUT_JST)

    assert utc == utc_converted


def main() -> bool:
    test_pass()
    return True
