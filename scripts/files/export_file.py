#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def byte_export(export_path: Path, content: bytes) -> Path:
    with open(export_path, 'wb') as file:
        file.write(content)
    return export_path


def text_export(export_path: Path, content: str) -> Path:
    content = content.replace('\r\n', '\n')
    return byte_export(export_path, content.encode('utf-8'))
