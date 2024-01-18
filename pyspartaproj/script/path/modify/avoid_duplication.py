#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_avoid_path(path: Path) -> Path:
    while path.exists():
        path = path.with_name(path.name + "_")

    return path
