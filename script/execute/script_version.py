#!/usr/bin/env python
# -*- coding: utf-8 -*-


from spartaproject.context.default.integer_context import Ints


def version_to_string(versions: Ints) -> str:
    return '.'.join([str(number) for number in versions])
