#!/usr/bin/env python

"""Test module to show log to stdout."""

from pyspartalib.context.callable_context import Type
from pyspartalib.script.stdout.logger import show_log
from pyspartalib.script.string.off_stdout import StdoutText


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> str:
    return "test"


def _show_log() -> None:
    show_log(_get_expected())


def _decorate_function(stdout_text: StdoutText) -> StdoutText:
    @stdout_text.decorator
    def _messages() -> None:
        _show_log()

    _messages()

    return stdout_text


def _execute_log_function() -> str:
    return _decorate_function(StdoutText()).show()


def test_show() -> None:
    """Test to show log to stdout."""
    _difference_error(_execute_log_function(), _get_expected())
