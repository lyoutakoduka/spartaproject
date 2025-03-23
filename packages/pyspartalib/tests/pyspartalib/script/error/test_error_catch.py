#!/usr/bin/env python

"""Test module to catch errors, and it is used through method overriding."""

from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import ErrorRaise


class TestValue(ErrorCatch, ErrorRaise):
    """Test class to catch ValueError together with the error identifier."""

    def _get_match(self) -> str:
        return "value"

    def _error_value(self) -> None:
        self.error_value(self._get_match())

    def test_value(self) -> None:
        """Catch ValueError together with the error identifier."""
        self.catch_value(self._error_value, self._get_match())


class TestNotFound(ErrorCatch, ErrorRaise):
    """Test class to catch FileNotFoundError.

    It together with the error identifier.
    """

    def _get_match(self) -> str:
        return "not_found"

    def _error_not_found(self) -> None:
        self.error_not_found(self._get_match())

    def test_not_found(self) -> None:
        """Catch FileNotFoundError together with the error identifier."""
        self.catch_not_found(self._error_not_found, self._get_match())


class TestFloat(ErrorCatch, ErrorRaise):
    """Test class to catch FloatOperation for a test."""

    def test_float(self) -> None:
        """Catch FloatOperation for a test."""
        self.catch_float(self.error_float)
