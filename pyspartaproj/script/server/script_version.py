#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.shell.execute_command import execute_command


def get_version_name(version: str) -> str:
    return "python".capitalize() + "-" + version


def execute_version(executable: Path) -> str:
    return execute_command([str(executable), "-V"])[0].split(" ")[-1]
