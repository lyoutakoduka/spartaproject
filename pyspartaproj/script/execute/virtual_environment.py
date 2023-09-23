#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from sys import executable

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.execute.execute_command import execute_command
from pyspartaproj.script.execute.script_version import (execute_version,
                                                         get_version_name)


def _filter_execute_version(source_path: Path, destination_path: Path) -> bool:
    return 1 == len(set([
        str(execute_version(path))
        for path in [source_path, destination_path]
    ]))


def _build_success(source_path: Path, destination_path: Path) -> bool:
    return _filter_execute_version(source_path, destination_path)


def _set_version(versions: Ints) -> str:
    if 0 == len(versions):
        versions = [3, 11, 5]

    return get_version_name(versions)


def _get_module_root(versions: Ints) -> Path:
    execute: Path = Path(executable)
    return Path(execute.parents[1], _set_version(versions))


def _get_execute_path(environment_root: Path, name: str) -> Path:
    return Path(
        environment_root,
        'scripts'.capitalize(),
        name + '.exe'
    )


def virtual_environment(
    environment_root: Path, versions: Ints = [], modules: Strs = []
) -> bool:
    source_path: Path = Path(_get_module_root(versions), 'python.exe')

    execute_command([str(source_path), '-m', 'venv', str(environment_root)])

    return _build_success(
        source_path, _get_execute_path(environment_root, 'python')
    )
