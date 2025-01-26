#!/usr/bin/env python

"""Test module to import Json file or load Json data."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.file.json_context import Json, Single, SinglePair
from pyspartalib.script.file.json.export_json import json_export
from pyspartalib.script.file.json.import_json import json_import, json_load


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _pair_from_json(value_json: Json) -> SinglePair:
    if not isinstance(value_json, dict):
        return {}

    return {
        key: value
        for key, value in value_json.items()
        if isinstance(value, Single)
    }


def _common_test(expected: Single, key: str, value: str) -> None:
    _difference_error(
        _pair_from_json(json_load(f'{{"{key}": {value}}}'))[key],
        expected,
    )


def _specify_pair(expected: Single, source: str) -> None:
    _common_test(expected, "group", source)


def _export_json(path: Path, config: Json) -> Path:
    return json_export(Path(path, "temporary.ini"), config)


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_none() -> None:
    """Test to load Json data as None data."""
    expected: None = None
    _specify_pair(expected, "null")


def test_bool() -> None:
    """Test to load Json data as type boolean."""
    expected: bool = True
    _specify_pair(expected, "true")


def test_integer() -> None:
    """Test to load Json data as type integer."""
    expected: int = 1
    _specify_pair(expected, str(expected))


def test_decimal() -> None:
    """Test to load Json data as type decimal."""
    expected: float = 0.1
    _specify_pair(expected, str(expected))


def test_string() -> None:
    """Test to load Json data as type string."""
    expected: str = "test"
    _specify_pair(expected, f'"{expected}"')


def test_export() -> None:
    """Test to import Json file as format "json"."""
    expected: Json = [None, True, 1, "test"]

    def individual_test(temporary_root: Path) -> None:
        _difference_error(
            json_import(_export_json(temporary_root, expected)),
            expected,
        )

    _inside_temporary_directory(individual_test)
