#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.path.modify.get_relative import get_relative


def get_file() -> Path:
    return get_relative(Path(__file__))
