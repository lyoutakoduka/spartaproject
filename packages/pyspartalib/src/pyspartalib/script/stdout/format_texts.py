#!/usr/bin/env python

"""Module to remove white space at the beginning of a sentence."""

from itertools import takewhile

from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.typed.builtin_context import LinePair, LinePairs


def _strip_line(source_text: str) -> LinePairs:
    line_attributes: LinePairs = []

    for line in source_text.splitlines():
        striped_right: str = line.rstrip()
        count_right: int = len(striped_right)
        space_size: int = 0

        if count_right > 0:
            striped_left: str = striped_right.lstrip()
            count_left: int = len(striped_left)
            space_size = count_right - count_left

        line_attribute: LinePair = {
            "text": striped_right,
            "count": space_size,
        }

        line_attributes += [line_attribute]

    return line_attributes


def _clip_line(empty_size: int, line_attributes: LinePairs) -> Strs:
    clipped_lines: Strs = []

    for line_attribute in line_attributes:
        line: str = line_attribute["text"]
        index: int = empty_size if empty_size < len(line) else 0
        clipped_lines += [line[index:]]

    return clipped_lines


def _strip_lines(lines: Strs) -> Strs:
    striped_lines: Strs = list(takewhile(lambda line: len(line) == 0, lines))
    index: int = len(striped_lines)
    return lines[index:]


def _get_line_counts(line_attributes: LinePairs) -> Ints:
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
    line_attributes: LinePairs = _strip_line(source_text)
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
