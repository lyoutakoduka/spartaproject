#!/usr/bin/env python


class _Base:
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert

    def base_value(self, match: str) -> None:
        raise ValueError(match)

    def raise_not_found(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            raise FileNotFoundError(match)

    def raise_value(self, result: bool, match: str, invert: bool) -> None:
        if self._invert(result, invert):
            self.base_value(match)


class _TypeFail(_Base):
    def __confirm(self, result: bool) -> bool:
        return not result

    def type_fail(self, result: bool, match: str, invert: bool) -> None:
        self.raise_value(self.__confirm(result), match, invert)


class _TypeNone(_Base):
    def __confirm(self, result: object) -> bool:
        return result is None
