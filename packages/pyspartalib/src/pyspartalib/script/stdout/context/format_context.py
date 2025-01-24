#!/usr/bin/env python

"""Module to represent string with white space character."""

from typing import TypedDict


class FormatPair(TypedDict):
    """Class to represent string with white space character."""

    text: str
    count: int


FormatPairs = list[FormatPair]
