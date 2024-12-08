#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Callable

from pyspartaproj.script.path.safe.safe_copy import SafeCopy

CopyPathFunc = Callable[[SafeCopy, Path], None]
