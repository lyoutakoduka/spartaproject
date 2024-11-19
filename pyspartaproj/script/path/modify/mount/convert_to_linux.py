#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.path.modify.mount.build_linux_path import (
    build_linux_path,
)
from pyspartaproj.script.path.modify.mount.shared.has_linux_head import (
    has_linux_head,
)


def _get_relative_strings(path: Path) -> Strs:
    return list(path.parts)


def _get_drive_letter(path: Path) -> str:
    return _get_relative_strings(path)[0][0]


def _get_relative_root(path: Path) -> Path:
    return Path(*_get_relative_strings(path)[1:])


def convert_to_linux(path: Path) -> Path:
    if has_linux_head(path):
        return path

    return build_linux_path(_get_drive_letter(path), _get_relative_root(path))
