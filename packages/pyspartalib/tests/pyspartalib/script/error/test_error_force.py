#!/usr/bin/env python

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.error.error_force import ErrorForce
from pyspartalib.script.error.error_type import ErrorDifference, ErrorNone


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

    def test_empty(self) -> None:
        self.error_difference(self._get_result(), "success", "empty")


class TestContain(ErrorNone):
    def _get_error_types(self) -> Strs:
        return ["none", "fail", "exists"]

    def _get_test_force(self) -> _TestForce:
        return _TestForce(error_types=self._get_error_types())

    def _get_result(self) -> str | None:
        return self._get_test_force().select_process("none")

    def test_contain(self) -> None:
        self.error_none(self._get_result(), "contain", invert=True)
