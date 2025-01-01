#!/usr/bin/env python

"""Module to create temporary files and directories tree."""

from pathlib import Path

from pyspartalib.context.default.string_context import StrPair, StrPair2, Strs
from pyspartalib.script.directory.create_directory import (
    create_directory_array,
)
from pyspartalib.script.file.config.export_config import config_export
from pyspartalib.script.file.json.export_json import Json, json_export
from pyspartalib.script.file.text.export_file import text_export


def _fill_index(index: int, digit: int) -> str:
    return str(index).zfill(digit)


def _get_file_path(file_root: Path, file_suffix: str) -> Path:
    return Path(file_root, "file").with_suffix("." + file_suffix)


def _get_index_digit(weight: int) -> int:
    return len(str(weight))


def _get_line(index_digit: int) -> str:
    line_width: int = 10
    return "-" * (line_width - index_digit)


def _get_text(weight: int, index_digit: int, line_text: str) -> Strs:
    return [_fill_index(i, index_digit) + line_text for i in range(weight)]


def _get_text_config(
    weight: int,
    section_digit: int,
    line_text: str,
) -> StrPair:
    return {_fill_index(i, section_digit): line_text for i in range(weight)}


def _merged_text(weight: int, index_digit: int, line_text: str) -> str:
    return "\n".join(_get_text(weight, index_digit, line_text))


def _sample_text(root: Path, weight: int) -> None:
    index_digit: int = _get_index_digit(weight)

    text_export(
        _get_file_path(root, "txt"),
        _merged_text(weight, index_digit, _get_line(index_digit)),
    )


def _sample_config(root: Path, weight: int) -> None:
    section_digit: int = _get_index_digit(weight)
    line_text: str = _get_line(0)

    source_pairs: StrPair2 = {
        _fill_index(i, section_digit): _get_text_config(
            weight,
            section_digit,
            line_text,
        )
        for i in range(weight)
    }

    config_export(_get_file_path(root, "ini"), source_pairs)


def _sample_json(root: Path, weight: int) -> None:
    section_digit: int = _get_index_digit(weight)
    line_text: str = _get_line(0)

    def function(count: int) -> Json:
        if count > 0:
            return {
                _fill_index(i, section_digit): function(count - 1)
                for i in range(weight)
            }

        return line_text

    json_export(_get_file_path(root, "json"), function(weight))


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
            "dir" + _fill_index(tree_deep - deep + 1, 3),
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
