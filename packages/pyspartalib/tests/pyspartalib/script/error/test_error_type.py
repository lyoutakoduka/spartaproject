#!/usr/bin/env python

"""Test module to raise errors, and it is used through method overriding."""

from pathlib import Path

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)
from pyspartalib.script.error.error_catch import ErrorCatch
from pyspartalib.script.error.error_raise import (
    ErrorContain,
    ErrorDifference,
    ErrorFail,
    ErrorLength,
    ErrorNoExists,
    ErrorNone,
    ErrorRaise,
)


class _TestShare(ErrorCatch):
    def get_result_integer(self) -> Ints:
        return list(range(3))


class TestBase(_TestShare, ErrorRaise):
    """Test class to raise errors together with the error identifier."""

    def _get_match(self) -> str:
        return "base"

    def _error_value(self) -> None:
        self.error_value(self._get_match())

    def _raise_not_found(self) -> None:
        self.error_not_found(self._get_match())

    def test_value(self) -> None:
        """Test to raise ValueError together with the error identifier."""
        self.catch_value(self._error_value, self._get_match())

    def test_not_found(self) -> None:
        """Test to raise FileNotFoundError.

        It together with the error identifier.
        """
        self.catch_not_found(self._raise_not_found, self._get_match())


class TestFail(_TestShare, ErrorFail):
    """Test class to raise error if the input value is False."""

    def _get_match(self) -> str:
        return "fail"

    def _error_fail(self, result: bool, invert: bool) -> None:
        self.error_fail(result, self._get_match(), invert=invert)

    def _raise_error(self) -> None:
        self._error_fail(False, False)

    def _raise_error_not(self) -> None:
        self._error_fail(True, True)

    def _cache_error(self, function: Func) -> None:
        self.catch_value(function, self._get_match())

    def test_fail(self) -> None:
        """Test to raise error if the input value is False."""
        self._cache_error(self._raise_error)

    def test_fail_not(self) -> None:
        """Test to raise error if the input value is True."""
        self._cache_error(self._raise_error_not)


class TestNone(_TestShare, ErrorNone, ErrorDifference):
    """Test class to raise error if the input value is None."""

    def _get_expected(self) -> str:
        return "success"

    def _get_match(self) -> str:
        return "none"

    def _error_none(self, result: str | None, invert: bool) -> None:
        self.error_none(result, self._get_match(), invert=invert)

    def _error_none_walrus(self) -> str | None:
        return self.error_none_walrus(self._get_expected(), self._get_match())

    def _raise_error(self) -> None:
        self._error_none(None, False)

    def _raise_error_not(self) -> None:
        self._error_none(self._get_expected(), True)

    def _raise_error_success(self) -> None:
        if (result := self._error_none_walrus()) is not None:
            self.error_difference(result, self._get_expected(), "difference")
        else:
            self.error_value("base")

    def _cache_error(self, function: Func) -> None:
        self.catch_value(function, self._get_match())

    def test_none(self) -> None:
        """Test to raise error if the input value is None."""
        self._cache_error(self._raise_error)

    def test_none_not(self) -> None:
        """Test to raise error if the input value is not None."""
        self._cache_error(self._raise_error_not)

    def test_none_success(self) -> None:
        """Test to assign the result of method by using a walrus operator."""
        self._raise_error_success()


class TestNoExists(_TestShare, ErrorNoExists, WorkingDirectory):
    """Test class to raise error if the input path does not exist."""

    def _get_match(self) -> str:
        return "exists"

    def _error_no_exists(self, result: Path, invert: bool) -> None:
        self.error_no_exists(result, self._get_match(), invert=invert)

    def _raise_error(self) -> None:
        self._error_no_exists(Path("error"), False)

    def _raise_error_not(self) -> None:
        self._error_no_exists(self.get_working_root(), True)

    def _cache_error(self, function: Func) -> None:
        self.catch_not_found(function, self._get_match())

    def _no_exists_not(self) -> bool:
        self._cache_error(self._raise_error_not)
        return True

    def test_no_exists(self) -> None:
        """Test to raise error if the input path does not exist."""
        self._cache_error(self._raise_error)

    def test_no_exists_not(self) -> None:
        """Test to raise error if the input path exists."""
        self.inside_working(self._no_exists_not)


class TestContain(_TestShare, ErrorContain):
    """Test class to raise error if the input value is not in the container."""

    def _get_match(self) -> str:
        return "contain"

    def _error_contain(self, expected: int, invert: bool) -> None:
        self.error_contain(
            self.get_result_integer(),
            expected,
            self._get_match(),
            invert=invert,
        )

    def _raise_error(self) -> None:
        self._error_contain(3, False)

    def _raise_error_not(self) -> None:
        self._error_contain(0, True)

    def _cache_error(self, function: Func) -> None:
        self.catch_value(function, self._get_match())

    def test_contain(self) -> None:
        """Test to raise error if the input value is not in the container."""
        self._cache_error(self._raise_error)

    def test_contain_not(self) -> None:
        """Test to raise error if the input value is in the container."""
        self._cache_error(self._raise_error_not)


class TestLength(_TestShare, ErrorLength):
    """Test class to raise error.

    If the input length of Sized type is not as the expected value.
    """

    def _get_match(self) -> str:
        return "length"

    def _error_length(self, expected: int, invert: bool) -> None:
        self.error_length(
            self.get_result_integer(),
            expected,
            self._get_match(),
            invert=invert,
        )

    def _raise_error(self) -> None:
        self._error_length(0, False)

    def _raise_error_not(self) -> None:
        self._error_length(3, True)

    def _cache_error(self, function: Func) -> None:
        self.catch_value(function, self._get_match())

    def test_length(self) -> None:
        """Test to raise error.

        If the input length of Sized type is not as the expected value.
        """
        self._cache_error(self._raise_error)

    def test_length_not(self) -> None:
        """Test to raise error.

        If the input length of Sized type is as the expected value.
        """
        self._cache_error(self._raise_error_not)


class TestDifference(_TestShare, ErrorDifference):
    """Test class to raise error if input the two values are different."""

    def _get_match(self) -> str:
        return "difference"

    def _error_difference(self, expected: int, invert: bool) -> None:
        self.error_difference(0, expected, self._get_match(), invert=invert)

    def _raise_error(self) -> None:
        self._error_difference(1, False)

    def _raise_error_not(self) -> None:
        self._error_difference(0, True)

    def _cache_error(self, function: Func) -> None:
        self.catch_value(function, self._get_match())

    def test_difference(self) -> None:
        """Test to raise error if input the two values are different."""
        self._cache_error(self._raise_error)

    def test_difference_not(self) -> None:
        """Test to raise error if input the two values are the same."""
        self._cache_error(self._raise_error_not)
