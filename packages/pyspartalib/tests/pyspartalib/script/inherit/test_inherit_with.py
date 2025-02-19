#!/usr/bin/env python

from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.inherit.inherit_with import InheritWith
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


class TemporaryWith(InheritWith):
    def exit(self) -> None:
        send_stdout("exit")

    def __init__(self) -> None:
        send_stdout("init")


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _status_error(status: bool) -> None:
    if not status:
        raise ValueError


def _get_expected() -> str:
    return """
        init
        exit
        """


def _use_temporary_with() -> None:
    with TemporaryWith() as node:
        _status_error(type(node) is TemporaryWith)


def _decorate_function(off_stdout: OffStdout) -> str:
    @off_stdout.decorator
    def _messages() -> None:
        _use_temporary_with()

    _messages()

    return off_stdout.show()
