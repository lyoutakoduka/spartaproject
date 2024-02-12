#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to export data used for configuration file."""

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


def _cleanup_key(text: str) -> str:
    return text.strip()


def _cleanup_key_default(source_config: Config) -> Config:
    return {
        _cleanup_key(section_key): {
            _cleanup_key(key): value for key, value in section.items()
        }
        for section_key, section in source_config.items()
    }


def config_dump(source_config: Config, compress: bool = False) -> str:
    """Function to convert data used for configuration file to text.

    Return following triple quoted text if argument "source_config" is...

    {"flags": {"bool": True}, "indies": {"int": 1}}

    '''
    [flags]
    bool = True

    [indies]
    int = 1
    '''

    Args:
        source_config (Config):
            Data used for configuration file you want to convert.

        compress (bool, optional): Defaults to False.
            Return following triple quoted text if argument "compress" is True.

            '''
            [flags]
            bool=True
            [indies]
            int=1
            '''

    Returns:
        str: Converted text used for configuration file.
    """
    cleanup = _cleanup_key_default(source_config)

    config = ConfigParser()
    config.read_dict(cleanup)

    with StringIO() as file:
        config.write(file)
        text: str = _cleanup_text_default(file.getvalue())
        return _cleanup_text(text) if compress else text


def config_export(
    export_path: Path, source_config: Config, compress: bool = False
) -> Path:
    """Function to export data used for configuration file.

    Args:
        export_path (Path): Path which is used for exporting data.

        source_config (Config):
            Data used for configuration file you want to export.

        compress (bool, optional): Defaults to False.
            True if you want to export small and obfuscated text.
            It's used for argument "compress" of function "config_dump".

    Returns:
        Path: Path of data which is finally exported.
    """
    return text_export(
        export_path, config_dump(source_config, compress=compress)
    )
