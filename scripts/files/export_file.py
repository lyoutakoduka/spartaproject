#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _file_export(path: Path, content: str | bytes, byte: bool = False) -> None:
    type: str = 'wb' if byte else 'w'

    with open(path, type) as file:
        file.write(content)


def byte_export(export_path: Path, content: bytes) -> None:
    _file_export(export_path, content, byte=True)


def text_export(export_path: Path, content: str) -> None:
    _file_export(export_path, content)
