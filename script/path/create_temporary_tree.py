#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from context.default.string_context import StrPair2
from script.directory.create_directory import create_directory_array
from script.file.export_config import config_export
from script.file.export_file import text_export
from script.file.json.export_json import json_export, Json

_NAME: str = 'file'


def _sample_text(root: Path, weight: int) -> None:
    line_width: int = 10
    index_order: int = len(str(weight))
    line_text: str = '-' * (line_width - index_order)

    INPUT: str = '\n'.join([
        str(i).zfill(index_order) + line_text for i in range(weight)
    ])

    text_export(Path(root, _NAME + '.txt'), INPUT)


def _sample_config(root: Path, weight: int) -> None:
    width: int = 10
    section_order: int = len(str(weight))
    line_text: str = '-' * width

    INPUT: StrPair2 = {
        str(i).zfill(section_order): {
            str(j).zfill(section_order): line_text for j in range(weight)
        }
        for i in range(weight)
    }

    config_export(Path(root, _NAME + '.ini'), INPUT)


def _sample_json(root: Path, weight: int) -> None:
    width: int = 10
    section_order: int = len(str(weight))
    line_text: str = '-' * width

    def function(count: int) -> Json:
        if 0 < count:
            return {
                str(i).zfill(section_order): function(count - 1)
                for i in range(weight)
            }
        return line_text

    json_export(Path(root, _NAME + '.json'), function(weight))


def _recursive_tree(root: Path, tree_deep: int, deep: int, weight: int):
    create_directory_array([root, Path(root, 'empty')])
    _sample_text(root, weight)
    _sample_config(root, weight)
    _sample_json(root, weight)

    if 1 < deep:
        directory_name: Path = Path(
            root, 'dir' + str(tree_deep - deep + 1).zfill(3)
        )
        _recursive_tree(directory_name, tree_deep, deep - 1, weight)


def create_temporary_tree(
    root_path: Path, tree_deep: int = 1, tree_weight: int = 1
) -> None:
    enable_deep: bool = 1 <= tree_deep <= 10
    enable_weight: bool = 1 <= tree_weight <= 10

    if enable_deep and enable_weight:
        _recursive_tree(root_path, tree_deep, tree_deep, tree_weight)
