#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def byte_export(export_path: Path, input: bytes) -> Path:
    with open(export_path, 'wb') as file:
        file.write(input)
    return export_path


def text_export(export_path: Path, input: str) -> Path:
    input = input.replace('\r\n', '\n')
    return byte_export(export_path, input.encode('utf-8'))
