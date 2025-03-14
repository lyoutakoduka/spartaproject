#!/usr/bin/env python

"""Test module to standardize string for key of dictionary."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.string.rename.standardize_text import StandardizeText


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_mail_elements() -> Strs:
    return ["name", "domain", "com"]


def _get_invalid_mail(elements: Strs) -> str:
    parentheses: str = "(" + elements[1] + ")"
    at_mark: str = elements[0] + "@"
    mail_body: str = "".join([at_mark, parentheses, elements[2]])
    space: str = " " + mail_body + " "

    return space


def test_lower() -> None:
    """Test to convert upper case string to lower case."""
    _difference_error(
        StandardizeText().standardize("TEST", lower=True),
        "test",
    )


def test_all() -> None:
    """Test to convert string by using all conditions at once."""
    mail_elements: Strs = _get_mail_elements()

    _difference_error(
        StandardizeText().standardize(
            _get_invalid_mail(mail_elements),
            lower=True,
            under=True,
            strip=True,
            replace=True,
        ),
        "_".join(mail_elements),
    )
