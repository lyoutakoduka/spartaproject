#!/usr/bin/env python

"""Module to represent single frame information in stack frames."""

from pathlib import Path
from typing import TypedDict


class StackFrame(TypedDict):
    """Class to represent single frame information in stack frames."""

    file: Path
    function: str
    line: int


StackFrames = list[StackFrame]
