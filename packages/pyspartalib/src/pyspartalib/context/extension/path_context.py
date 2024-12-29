#!/usr/bin/env python

"""User defined types about type "Path"."""

from pathlib import Path
from typing import Callable, Dict, Generator, List

PathGene = Generator[Path, None, None]
PathPair = Dict[str, Path]
Paths = List[Path]
PathFunc = Callable[[Path], None]
PathBoolFunc = Callable[[Path], bool]

PathGeneFunc = Callable[[], PathGene]
PathPair2 = Dict[str, PathPair]
Paths2 = List[Paths]
PathsPair = Dict[str, Paths]

Paths3 = List[Paths2]
