#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class "TypedDict"."""

from pathlib import Path
from typing import TypedDict

from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import Paths


class ArchiveStatus(TypedDict):
    """Class to represent an archive information.

    It's used for test to take out directory from inside of archive.
    """

    archive: Path
    take: Paths
    keep: Paths


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
