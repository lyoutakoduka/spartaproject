#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.current.get_relative import get_relative
from pyspartaproj.script.path.modify.mount.get_linux_head import get_linux_head


def get_linux_relative(path: Path) -> Path:
    return get_relative(path, root_path=get_linux_head())
