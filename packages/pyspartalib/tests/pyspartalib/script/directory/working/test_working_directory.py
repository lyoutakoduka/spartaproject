#!/usr/bin/env python

from pyspartalib.context.custom.callable_context import BoolFunc, Func
from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if expected != result:
        raise ValueError


def _fail_error(status: bool) -> None:
    if not status:
        raise ValueError


class _Share(WorkingDirectory):
    def execute_function(self, function: BoolFunc) -> None:
        _fail_error(self.inside_working(function))


class TestLaunch(_Share):
    def _individual_test(self) -> bool:
        return True

    def test_launch(self) -> None:
        self.execute_function(self._individual_test)


class TestPath(_Share):
    def _decorate_function(self, function: Func) -> str:
        off_stdout = OffStdout()

        @off_stdout.decorator
        def _messages() -> None:
            function()

        _messages()

        return off_stdout.show()

    def _execute_with_log(self) -> None:
        send_stdout(self.get_working_root())

    def _remove_line_break(self, result: str) -> str:
        return result[:-1]

    def _get_result(self) -> str:
        return self._remove_line_break(
            self._decorate_function(self._execute_with_log),
        )

    def _get_expected(self) -> str:
        return self.get_working_root().as_posix()

    def _individual_test(self) -> bool:
        _difference_error(self._get_result(), self._get_expected())
        return True

    def test_path(self) -> None:
        self.execute_function(self._individual_test)
