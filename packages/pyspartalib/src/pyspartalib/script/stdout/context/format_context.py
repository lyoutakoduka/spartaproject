#!/usr/bin/env python

from typing import TypedDict


class FormatPair(TypedDict):
    text: str
    count: int


FormatPairs = list[FormatPair]
