#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.context.default.string_context import Strs


def temporary_text(count: int, order: int) -> Strs:
    return [str(i).zfill(order) for i in range(count)]
