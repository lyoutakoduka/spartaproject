#!/usr/bin/env python

"""Test module to import configuration file or load configuration data."""

from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.extension.path_context import PathFunc
from pyspartalib.context.file.config_context import Config, Single
from pyspartalib.context.type_context import Type
from pyspartalib.script.file.config.import_config import (
    config_import,
    config_load,
)
from pyspartalib.script.file.text.export_file import text_export
from pyspartalib.script.string.format_texts import format_indent


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _instance_error(result: object, type_variable: type) -> object:
    if isinstance(result, type_variable):
        return result

    raise TypeError


def _get_section(formatted: str) -> Single:
    config: Config = config_load(formatted)
    return config["section"]["option"]


def _get_config_bool() -> str:
    return """
        [section]
        option=True
    """


def _get_config_integer() -> str:
    return """
        [section]
        option=1
    """


def _get_config_decimal() -> str:
    return """
        [section]
        option=1.0
    """


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


def test_bool() -> None:
    """Test to load configuration data as type boolean."""
    source: str = _get_config_bool()
    result: Single = _get_section(format_indent(source))

    _fail_error(bool(_instance_error(result, bool)))


def test_integer() -> None:
    """Test to load configuration data as type integer."""
    source: str = _get_config_integer()
    expected: int = 1

    _difference_error(_get_section(format_indent(source)), expected)


def test_decimal() -> None:
    """Test to load configuration data as type decimal."""
    source: str = _get_config_decimal()
    expected: Decimal = Decimal("1.0")

    _difference_error(_get_section(format_indent(source)), expected)


def test_string() -> None:
    """Test to load configuration data as type string."""
    source: str = """
        [section]
        option=text
    """
    expected: str = "text"

    _difference_error(_get_section(format_indent(source)), expected)


def test_path() -> None:
    """Test to load configuration data as type path."""
    source: str = """
        [section]
        path=text
    """
    expected: Path = Path("text")

    config: Config = config_load(format_indent(source))
    _difference_error(config["section"]["path"], expected)


def test_import() -> None:
    """Test to import configuration file as format "ini"."""
    source: str = """
        [section]
        option=text
    """
    expected: str = "text"

    def individual_test(temporary_root: Path) -> None:
        config: Config = config_import(
            text_export(
                Path(temporary_root, "temporary.ini"),
                format_indent(source),
            ),
        )
        _difference_error(config["section"]["option"], expected)

    _inside_temporary_directory(individual_test)
