#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from io import StringIO
from pathlib import Path

from contexts.config_context import Config
from scripts.files.export_file import text_export


def _cleanup_text(test: str, compress: bool) -> str:
    test = test.strip()

    if not compress:
        return test

    test = test.replace('\n' * 2, '\n')
    return test.replace(' = ', '=')


def config_dump(content: Config, compress: bool = False) -> str:
    config = ConfigParser()
    config.read_dict(content)

    with StringIO() as file:
        config.write(file)
        return _cleanup_text(file.getvalue(), compress)


def config_export(export_path: Path, content: Config, compress: bool = False) -> Path:
    return text_export(export_path, config_dump(content, compress=compress))
