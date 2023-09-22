#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from spartaproject.context.default.integer_context import Ints
from spartaproject.context.default.string_context import Strs
from spartaproject.script.execute.execute_command import execute_command


def version_to_string(versions: Ints) -> str:
    return '.'.join([str(number) for number in versions])


def version_from_string(version: str) -> Ints:
    return [int(number) for number in version.split('.')]


def get_version_name(versions: Ints) -> str:
    return 'python'.capitalize() + '-' + version_to_string(versions)


def execute_version(executable: Path) -> Ints:
    results: Strs = execute_command([str(executable), '-V'])

    version_test: str = results[0]
    version_tests = version_test.split(' ')
    return version_from_string(version_tests[-1])
