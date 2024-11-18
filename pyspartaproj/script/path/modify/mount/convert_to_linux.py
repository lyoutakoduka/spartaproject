#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs


def _get_relative_strings(path: Path) -> Strs:
    return list(path.parts)
