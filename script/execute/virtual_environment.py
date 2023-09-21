#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from platform import python_version
from sys import executable

from spartaproject.context.default.integer_context import Ints
from spartaproject.context.default.string_context import Strs
from spartaproject.script.execute.execute_command import execute_command
from spartaproject.script.execute.script_version import get_version_name


def _filter_execute_version(module_path: Path) -> bool:
    results: Strs = execute_command([str(module_path), '-V'])
    version_test: str = results[0]
    version_tests = version_test.split(' ')

    return python_version() == version_tests[-1]


def _build_success(module_path: Path) -> bool:
    return _filter_execute_version(module_path)


def _set_version(versions: Ints) -> str:
    if 0 == len(versions):
        versions = [3, 11, 5]

    return get_version_name(versions)


def _get_module_root(versions: Ints) -> Path:
    execute: Path = Path(executable)
    return Path(execute.parents[1], _set_version(versions))


def virtual_environment(environment_root: Path) -> bool:
    versions: Ints = []
    module_root: Path = _get_module_root(versions)
    module_path: Path = Path(module_root, 'python.exe')

    execute_command([str(module_path), '-m', 'venv', str(environment_root)])
    return _build_success(module_path)
