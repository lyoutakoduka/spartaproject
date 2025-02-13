#!/usr/bin/env python

from pathlib import Path
from typing import TypedDict


class SymbolicLink(TypedDict):
    source: Path
    symbolic: Path
