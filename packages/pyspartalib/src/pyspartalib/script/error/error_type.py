#!/usr/bin/env python


class _Base:
    def _invert(self, result: bool, invert: bool) -> bool:
        return result ^ invert
