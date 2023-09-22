#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def byte_import(import_path: Path) -> bytes:
    with open(import_path, 'rb') as file:
        return file.read()


def text_import(import_path: Path) -> str:
    byte: bytes = byte_import(import_path)
    content: str = byte.decode()
    return content.replace('\r\n', '\n')
