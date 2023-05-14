#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
from pathlib import Path
from configparser import ConfigParser

from contexts.config_context import Config
from scripts.files.export_file import text_export


def config_dump(content: Config) -> str:
    config = ConfigParser()
    config.read_dict(content)

    with StringIO() as file:
        config.write(file)
        test: str = file.getvalue()
        return test.strip()


def config_export(export_path: Path, content: Config) -> Path:
    return text_export(export_path, config_dump(content))
