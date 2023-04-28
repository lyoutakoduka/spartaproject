#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
from configparser import ConfigParser

from contexts.path_context import Path
from contexts.config_context import Config


def _export_text(path: Path, content: str) -> None:
    with open(path, 'w') as file:
        file.write(content)


def config_dump(content: Config) -> str:
    config = ConfigParser()
    config.read_dict(content)

    with StringIO() as file:
        config.write(file)
        test: str = file.getvalue()
        return test.strip()


def config_export(export_path: Path, content: Config) -> None:
    _export_text(export_path, config_dump(content))
