#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict, Generator
from pathlib import Path

PathGene = Generator[Path, None, None]
PathPair = Dict[str, Path]
Paths = List[Path]

PathPair2 = Dict[str, PathPair]
Paths2 = List[Paths]
