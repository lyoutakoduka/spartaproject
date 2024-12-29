#!/usr/bin/env python

"""User defined types about type "datetime"."""

from datetime import datetime
from typing import Dict, List

Times = List[datetime]
TimePair = Dict[str, datetime]

Times2 = List[Times]

TimePair2 = Dict[str, TimePair]
