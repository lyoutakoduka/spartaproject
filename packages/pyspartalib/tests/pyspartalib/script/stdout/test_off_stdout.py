#!/usr/bin/env python

"""Test module to redirect stdout to string variable forcibly."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_source() -> str:
    return "Hello, World!"


def _get_expected() -> str:
    return """
        Hello, World!
        Hello, World!
        """


def _decorate_function(message: str, off_stdout: OffStdout) -> OffStdout:
    @off_stdout.decorator
    def _messages() -> None:
        send_stdout(message)
        send_stdout(message)

    _messages()

    return off_stdout


def test_messages() -> None:
    """Test to redirect stdout to string variable forcibly."""
    _difference_error(
        _decorate_function(_get_source(), OffStdout()).show(),
        format_indent(_get_expected(), stdout=True),
    )
