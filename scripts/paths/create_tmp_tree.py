#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
from configparser import ConfigParser

from contexts.string_context import Strs, StrPair2
from contexts.path_context import Path
from scripts.files.export_json import json_export, Json
from scripts.paths.create_directory import path_mkdir

_LIST_SAMPLE: Strs = ['line' + str(i) for i in range(3)]
_DICT_SAMPLE: StrPair2 = {
    'section': {'option' + str(i): str(i) for i in range(3)}
}

_NAME: str = 'file'


def _write_text(root: Path, format: str, content: str) -> None:
    path: Path = Path(root, '.'.join(['file', format]))
    with open(path, 'w') as file:
        file.write(content)


def _sample_text(root: Path) -> None:
    _write_text(root, 'txt', '\n'.join(_LIST_SAMPLE))


def _sample_config(root: Path) -> None:
    config = ConfigParser()
    config.read_dict(_DICT_SAMPLE)

    with StringIO() as file:
        config.write(file)
        _write_text(root, 'ini', file.getvalue())


def _sample_json(root: Path) -> None:
    INPUT: Json = {
        'section': {'option' + str(i): str(i) for i in range(3)}
    }
    json_export(Path(root, _NAME + '.json'), INPUT)


def _recursive_tree(root: Path, tree_deep: int, deep: int):
    path_mkdir(root)
    path_mkdir(Path(root, 'empty'))
    _sample_text(root)
    _sample_config(root)
    _sample_json(root)

    if 1 < deep:
        directory_name: Path = Path('dir' + str(tree_deep - deep + 1).zfill(3))
        _recursive_tree(Path(root, directory_name), tree_deep, deep - 1)


def create_tree(root_path: Path, tree_deep: int = 1) -> None:
    if 1 <= tree_deep <= 10:
        _recursive_tree(root_path, tree_deep, tree_deep)
