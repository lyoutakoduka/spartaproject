#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class "TypedDict"."""

from pathlib import Path
from typing import List, TypedDict


class LinePair(TypedDict):
    """Class to represent string with white space character on head."""

    text: str
    count: int


class StackFrame(TypedDict):
    """Class to represent single frame information in stack frames."""

    file: Path
    function: str
    line: int


LinePairs = List[LinePair]
StackFrames = List[StackFrame]
