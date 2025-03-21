#!/usr/bin/env python


class _Base:
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert

    def base_value(self, match: str) -> None:
        raise ValueError(match)
