#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_command import execute_command


def get_version_name(versions: str) -> str:
    return "python".capitalize() + "-" + versions


def execute_version(executable: Path) -> str:
    return execute_command([str(executable), "-V"])[0]
