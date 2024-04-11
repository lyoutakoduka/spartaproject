#!/usr/bin/env python
# -*- coding: utf-8 -*-


def convert_integer(index: str) -> int | None:
    try:
        return int(index)
    except BaseException:
        return None
