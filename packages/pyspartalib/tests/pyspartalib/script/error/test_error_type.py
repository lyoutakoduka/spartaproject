#!/usr/bin/env python

import pytest
from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.script.error.error_type import ErrorBase, ErrorFail


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
