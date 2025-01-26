#!/usr/bin/env python

"""Module to represent elements for base name of file."""

from typing import TypedDict


class BaseName(TypedDict):
    """Class to represent elements for base name of file.

    It's used for the base name including index string.
    """

    name: str
    index: int
