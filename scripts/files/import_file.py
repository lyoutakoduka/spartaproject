#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def _file_import(path: Path) -> bytes:
    with open(path, 'rb') as file:
        content: bytes = file.read()
        return content.replace(b'\r\n', b'\n')


def byte_import(import_path: Path) -> bytes:
    return _file_import(import_path)


def text_import(import_path: Path) -> str:
    byte: bytes = _file_import(import_path)
    return byte.decode('utf-8')
