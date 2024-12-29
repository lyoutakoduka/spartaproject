#!/usr/bin/env python

"""User defined types using class SafeCopy."""

from collections.abc import Callable
from pathlib import Path

from pyspartalib.script.path.safe.safe_copy import SafeCopy

CopyPathFunc = Callable[[SafeCopy, Path], None]
