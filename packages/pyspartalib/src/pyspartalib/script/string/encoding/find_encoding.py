#!/usr/bin/env python

"""Module to find character encoding from string automatically."""

from pyspartalib.interface.chardet import UniversalDetector


def _analysis(byte: bytes) -> str | None:
    detector = UniversalDetector()

    detector.feed(byte)
    detector.close()

    return detector.result["encoding"]


def _find_sjis(candidate: str) -> str:
    if candidate in ["Windows-1254", "Windows-1252"]:
        return "shift-jis"

    return candidate


def find_encoding(byte: bytes) -> str:
    """Find character encoding from string automatically.

    Args:
        byte (bytes): Byte data you want to get character encoding.

    Returns:
        str: Character encoding of the byte data.
    """
    encoding: str = "utf-8"

    if candidate := _analysis(byte):
        encoding = _find_sjis(candidate)

    return encoding
