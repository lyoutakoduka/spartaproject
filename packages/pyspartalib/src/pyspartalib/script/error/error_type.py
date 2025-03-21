#!/usr/bin/env python

from collections.abc import Container, Sized
from pathlib import Path

from pyspartalib.context.custom.type_context import Type


class _Base:
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert

    def error_base(self, match: str) -> None:
        raise ValueError(match)

    def raise_not_found(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            raise FileNotFoundError(match)

    def raise_value(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.error_base(match)


class _TypeFail(_Base):
    def __confirm(self, result: bool) -> bool:
        return not result

    def error_fail(
        self,
        result: bool,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self.__confirm(result), match, invert)


class _TypeNone(_Base):
    def __confirm(self, result: object) -> bool:
        return result is None

    def error_none(
        self,
        result: object | None,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self.__confirm(result), match, invert)


class _TypeNoExists(_Base):
    def __confirm(self, result: Path) -> bool:
        return not result.exists()

    def error_no_exists(
        self,
        result: Path,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_not_found(self.__confirm(result), match, invert)


class _TypeContain(_Base):
    def __confirm(self, result: Container[Type], expected: object) -> bool:
        return expected not in result

    def error_contain(
        self,
        result: Container[Type],
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self.__confirm(result, expected), match, invert)


class _TypeLength(_Base):
    def __confirm(self, result: Sized, expected: int) -> bool:
        return len(result) != expected

    def error_length(
        self,
        result: Sized,
        expected: int,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self.__confirm(result, expected), match, invert)


class _TypeDifference(_Base):
    def __confirm(self, result: Type, expected: Type) -> bool:
        return result != expected

    def error_difference(
        self,
        result: Type,
        expected: Type,
        match: str,
        invert: bool = False,
    ) -> None:
        self.raise_value(self.__confirm(result, expected), match, invert)
