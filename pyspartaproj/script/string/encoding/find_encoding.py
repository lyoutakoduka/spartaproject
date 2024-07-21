#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chardet.universaldetector import UniversalDetector


def find_encoding(byte: bytes) -> str:
    encoding: str = "utf-8"

    detector = UniversalDetector()
    detector.feed(byte)
    detector.close()

    if candidate := detector.result["encoding"]:
        if "Windows-1254" == candidate:
            encoding = "shift-jis"

        elif "Windows-1252" == candidate:
            encoding = "shift-jis"

        else:
            encoding = candidate

    return encoding
