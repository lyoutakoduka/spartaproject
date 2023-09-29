#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from io import StringIO
from pathlib import Path

from pyspartaproj.context.file.config_context import Config
from pyspartaproj.script.file.text.export_file import text_export


def _cleanup_text(text: str, compress: bool) -> str:
    text = text.strip()

    if not compress:
        return text

    text = text.replace("\n" * 2, "\n")
    return text.replace(" = ", "=")


def config_dump(input: Config, compress: bool = False) -> str:
    config = ConfigParser()
    config.read_dict(input)

    with StringIO() as file:
        config.write(file)
        return _cleanup_text(file.getvalue(), compress)


def config_export(
    export_path: Path, input: Config, compress: bool = False
) -> Path:
    return text_export(export_path, config_dump(input, compress=compress))
