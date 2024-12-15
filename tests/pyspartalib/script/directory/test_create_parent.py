#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test module to create all parent directories of the path you select."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.script.directory.create_parent import create_parent


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_directory() -> None:
    """Test to create all parent directories of the path you select."""

    def individual_test(temporary_root: Path) -> None:
        expected: Path = Path(temporary_root, "parent")
        parent_path: Path = create_parent(Path(expected, "temporary.json"))

        assert expected == parent_path
        assert parent_path.exists()

    _inside_temporary_directory(individual_test)
