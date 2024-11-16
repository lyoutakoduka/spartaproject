#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _convert_windows(identifier: str) -> Path:
    return Path(identifier.capitalize() + ":")
