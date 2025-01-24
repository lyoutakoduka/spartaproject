#!/usr/bin/env python

"""User defined types using class "TypedDict"."""

from pathlib import Path
from typing import TypedDict


class StackFrame(TypedDict):
    """Class to represent single frame information in stack frames."""

    file: Path
    function: str
    line: int


StackFrames = list[StackFrame]
