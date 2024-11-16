#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _get_drive_letter() -> str:
    return "c"


def _get_relative_root() -> Path:
    return Path("root", "body", "head")
