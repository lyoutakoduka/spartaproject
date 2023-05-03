#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _file_export(path: Path, content: bytes, byte: bool = False) -> None:
    with open(path, 'wb') as file:
        file.write(content)


def byte_export(export_path: Path, content: bytes) -> None:
    _file_export(export_path, content, byte=True)


def text_export(export_path: Path, content: str) -> None:
    _file_export(export_path, content.encode('utf-8'))
