#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def byte_export(export_path: Path, content: bytes) -> None:
    with open(export_path, 'wb') as file:
        file.write(content)


def text_export(export_path: Path, content: str) -> None:
    content = content.replace('\r\n', '\n')
    byte_export(export_path, content.encode('utf-8'))
