#!/usr/bin/env python

from os import chdir
from pathlib import Path


def set_current(path: Path) -> None:
    chdir(path)
