#!/usr/bin/env python

"""Module to represent string list about alphabets and numbers, and others."""

from typing import TypedDict

from pyspartalib.context.default.string_context import Strs


class CharacterTable(TypedDict):
    """Class to represent string list about alphabets and numbers, and others.

    It's used for renaming file or e-mail addresses.
    """

    upper: Strs
    lower: Strs
    number: Strs
    other: Strs
