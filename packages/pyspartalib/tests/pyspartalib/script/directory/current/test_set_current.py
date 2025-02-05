#!/usr/bin/env python

from pathlib import Path


def _get_current() -> Path:
    return Path().cwd()
