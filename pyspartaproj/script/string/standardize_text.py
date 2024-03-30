#!/usr/bin/env python
# -*- coding: utf-8 -*-


def standardize_text(text: str) -> str:
    text = text.lower()

    for identifier in [" ", "."]:
        text = text.replace(identifier, "_")

    return text
