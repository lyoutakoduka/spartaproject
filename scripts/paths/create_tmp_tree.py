#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
from json import dumps
from typing import List, Dict
from pathlib import Path
from configparser import ConfigParser

from scripts.paths.create_directory import path_mkdir

_Strs = List[str]
_Pair = Dict[str, str]
_PairTwo = Dict[str, _Pair]

LIST_SAMPLE: _Strs = ['line' + str(i) for i in range(3)]
DICT_SAMPLE: _PairTwo = {
    'section': {'option' + str(i): str(i) for i in range(3)}
}


def _write_text(root: Path, format: str, content: str) -> None:
    path: Path = root.joinpath('.'.join(['file', format]))
    with open(path, 'w') as file:
        file.write(content)


def _sample_text(root: Path) -> None:
    _write_text(root, 'txt', '\n'.join(LIST_SAMPLE))


def _sample_config(root: Path) -> None:
    config = ConfigParser()
    config.read_dict(DICT_SAMPLE)

    with StringIO() as file:
        config.write(file)
        _write_text(root, 'ini', file.getvalue())


def _sample_json(root: Path) -> None:
    text: str = dumps(
        DICT_SAMPLE, indent=2, ensure_ascii=False, sort_keys=True)
    _write_text(root, 'json', text)


def _recursive_tree(root: Path, tree_deep: int, deep: int):
    path_mkdir(root)
    path_mkdir(root.joinpath('empty'))
    _sample_text(root)
    _sample_config(root)
    _sample_json(root)

    if 1 < deep:
        directory_name: Path = Path('dir' + str(tree_deep - deep + 1).zfill(3))
        _recursive_tree(root.joinpath(directory_name), tree_deep, deep - 1)


def create_tree(root_path: Path, tree_deep: int = 1) -> None:
    if 1 <= tree_deep <= 10:
        _recursive_tree(root_path, tree_deep, tree_deep)
