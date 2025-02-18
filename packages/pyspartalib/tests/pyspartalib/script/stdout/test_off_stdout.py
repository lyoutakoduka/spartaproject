#!/usr/bin/env python

"""Test module to redirect stdout to string variable forcibly."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _decorate_function(message: str, off_stdout: OffStdout) -> None:
    @off_stdout.decorator
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
    off_stdout = OffStdout()

    _decorate_function(message, off_stdout)

    _difference_error(off_stdout.show(), format_indent(expected, stdout=True))
