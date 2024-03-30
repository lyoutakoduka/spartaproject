#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _convert_lower(text: str) -> str:
    return text.lower()


def standardize_text(text: str) -> str:
    text = _convert_lower(text)

    for identifier in [" ", "."]:
        text = text.replace(identifier, "_")

    text = text.strip("_")

    return text
