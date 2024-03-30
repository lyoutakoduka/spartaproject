#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _convert_lower(text: str) -> str:
    return text.lower()


def _convert_under(text: str) -> str:
    for identifier in [" ", "."]:
        text = text.replace(identifier, "_")

    return text


def standardize_text(text: str) -> str:
    text = _convert_lower(text)

    text = _convert_under(text)

    text = text.strip("_")

    return text
