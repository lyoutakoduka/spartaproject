#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to get latest date time of file or directory as time object."""

from pyspartaproj.context.extension.time_context import TimePair
from pyspartaproj.context.file.json_context import Json
from pyspartaproj.script.bool.compare_json import is_same_json
from pyspartaproj.script.file.json.convert_to_json import multiple_to_json


def _get_stamp_json(times: TimePair) -> Json:
    return multiple_to_json(
        {path_text: time.isoformat() for path_text, time in times.items()}
    )


def is_same_stamp(left: TimePair, right: TimePair) -> bool:
    """Compare 2 dictionaries which store path and time stamp of the path.

    Args:
        left (TimePair): Time stamp of the path you want to compare.

        right (TimePair): Time stamp of the path you want to compare.

    Returns:
        bool: True if 2 dictionaries are same value.
    """
    return is_same_json(*[_get_stamp_json(times) for times in [left, right]])
