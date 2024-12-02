#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to create empty temporary file as json format."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.extension.path_context import PathFunc
from pyspartaproj.script.path.temporary.create_temporary_file import (
    create_temporary_file,
)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_file() -> None:
    """Test to create empty temporary file as json format."""

    def individual_test(temporary_root: Path) -> None:
        file_path: Path = create_temporary_file(temporary_root)

        assert file_path.exists()
        assert file_path == Path(temporary_root, "temporary.json")

    _inside_temporary_directory(individual_test)
