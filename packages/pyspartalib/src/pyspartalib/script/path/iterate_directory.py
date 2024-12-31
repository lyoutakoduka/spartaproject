#!/usr/bin/env python

"""Module to get list of contents in the directory you select."""

from pathlib import Path

from pyspartalib.context.extension.path_context import PathGene


def _create_filter(
    depth: int,
    file: bool,
    directory: bool,
    suffix: str,
) -> str:
    if not file and not directory:
        return ""

    glob_filter = "*/" * (depth - 1) if depth > 0 else "**/"

    if file and directory:
        glob_filter += "*"

    if file and not directory:
        glob_filter += "*." + suffix

    if not file and directory:
        glob_filter += "*/"

    return glob_filter


def _iterate_tree(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = "*",
    glob_filter: str | None = None,
) -> PathGene:
    default_filter: str = "**/*"

    if glob_filter is None:
        glob_filter = default_filter

    if default_filter == glob_filter:
        glob_filter = _create_filter(depth, file, directory, suffix)

    if len(glob_filter) > 0:
        for path in root.glob(glob_filter):
            if root != path:
                yield path


def walk_iterator(
    root: Path,
    depth: int = 0,
    file: bool = True,
    directory: bool = True,
    suffix: str = "*",
    glob_filter: str | None = None,
) -> PathGene:
    """Get list of contents in the directory you search.

    Args:
        root (Path): Path of directory you  want to get contents.

        depth (int, optional): Defaults to 0.
            Additional depth of directory hierarchy which you want to search.
            Only surface in the directory is searched if it's 0.

        file (bool, optional): Defaults to True.
            Search file. If it's False, Ignore file when search.

        directory (bool, optional): Defaults to True.
            Search directory. If it's False, Ignore directory when search.

        suffix (str, optional): Defaults to "*".
            Filter by file extension.
            If it's "*", all type files become search target.

        glob_filter (str, optional): Defaults to default_filter.
            String used for glob filter.
            If it's not default, following argument are ignored.
            ("depth", "file", "directory", and "suffix")

    Returns:
        PathGene: Path generator, not list of Path.

    Yields:
        Iterator[PathGene]: Path of file or directory found by search.

    """
    yield from _iterate_tree(root, depth, file, directory, suffix, glob_filter)
