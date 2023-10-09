#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.extension.time_context import datetime
from pyspartaproj.script.time.stamp.offset_timezone import offset_time


def _common_text(source_time: str) -> None:
    expected_utc: str = "2023-04-15T20:09:30.936886+00:00"
    expected: datetime = datetime.fromisoformat(expected_utc)

    assert expected == offset_time(datetime.fromisoformat(source_time))


def test_timezone() -> None:
    source_jst: str = "2023-04-16T05:09:30.936886+09:00"
    _common_text(source_jst)


def test_lost() -> None:
    source_lost: str = "2023-04-15T20:09:30.936886"
    _common_text(source_lost)


def main() -> bool:
    test_timezone()
    test_lost()
    return True
