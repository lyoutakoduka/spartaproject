#!/usr/bin/env python

"""Test module to take out name and index from base name of file."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.string.rename.context.rename_context import BaseName
from pyspartalib.script.string.rename.name_elements import NameElements


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


def _not_none_error(result: object) -> None:
    if result is not None:
        raise ValueError


def _compare_name(name: str, base_name: BaseName) -> None:
    _difference_error(base_name["name"], name)


def _compare_index(index: int, base_name: BaseName) -> None:
    _difference_error(base_name["index"], index)


def _compare_elements(name: str, index: int, base_name: BaseName) -> None:
    _compare_name(name, base_name)
    _compare_index(index, base_name)


def _get_identifier() -> str:
    return "_"


def _get_name(names: Strs, identifier: str) -> str:
    return identifier.join(names)


def _get_index(index: int, digit: int) -> str:
    return str(index).zfill(digit)


def _merge_base_name(name: str, index_text: str, identifier: str) -> str:
    return name + identifier + index_text


def _get_base_name(name: str, index: int, identifier: str) -> str:
    return _merge_base_name(name, _get_index(index, 1), identifier)


def _get_base_name_option(name: str, index: int, identifier: str) -> str:
    return _merge_base_name(name, "v" + _get_index(index, 1) + "a", identifier)


def _get_base_name_digit(name: str, index: int, identifier: str) -> str:
    return _merge_base_name(name, _get_index(index, 4), identifier)


def _split_test(name: str, index: int, base_name: BaseName | None) -> None:
    _compare_elements(name, index, _none_error(base_name))


def _join_test(expected: str, name_elements: NameElements) -> None:
    _difference_error(
        name_elements.join_name(
            _none_error(name_elements.split_name(expected)),
        ),
        expected,
    )


def _split_name(text: str) -> BaseName | None:
    return NameElements().split_name(text)


def _split_name_identifier(text: str, identifier: str) -> BaseName | None:
    return NameElements(identifier=identifier).split_name(text)


def _common_test(name: str, index: int, identifier: str) -> None:
    _split_test(
        name,
        index,
        _split_name(_get_base_name(name, index, identifier)),
    )


def test_single() -> None:
    """Test for base name of file including only single split identifier."""
    identifier: str = _get_identifier()
    name: str = "file"
    index: int = 1

    _common_test(name, index, identifier)


def test_multiple() -> None:
    """Test for base name of file including several same split identifier."""
    identifier: str = _get_identifier()
    name: str = _get_name(["group", "type"], identifier)
    index: int = 1

    _common_test(name, index, identifier)


def test_index() -> None:
    """Test for base name of file, but it doesn't include index string."""
    name: str = "file"

    _not_none_error(_split_name(name))


def test_option() -> None:
    """Test for index string including option characters."""
    identifier: str = _get_identifier()
    name: str = "file"
    index: int = 1

    _split_test(
        name,
        index,
        _split_name(_get_base_name_option(name, index, identifier)),
    )


def test_digit() -> None:
    """Test for base name of file including 4 digit index text."""
    identifier: str = _get_identifier()
    name: str = "file"
    index: int = 1

    _split_test(
        name,
        index,
        _split_name(_get_base_name_digit(name, index, identifier)),
    )


def test_identifier() -> None:
    """Test for base name including specific split identifier."""
    identifier: str = "-"
    name: str = _get_name(["group", "type"], identifier)
    index: int = 1

    _split_test(
        name,
        index,
        _split_name_identifier(
            _get_base_name(name, index, identifier),
            identifier,
        ),
    )


def test_join() -> None:
    """Test to Convert elements about file name to base name of file."""
    identifier: str = _get_identifier()
    name: str = "file"
    index: int = 1

    _join_test(_get_base_name_digit(name, index, identifier), NameElements())
