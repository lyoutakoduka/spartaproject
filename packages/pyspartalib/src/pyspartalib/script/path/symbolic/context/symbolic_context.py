#!/usr/bin/env python

"""Module to represent paths about symbolic link."""

from pathlib import Path
from typing import TypedDict


class SymbolicLink(TypedDict):
    """Class to represent paths about symbolic link."""

    source: Path
    symbolic: Path
