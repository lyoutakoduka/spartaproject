#!/usr/bin/env python

"""Module to remove white space at the beginning of a sentence."""

from itertools import takewhile

from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs

from .context.format_context import FormatPair, FormatPairs


def _get_space_size(striped_right: str) -> int:
    count_right: int = len(striped_right)
    minimum: int = 0

    if count_right <= minimum:
        return minimum

    return count_right - len(striped_right.lstrip())


def _get_format_pair(line: str) -> FormatPair:
    striped_right: str = line.rstrip()

    return {
        "text": striped_right,
        "count": _get_space_size(striped_right),
    }


def _strip_line(source_text: str) -> FormatPairs:
    return [_get_format_pair(line) for line in source_text.splitlines()]


def _get_clipped_line(size: int, line: str) -> str:
    return line[(size if size < len(line) else 0) :]


def _clip_line(size: int, attributes: FormatPairs) -> Strs:
    return [
        _get_clipped_line(size, attribute["text"]) for attribute in attributes
    ]


def _strip_lines(lines: Strs) -> Strs:
    striped_lines: Strs = list(takewhile(lambda line: len(line) == 0, lines))
    index: int = len(striped_lines)
    return lines[index:]


def _get_line_counts(line_attributes: FormatPairs) -> Ints:
    return [line_attribute["count"] for line_attribute in line_attributes]


def format_indent(source_text: str, stdout: bool = False) -> str:
    """Remove white space at the beginning of a sentence.

    Args:
        source_text (str): Multiple line text you want to remove white space.

        stdout (bool, optional): Defaults to False.
            If True, add line break to end of the sentence at last line.

    Returns:
        str: Text which is removed white space.

    """
    line_attributes: FormatPairs = _strip_line(source_text)
    counts: Ints = sorted(set(_get_line_counts(line_attributes)))
    counts.remove(0)

    if len(counts) == 0:
        return ""

    empty_size: int = counts[0]
    lines: Strs = _clip_line(empty_size, line_attributes)

    for _ in range(2):
        lines = _strip_lines(list(reversed(lines)))

    if stdout:
        lines += [""]

    return "\n".join(lines)
