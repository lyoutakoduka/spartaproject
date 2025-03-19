#!/usr/bin/env python

from pyspartalib.context.custom.callable_context import BoolFunc
from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)


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
