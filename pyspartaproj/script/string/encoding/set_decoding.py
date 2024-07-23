#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to decode byte data by specific character encoding."""

from pyspartaproj.script.string.encoding.find_encoding import find_encoding


def set_decoding(byte: bytes, encoding: str | None = None) -> str:
    """Decode byte data by specific character encoding.

    Args:
        byte (bytes): Byte data you want to decode.

        encoding (str | None, optional): Defaults to None.
            Character encoding used for decoding forcibly.

    Returns:
        str: Decoded string.
    """
    if encoding is None:
        encoding = find_encoding(byte)

    return byte.decode(encoding)
