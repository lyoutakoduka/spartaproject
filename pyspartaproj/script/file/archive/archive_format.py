#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def get_format() -> str:
    return "zip"


def rename_format(path: Path) -> Path:
    return path.with_suffix("." + get_format())
