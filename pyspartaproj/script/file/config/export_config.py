#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from io import StringIO
from pathlib import Path

from pyspartaproj.context.file.config_context import Config
from pyspartaproj.script.file.text.export_file import text_export


def _cleanup_text(text: str) -> str:
    text = text.strip()
    text = text.replace("\n" * 2, "\n")
    return text.replace(" = ", "=")


def _cleanup_text_default(text: str) -> str:
    if text.endswith("\n" * 2):
        return text[:-1]

    return text


def _cleanup(text: str) -> str:
    return text.strip()


def _cleanup_key_default(input: Config) -> Config:
    return {
        _cleanup(section_key): {
            _cleanup(key): value for key, value in section.items()
        }
        for section_key, section in input.items()
    }


def config_dump(input: Config, compress: bool = False) -> str:
    input = _cleanup_key_default(input)

    config = ConfigParser()
    config.read_dict(input)

    with StringIO() as file:
        config.write(file)
        text: str = _cleanup_text_default(file.getvalue())
        return _cleanup_text(text) if compress else text


def config_export(
    export_path: Path, input: Config, compress: bool = False
) -> Path:
    return text_export(export_path, config_dump(input, compress=compress))
