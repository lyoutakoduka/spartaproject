#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to find character encoding from string automatically."""

from chardet.universaldetector import UniversalDetector


def _analysis(byte: bytes) -> str | None:
    detector = UniversalDetector()

    detector.feed(byte)
    detector.close()

    return detector.result["encoding"]


def find_encoding(byte: bytes) -> str:
    """Find character encoding from string automatically.

    Args:
        byte (bytes): Byte data you want to get character encoding.

    Returns:
        str: Character encoding of the byte data.
    """
    encoding: str = "utf-8"

    if candidate := _analysis(byte):
        if "Windows-1254" == candidate:
            encoding = "shift-jis"

        elif "Windows-1252" == candidate:
            encoding = "shift-jis"

        else:
            encoding = candidate

    return encoding
