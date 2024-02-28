#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_file_size(path: Path) -> int:
    return path.stat().st_size
