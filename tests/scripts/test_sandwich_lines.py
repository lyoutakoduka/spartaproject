#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.off_stdout import StdoutText
from scripts.format_texts import format_indent
from scripts.sandwich_lines import SandWich


def test_pass() -> None:
    MESSAGE: str = "Hello, World!"
    EXPECTED: str = """
        -------------
        Hello, World!
        =============
        """

    expected: str = format_indent(EXPECTED, stdout=True)

    stdout_text = StdoutText()
    sandwich = SandWich(count=len(MESSAGE), begin='-', end='=')

    @stdout_text.deco
    @sandwich.deco
    def _messages_sand() -> None:
        print(MESSAGE)

    _messages_sand()
    assert expected == stdout_text.show()


def main() -> bool:
    test_pass()
    return True
