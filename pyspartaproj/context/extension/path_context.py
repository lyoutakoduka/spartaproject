#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types about type "Path"."""

from pathlib import Path
from typing import Dict, Generator, List

PathGene = Generator[Path, None, None]
PathPair = Dict[str, Path]
Paths = List[Path]

PathPair2 = Dict[str, PathPair]
Paths2 = List[Paths]
