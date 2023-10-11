#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.shell.execute_command import execute_command


def get_version_name(versions: Ints) -> str:
    return "python".capitalize() + "-" + version_to_string(versions)


def execute_version(executable: Path) -> Ints:
    results: Strs = execute_command([str(executable), "-V"])

    version_test: str = results[0]
    version_tests = version_test.split(" ")
    return version_from_string(version_tests[-1])
