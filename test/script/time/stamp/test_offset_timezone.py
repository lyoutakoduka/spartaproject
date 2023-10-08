#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.extension.time_context import datetime
from pyspartaproj.script.time.stamp.offset_timezone import offset_time


def _common_text(input: str) -> None:
    input_utc: str = "2023-04-15T20:09:30.936886+00:00"
    input_utc: datetime = datetime.fromisoformat(input_utc)

    assert input_utc == offset_time(datetime.fromisoformat(input))


def test_timezone() -> None:
    input_jst: str = "2023-04-16T05:09:30.936886+09:00"
    _common_text(input_jst)


def test_lost() -> None:
    input_lost: str = "2023-04-15T20:09:30.936886"
    _common_text(input_lost)


def main() -> bool:
    test_timezone()
    test_lost()
    return True
