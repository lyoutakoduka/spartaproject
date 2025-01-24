#!/usr/bin/env python

"""User defined types using class "TypedDict"."""

from typing import TypedDict

from pyspartalib.context.default.string_context import Strs


class BaseName(TypedDict):
    """Class to represent elements for base name of file.

    It's used for the base name including index string.
    """

    name: str
    index: int


class CharacterTable(TypedDict):
    """Class to represent 3 types list about alphabets and numbers, and others.

    It's used for renaming file or e-mail addresses.
    """

    upper: Strs
    lower: Strs
    number: Strs
    other: Strs
