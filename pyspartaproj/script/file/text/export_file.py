#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def byte_export(export_path: Path, source: bytes) -> Path:
    with open(export_path, "wb") as file:
        file.write(source)
    return export_path


def text_export(export_path: Path, source: str) -> Path:
    replaced = source.replace("\r\n", "\n")
    return byte_export(export_path, replaced.encode("utf-8"))
