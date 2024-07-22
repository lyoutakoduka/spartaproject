#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyspartaproj.script.string.encoding.find_encoding import find_encoding


def set_decoding(byte: bytes, encoding: str | None = None) -> str:
    if encoding is None:
        encoding = find_encoding(byte)

    return byte.decode(encoding)
