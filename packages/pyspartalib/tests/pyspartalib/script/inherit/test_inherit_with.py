#!/usr/bin/env python

"""Test module to use With statement by using custom class."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.inherit.inherit_with import InheritWith
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


class TemporaryWith(InheritWith):
    """Test class to use With statement by using custom class."""

    def exit(self) -> None:
        """Show log message when leaving With statement."""
        send_stdout("exit")

    def __init__(self) -> None:
        """Show log message when creating instance."""
        send_stdout("init")


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_expected() -> str:
    return """
        init
        exit
        """


def _use_temporary_with() -> None:
    with TemporaryWith() as node:
        _fail_error(type(node) is TemporaryWith)


def _decorate_function(off_stdout: OffStdout) -> str:
    @off_stdout.decorator
    def _messages() -> None:
        _use_temporary_with()

    _messages()

    return off_stdout.show()


def test_with() -> None:
    """Test to call custom method when leaving from With statement."""
    _difference_error(
        _decorate_function(OffStdout()),
        format_indent(_get_expected(), stdout=True),
    )
