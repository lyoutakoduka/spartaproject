#!/usr/bin/env python

"""User defined types about type "datetime"."""

from datetime import datetime
from typing import Dict, List

Times = list[datetime]
TimePair = dict[str, datetime]

Times2 = list[Times]

TimePair2 = dict[str, TimePair]
