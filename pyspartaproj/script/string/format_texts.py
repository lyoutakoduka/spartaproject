#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import takewhile
from typing import List, TypedDict

from pyspartaproj.context.default.integer_context import Ints
from pyspartaproj.context.default.string_context import Strs


class _LinePair(TypedDict):
    text: str
    count: int


_LinePairs = List[_LinePair]


def _strip_line(source_text: str) -> _LinePairs:
    line_attributes: _LinePairs = []

    for line in source_text.splitlines():
        striped_right: str = line.rstrip()
        count_right: int = len(striped_right)
        space_size: int = 0

        if 0 < count_right:
            striped_left: str = striped_right.lstrip()
            count_left: int = len(striped_left)
            space_size = count_right - count_left

        line_attribute: _LinePair = {
            "text": striped_right,
            "count": space_size,
        }

        line_attributes += [line_attribute]

    return line_attributes


def _clip_line(empty_size: int, line_attributes: _LinePairs) -> Strs:
    clipped_lines: Strs = []

    for line_attribute in line_attributes:
        line: str = line_attribute["text"]
        index: int = empty_size if empty_size < len(line) else 0
        clipped_lines += [line[index:]]

    return clipped_lines


def _strip_lines(lines: Strs) -> Strs:
    striped_lines: Strs = list(takewhile(lambda line: 0 == len(line), lines))
    index: int = len(striped_lines)
    return lines[index:]


def format_indent(source_text: str, stdout: bool = False) -> str:
    line_attributes: _LinePairs = _strip_line(source_text)

    counts: Ints = [
        line_attribute["count"] for line_attribute in line_attributes
    ]

    counts = sorted(set(counts))

    counts.remove(0)

    if 0 == len(counts):
        return ""

    empty_size: int = counts[0]
    lines: Strs = _clip_line(empty_size, line_attributes)

    for _ in range(2):
        lines = _strip_lines(list(reversed(lines)))

    if stdout:
        lines += [""]

    return "\n".join(lines)
