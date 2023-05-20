#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from contexts.string_context import StrPair2
from scripts.files.export_config import config_export
from scripts.files.export_file import text_export
from scripts.files.export_json import json_export, Json
from scripts.paths.create_directory import path_mkdir

_NAME: str = 'file'


def _sample_text(root: Path, weight: int) -> None:
    line_width: int = 10
    index_order: int = len(str(weight))
    line_text: str = '-' * (line_width - index_order)

    INPUT: str = '\n'.join([
        str(i).zfill(index_order) + line_text
        for i in range(weight)
    ])

    text_export(Path(root, _NAME + '.txt'), INPUT)


def _sample_config(root: Path, weight: int) -> None:
    width: int = 10
    section_order: int = len(str(weight))
    line_text: str = '-' * width

    INPUT: StrPair2 = {
        str(i).zfill(section_order): {
            str(j).zfill(section_order): line_text
            for j in range(weight)
        }
        for i in range(weight)
    }

    config_export(Path(root, _NAME + '.ini'), INPUT)


def _sample_json(root: Path, weight: int) -> None:
    width: int = 10
    section_order: int = len(str(weight))
    line_text: str = '-' * width

    def func(count: int) -> Json:
        if 0 < count:
            return {
                str(i).zfill(section_order): func(count - 1)
                for i in range(weight)
            }
        return line_text

    input: Json = func(weight)

    json_export(Path(root, _NAME + '.json'), input)


def _recursive_tree(root: Path, tree_deep: int, deep: int, weight: int):
    path_mkdir(root)
    path_mkdir(Path(root, 'empty'))
    _sample_text(root, weight)
    _sample_config(root, weight)
    _sample_json(root, weight)

    if 1 < deep:
        directory_name: Path = Path('dir' + str(tree_deep - deep + 1).zfill(3))

        _recursive_tree(
            Path(root, directory_name),
            tree_deep,
            deep - 1,
            weight
        )


def create_tree(root_path: Path, tree_deep: int = 1,
                tree_weight: int = 1) -> None:
    enable_deep: bool = 1 <= tree_deep <= 10
    enable_weight: bool = 1 <= tree_weight <= 10

    if enable_deep and enable_weight:
        _recursive_tree(root_path, tree_deep, tree_deep, tree_weight)
