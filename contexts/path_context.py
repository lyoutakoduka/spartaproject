#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict, Generator
from pathlib import Path

Paths = List[Path]
PathPair = Dict[str, Path]
Paths2 = List[Paths]
PathPair2 = Dict[str, PathPair]
PathGene = Generator[Path, None, None]
