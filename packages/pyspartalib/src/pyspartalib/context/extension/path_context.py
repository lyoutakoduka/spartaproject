#!/usr/bin/env python

"""User defined types about type "Path"."""

from pathlib import Path
from typing import Callable, Generator

PathGene = Generator[Path, None, None]
PathPair = dict[str, Path]
Paths = list[Path]
PathFunc = Callable[[Path], None]
PathBoolFunc = Callable[[Path], bool]

PathGeneFunc = Callable[[], PathGene]
PathPair2 = dict[str, PathPair]
Paths2 = list[Paths]
PathsPair = dict[str, Paths]

Paths3 = list[Paths2]
