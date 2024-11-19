#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs


def _get_relative_strings(path: Path) -> Strs:
    return list(path.parts)


def _get_drive_letter(path: Path) -> str:
    return _get_relative_strings(path)[0][0]


def _get_relative_root(path: Path) -> Path:
    return Path(*_get_relative_strings(path)[1:])
