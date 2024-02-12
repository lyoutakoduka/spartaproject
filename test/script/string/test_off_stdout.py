#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to redirect stdout to string variable forcibly."""

from pyspartaproj.script.string.format_texts import format_indent
from pyspartaproj.script.string.off_stdout import StdoutText


def test_messages() -> None:
    """Test to redirect stdout to string variable forcibly."""
    message: str = "Hello, World!"
    expected: str = """
        Hello, World!
        Hello, World!
        """

    stdout_text = StdoutText()

    @stdout_text.decorator
    def _messages() -> None:
        print(message)
        print(message)

    _messages()

    assert format_indent(expected, stdout=True) == stdout_text.show()


def main() -> bool:
    """Run all tests.

    Returns:
        bool: Success if get to the end of function.
    """
    test_messages()
    return True
