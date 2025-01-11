#!/usr/bin/env python

"""Test module to convert path to avoid existing path."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.json.export_json import json_export
from pyspartalib.script.path.modify.avoid_duplication import get_avoid_path


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path, "temporary.json"))


def test_exists() -> None:
    """Test to convert path to avoid existing path."""

    def individual_test(source_path: Path) -> None:
        source_path = json_export(source_path, "test")

        _difference_error(
            get_avoid_path(source_path),
            source_path.with_stem(source_path.stem + "_"),
        )

    _inside_temporary_directory(individual_test)


def test_empty() -> None:
    """Test to convert path, but no path competition."""

    def individual_test(source_path: Path) -> None:
        _difference_error(get_avoid_path(source_path), source_path)

    _inside_temporary_directory(individual_test)
