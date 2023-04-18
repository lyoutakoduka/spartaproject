#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
from typing import List, TypedDict


class _LinePair(TypedDict):
    text: str
    count: int


_Nums = List[int]
_Strs = List[str]
_LinePairs = List[_LinePair]


_EMPTY = ''
_ENTER = '\n'


def _strip_line(input: str) -> _LinePairs:
    line_attributes: _LinePairs = []

    for line in input.splitlines():
        striped_right: str = line.rstrip()
        count_right: int = len(striped_right)
        space_size: int = 0

        if 0 < count_right:
            striped_left: str = striped_right.lstrip()
            count_left: int = len(striped_left)
            space_size = count_right - count_left

        line_attribute: _LinePair = {
            'text': striped_right,
            'count': space_size
        }

        line_attributes += [line_attribute]

    return line_attributes


def _clip_line(empty_size: int, line_attributes: _LinePairs) -> _Strs:
    clipped_lines: _Strs = []

    for line_attribute in line_attributes:
        line: str = line_attribute['text']
        index: int = empty_size if empty_size < len(line) else 0
        clipped_lines += [line[index:]]

    return clipped_lines


def _strip_lines(lines: _Strs) -> _Strs:
    striped_Lines: _Strs = list(itertools.takewhile(
        lambda line: 0 == len(line), lines))

    return lines[len(striped_Lines):]


def format_indent(input: str, stdout: bool = False) -> str:
    line_attributes: _LinePairs = _strip_line(input)

    counts: _Nums = [
        line_attribute['count'] for line_attribute in line_attributes]

    counts = list(set(counts))

    counts.sort()
    counts.remove(0)

    if 0 == len(counts):
        return _EMPTY

    empty_size: int = counts[0]
    lines: _Strs = _clip_line(empty_size, line_attributes)

    for _ in range(2):
        lines = _strip_lines(list(reversed(lines)))

    if stdout:
        lines += ['']

    return _ENTER.join(lines)


def main() -> bool:
    INPUT: str = """

        Formats text for document of API.

        Args:
            num1 (int): 1st operand.
            num2 (int): 2nd operand.

        Returns:
            int: result.

        Raises:
            InvalidArgumentsError:

    """

    EXPECTED: _Strs = [
        "Formats text for document of API.",
        "",
        "Args:",
        "    num1 (int): 1st operand.",
        "    num2 (int): 2nd operand.",
        "",
        "Returns:",
        "    int: result.",
        "",
        "Raises:",
        "    InvalidArgumentsError:",
        "",
    ]
    expected: str = _ENTER.join(EXPECTED)

    result: str = format_indent(INPUT, stdout=True)

    return expected == result


if __name__ == '__main__':
    sys.exit(not main())
