#!/usr/bin/env python

"""Module to create temporary files and directories tree."""

from pathlib import Path

from pyspartalib.context.default.string_context import StrPair2, Strs
from pyspartalib.script.directory.create_directory import (
    create_directory_array,
)
from pyspartalib.script.file.config.export_config import config_export
from pyspartalib.script.file.json.export_json import Json, json_export
from pyspartalib.script.file.text.export_file import text_export


def _get_text(weight: int, index_digit: int, line_text: str) -> Strs:
    return [str(i).zfill(index_digit) + line_text for i in range(weight)]


def _sample_text(root: Path, weight: int) -> None:
    line_width: int = 10
    index_digit: int = len(str(weight))
    line_text: str = "-" * (line_width - index_digit)

    source: str = "\n".join(_get_text(weight, index_digit, line_text))

    text_export(Path(root, "file.txt"), source)


def _sample_config(root: Path, weight: int) -> None:
    width: int = 10
    section_digit: int = len(str(weight))
    line_text: str = "-" * width

    source_pairs: StrPair2 = {
        str(i).zfill(section_digit): {
            str(j).zfill(section_digit): line_text for j in range(weight)
        }
        for i in range(weight)
    }

    config_export(Path(root, "file.ini"), source_pairs)


def _sample_json(root: Path, weight: int) -> None:
    width: int = 10
    section_digit: int = len(str(weight))
    line_text: str = "-" * width

    def function(count: int) -> Json:
        if count > 0:
            return {
                str(i).zfill(section_digit): function(count - 1)
                for i in range(weight)
            }

        return line_text

    json_export(Path(root, "file.json"), function(weight))


def _recursive_tree(
    root: Path,
    tree_deep: int,
    deep: int,
    weight: int,
) -> None:
    create_directory_array([root, Path(root, "empty")])

    _sample_text(root, weight)
    _sample_config(root, weight)
    _sample_json(root, weight)

    if deep > 1:
        directory_name: Path = Path(
            root,
            "dir" + str(tree_deep - deep + 1).zfill(3),
        )
        _recursive_tree(directory_name, tree_deep, deep - 1, weight)


def _inside_span(tree_deep: int) -> bool:
    max_deep: int = 10
    return 1 <= tree_deep <= max_deep


def create_temporary_tree(
    root_path: Path,
    tree_deep: int = 1,
    tree_weight: int = 1,
) -> Path:
    """Create temporary files and directories tree.

    Args:
        root_path (Path): Path of directory that the temporary tree is created.

        tree_deep (int, optional): Defaults to 1.
            Count of hierarchy of the temporary tree.

        tree_weight (int, optional): Defaults to 1.
            Scale of file size which is placed on the temporary tree.

    Returns:
        Path: "root_path" is returned.

    """
    enable_deep: bool = _inside_span(tree_deep)
    enable_weight: bool = _inside_span(tree_weight)

    if enable_deep and enable_weight:
        _recursive_tree(root_path, tree_deep, tree_deep, tree_weight)

    return root_path
