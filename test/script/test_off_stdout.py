#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.format_texts import format_indent
from pyspartaproj.script.off_stdout import StdoutText


def test_messages() -> None:
    MESSAGE: str = "Hello, World!"
    EXPECTED: str = """
        Hello, World!
        Hello, World!
        """

    expected: str = format_indent(EXPECTED, stdout=True)

    stdout_text = StdoutText()

    @stdout_text.decorator
    def _messages() -> None:
        print(MESSAGE)
        print(MESSAGE)

    _messages()

    assert expected == stdout_text.show()


def main() -> bool:
    test_messages()
    return True
