#!/usr/bin/env python

from collections.abc import Container, Sized
from pathlib import Path

from pyspartalib.context.custom.type_context import Type


class ErrorBase:
    def _error_base(
        self,
        match: str,
        error: type[Exception] = ValueError,
    ) -> None:
        raise error(match)

    def error_value(self, match: str) -> None:
        self._error_base(match)

    def error_not_found(self, match: str) -> None:
        self._error_base(match, error=FileNotFoundError)


class _Base(ErrorBase):
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert

    def raise_not_found(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.error_not_found(match)

    def raise_value(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.error_value(match)


class ErrorFail(_Base):
    def _confirm(self, result: bool) -> bool:
        return not result

    def error_fail(
        self,
        result: bool,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self._confirm(result), match, invert)


class ErrorNone(_Base):
    def _confirm(self, result: object) -> bool:
        return result is None

    def error_none(
        self,
        result: object | None,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self._confirm(result), match, invert)

    def error_none_walrus(
        self,
        result: Type | None,
        match: str,
        invert: bool = False,
    ) -> Type | None:
        self.error_none(result, match, invert=invert)
        return result


class ErrorNoExists(_Base):
    def _confirm(self, result: Path) -> bool:
        return not result.exists()

    def error_no_exists(
        self,
        result: Path,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_not_found(self._confirm(result), match, invert)


class ErrorContain(_Base):
    def _confirm(self, result: Container[Type], expected: object) -> bool:
        return expected not in result

    def error_contain(
        self,
        result: Container[Type],
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self._confirm(result, expected), match, invert)


class ErrorLength(_Base):
    def _confirm(self, result: Sized, expected: int) -> bool:
        return len(result) != expected

    def error_length(
        self,
        result: Sized,
        expected: int,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self._confirm(result, expected), match, invert)


class ErrorDifference(_Base):
    def _confirm(self, result: Type, expected: Type) -> bool:
        return result != expected

    def error_difference(
        self,
        result: Type,
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self._confirm(result, expected), match, invert)
