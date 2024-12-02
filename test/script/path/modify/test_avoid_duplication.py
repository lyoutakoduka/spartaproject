#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to convert path to avoid existing path."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartaproj.context.extension.path_context import PathFunc
from pyspartaproj.script.file.json.export_json import json_export
from pyspartaproj.script.path.modify.avoid_duplication import get_avoid_path


def _common_test(source_path: Path, destination_path: Path) -> None:
    assert source_path == destination_path


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path, "temporary.json"))


def test_exists() -> None:
    """Test to convert path to avoid existing path."""

    def individual_test(source_path: Path) -> None:
        source_path = json_export(source_path, "test")
        _common_test(
            get_avoid_path(source_path),
            source_path.with_stem(source_path.stem + "_"),
        )

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    """Test to convert path, but no path competition."""

    def individual_test(source_path: Path) -> None:
        _common_test(get_avoid_path(source_path), source_path)

    _inside_temporary_directory(individual_test)
