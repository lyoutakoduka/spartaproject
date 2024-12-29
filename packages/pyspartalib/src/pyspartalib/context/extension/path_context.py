#!/usr/bin/env python

"""User defined types about type "Path"."""

from collections.abc import Callable, Generator
from pathlib import Path

PathGene = Generator[Path]
PathPair = dict[str, Path]
Paths = list[Path]
PathFunc = Callable[[Path], None]
PathBoolFunc = Callable[[Path], bool]

PathGeneFunc = Callable[[], PathGene]
PathPair2 = dict[str, PathPair]
Paths2 = list[Paths]
PathsPair = dict[str, Paths]

Paths3 = list[Paths2]
