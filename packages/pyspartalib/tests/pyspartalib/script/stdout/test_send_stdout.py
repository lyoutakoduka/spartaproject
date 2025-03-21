#!/usr/bin/env python

"""Test module to show log to stdout."""

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> str:
    return "test"


def _show_log() -> None:
    send_stdout(_get_expected())


def _decorate_function(off_stdout: OffStdout) -> str:
    @off_stdout.decorator
    def _messages() -> None:
        _show_log()

    _messages()

    return off_stdout.show()


def _remove_end(result: str) -> str:
    return result[:-1]


def _execute_log_function() -> str:
    return _remove_end(_decorate_function(OffStdout()))


def test_show() -> None:
    """Test to show log to stdout."""
    _difference_error(_execute_log_function(), _get_expected())
