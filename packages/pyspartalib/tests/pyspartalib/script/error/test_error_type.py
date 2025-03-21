#!/usr/bin/env python

from pathlib import Path

import pytest
from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.script.directory.working.working_directory import (
    WorkingDirectory,
)
from pyspartalib.script.error.error_type import (
    ErrorBase,
    ErrorContain,
    ErrorDifference,
    ErrorFail,
    ErrorLength,
    ErrorNoExists,
    ErrorNone,
)


class _TestShare:
    def catch_error(
        self,
        function: Func,
        match: str,
        error: type[Exception] = ValueError,
    ) -> None:
        with pytest.raises(error, match=match):
            function()

    def catch_error_not_found(self, function: Func, match: str) -> None:
        self.catch_error(function, match, error=FileNotFoundError)

    def get_result_integer(self) -> Ints:
        return list(range(3))


class TestBase(_TestShare, ErrorBase):
    def _get_match(self) -> str:
        return "base"

    def _raise_error(self) -> None:
        self.error_value(self._get_match())

    def test_value(self) -> None:
        self.catch_error(self._raise_error, self._get_match())


class TestFail(_TestShare, ErrorFail):
    def _get_match(self) -> str:
        return "fail"

    def _error_fail(self, result: bool, invert: bool) -> None:
        self.error_fail(result, self._get_match(), invert=invert)

    def _raise_error(self) -> None:
        self._error_fail(False, False)

    def _raise_error_not(self) -> None:
        self._error_fail(True, True)

    def _cache_error(self, function: Func) -> None:
        self.catch_error(function, self._get_match())

    def test_fail(self) -> None:
        self._cache_error(self._raise_error)

    def test_fail_not(self) -> None:
        self._cache_error(self._raise_error_not)


class TestNone(_TestShare, ErrorNone, ErrorDifference):
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
        self.catch_error(function, self._get_match())

    def test_none(self) -> None:
        self._cache_error(self._raise_error)

    def test_none_not(self) -> None:
        self._cache_error(self._raise_error_not)

    def test_none_success(self) -> None:
        self._raise_error_success()


class TestNoExists(_TestShare, ErrorNoExists, WorkingDirectory):
    def _get_match(self) -> str:
        return "exists"

    def _error_no_exists(self, result: Path, invert: bool) -> None:
        self.error_no_exists(result, self._get_match(), invert=invert)

    def _raise_error(self) -> None:
        self._error_no_exists(Path("error"), False)

    def _raise_error_not(self) -> None:
        self._error_no_exists(self.get_working_root(), True)

    def _cache_error(self, function: Func) -> None:
        self.catch_error_not_found(function, self._get_match())

    def _no_exists_not(self) -> bool:
        self._cache_error(self._raise_error_not)
        return True

    def test_no_exists(self) -> None:
        self._cache_error(self._raise_error)

    def test_no_exists_not(self) -> None:
        self.inside_working(self._no_exists_not)


class TestContain(_TestShare, ErrorContain):
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
        self.catch_error(function, self._get_match())

    def test_contain(self) -> None:
        self._cache_error(self._raise_error)

    def test_contain_not(self) -> None:
        self._cache_error(self._raise_error_not)


class TestLength(_TestShare, ErrorLength):
    def _get_match(self) -> str:
        return "length"
