#!/usr/bin/env python

"""Test module to redirect stdout to string variable forcibly."""

from pyspartalib.context.type_context import Type
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import StdoutText
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _decorate_function(message: str, stdout_text: StdoutText) -> None:
    @stdout_text.decorator
    def _messages() -> None:
        send_stdout(message)
        send_stdout(message)

    _messages()


def test_messages() -> None:
    """Test to redirect stdout to string variable forcibly."""
    message: str = "Hello, World!"
    expected: str = """
        Hello, World!
        Hello, World!
        """
    stdout_text = StdoutText()

    _decorate_function(message, stdout_text)

    _difference_error(stdout_text.show(), format_indent(expected, stdout=True))
