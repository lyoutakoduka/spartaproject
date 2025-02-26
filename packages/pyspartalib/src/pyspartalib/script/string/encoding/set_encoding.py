#!/usr/bin/env python

"""Module to encode string by specific character encoding."""


def set_encoding(source: str, encoding: str | None = None) -> bytes:
    """Encode string by specific character encoding.

    Args:
        source (str): String data you want to encode.

        encoding (str | None, optional): Defaults to None.
            Character encoding you want to override forcibly.
            Default character encoding is "utf-8".

    Returns:
        bytes: Converted Byte date.

    """
    if encoding is None:
        encoding = "utf-8"

    return source.encode(encoding)
