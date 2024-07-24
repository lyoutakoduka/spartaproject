#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from decimal import Decimal
from pathlib import Path

from pyspartaproj.context.default.string_context import StrsPair
from pyspartaproj.context.file.config_context import Basic, Config
from pyspartaproj.script.file.text.import_file import text_import


def _load_each_type(config: ConfigParser, section: str, option: str) -> Basic:
    for i in range(3):
        try:
            if 0 == i:
                return config.getint(section, option)
            elif 1 == i:
                return Decimal(str(config.getfloat(section, option)))
            elif 2 == i:
                return config.getboolean(section, option)
        except BaseException:
            pass

    text: str = config.get(section, option)
    return Path(text) if "path" in option else text


def config_load(source: str) -> Config:
    config = ConfigParser()
    config.read_string(source)

    key_groups: StrsPair = {
        section: config.options(section) for section in config.sections()
    }

    result_config: Config = {
        key_section: {
            key: _load_each_type(config, key_section, key) for key in key_group
        }
        for key_section, key_group in key_groups.items()
    }

    return result_config


def config_import(import_path: Path, encoding: str | None = None) -> Config:
    return config_load(text_import(import_path, encoding=encoding))
