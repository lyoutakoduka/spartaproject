#!/usr/bin/env python

from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import ErrorRaise


class TestValue(ErrorCatch, ErrorRaise):
    def _get_match(self) -> str:
        return "value"

    def _error_value(self) -> None:
        self.error_value(self._get_match())

    def test_value(self) -> None:
        self.catch_value(self._error_value, self._get_match())


class TestNotFound(ErrorCatch, ErrorRaise):
    def _get_match(self) -> str:
        return "not_found"

    def _error_not_found(self) -> None:
        self.error_not_found(self._get_match())

    def test_not_found(self) -> None:
        self.catch_not_found(self._error_not_found, self._get_match())


class TestFloat(ErrorCatch, ErrorRaise):
    def test_float(self) -> None:
        self.catch_float(self.error_float)
