#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import is_relative
from pyspartaproj.script.path.modify.mount.shared.get_linux_head import (
    get_linux_head,
)


def has_linux_head(path: Path) -> bool:
    return is_relative(path, root_path=get_linux_head())
