#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contexts.string_context import Strs
from contexts.path_context import Path
from scripts.files.export_config import config_export, Config
from scripts.files.export_json import json_export, Json
from scripts.paths.create_directory import path_mkdir

_NAME: str = 'file'


def _sample_text(root: Path) -> None:
    line_count: int = 1
    line_width: int = 64
    line_count *= 10
    index_order: int = len(str(line_count))
    width: int = line_width - index_order
    line_text: str = '-' * width

    INPUT: str = '\n'.join([
        str(i).zfill(index_order) + line_text
        for i in range(line_count)
    ])

    with open(Path(root, _NAME + '.txt'), 'w') as file:
        file.write(INPUT)


def _sample_config(root: Path) -> None:
    INPUT: Config = {
        'section': {'option' + str(i): str(i) for i in range(3)}
    }
    config_export(Path(root, _NAME + '.ini'), INPUT)


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
