#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.string.format_texts import format_indent
from pyspartaproj.script.string.off_stdout import StdoutText


def test_messages() -> None:
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
    test_messages()
    return True
