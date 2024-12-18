#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class SafeCopy."""

from pathlib import Path
from typing import Callable

from pyspartalib.script.path.safe.safe_copy import SafeCopy

CopyPathFunc = Callable[[SafeCopy, Path], None]
