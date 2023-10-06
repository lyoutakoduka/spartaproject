#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.string.find_encoding import find_encoding


def byte_import(import_path: Path) -> bytes:
    with open(import_path, "rb") as file:
        return file.read()


def text_import(import_path: Path) -> str:
    byte: bytes = byte_import(import_path)
    content: str = byte.decode(find_encoding(byte))
    return content.replace("\r\n", "\n")
