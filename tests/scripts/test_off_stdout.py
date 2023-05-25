#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.format_texts import format_indent
from scripts.off_stdout import StdoutText


def test_pass() -> None:
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
    test_pass()
    return True
