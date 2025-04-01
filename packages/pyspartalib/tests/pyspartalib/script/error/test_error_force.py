#!/usr/bin/env python

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.error.error_force import ErrorForce
from pyspartalib.script.error.error_type import ErrorDifference


class _TestForce(ErrorForce):
    def __initialize_super_class(self, error_types: Strs | None) -> None:
        ErrorForce.__init__(self, error_types=error_types)

    def _reproduce_external(self) -> str | None:
        return "success"

    def select_process(self, error_type: str) -> str | None:
        if self.find_type(error_type):
            return None

        return self._reproduce_external()

    def __init__(self, error_types: Strs | None = None) -> None:
        self.__initialize_super_class(error_types)


class TestEmpty(ErrorDifference):
    def _get_result(self) -> str | None:
        return _TestForce().select_process("none")
