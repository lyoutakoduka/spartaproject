#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to compare two dictionaries which store path and time stamp."""

from pyspartalib.context.extension.time_context import TimePair
from pyspartalib.context.file.json_context import Json
from pyspartalib.script.bool.compare_json import is_same_json
from pyspartalib.script.file.json.convert_to_json import multiple_to_json


def _get_stamp_json(times: TimePair) -> Json:
    return multiple_to_json(
        {path_text: time.isoformat() for path_text, time in times.items()}
    )


def is_same_stamp(left: TimePair, right: TimePair) -> bool:
    """Compare two dictionaries which store path and time stamp of the path.

    Args:
        left (TimePair): Time stamp of the path you want to compare.

        right (TimePair): Time stamp of the path you want to compare.

    Returns:
        bool: True if two dictionaries are same value.
    """
    return is_same_json(*[_get_stamp_json(times) for times in [left, right]])
